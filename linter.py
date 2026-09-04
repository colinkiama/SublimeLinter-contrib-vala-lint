import json

import sublime
from SublimeLinter.lint import Linter, LintMatch
from SublimeLinter.lint.quick_fix import TextRange, provide_fix_for


def byte_col_to_char_index(line_text, one_based_byte_col):
    """Convert a 1-based UTF-8 byte column (as reported by vala-lint) to a
    0-based character index into `line_text`."""
    if one_based_byte_col is None:
        return None

    encoded = line_text.encode('utf-8')
    byte_offset = max(0, min(one_based_byte_col - 1, len(encoded)))
    return len(encoded[:byte_offset].decode('utf-8'))


class ValaLint(Linter):
    cmd = (
        'io.elementary.vala-lint', '--stdin', '--stdin-filename',
        '${canonical_filename}', '--json-output', '--print-end'
    )
    defaults = {
        'selector': 'source.vala'
    }
    name = 'vala-lint'

    def find_errors(self, output):
        try:
            data = json.loads(output)
        except ValueError:
            self.logger.error(
                '{}: could not parse JSON output:\n{}'.format(self.name, output)
            )
            return

        for mistake in data.get('mistakes') or []:
            yield LintMatch({
                'line': mistake.get('line'),
                'col': mistake.get('column'),
                'end_line': mistake.get('endLine'),
                'end_col': mistake.get('endColumn'),
                'error_type': 'warning' if mistake.get('level') == 'warn' else 'error',
                'code': mistake.get('ruleId') or '',
                'message': (mistake.get('message') or '').strip(),
                'fix': mistake.get('fix'),
            })

    def process_match(self, m, vv):
        line = self.apply_line_base(m.line)
        end_line = (
            None if m.end_line is None else self.apply_line_base(m.end_line)
        )

        col = self.byte_col_for_line(vv, line, m.col)
        end_col = self.byte_col_for_line(
            vv, end_line if end_line is not None else line, m.end_col
        )

        adjusted = m.copy()
        adjusted.update({
            'line': line, 'col': col, 'end_line': end_line, 'end_col': end_col
        })

        error = super().process_match(adjusted, vv)
        if error is not None:
            error['fix'] = m.get('fix')

        return error

    def byte_col_for_line(self, vv, line, byte_col):
        if byte_col is None or line is None or line < 0 or line > vv.max_lines():
            return None

        return byte_col_to_char_index(vv.select_line(line), byte_col)


def _point_for_fix_position(view, position):
    line_region = view.line(view.text_point(position['line'] - 1, 0))
    line_text = view.substr(line_region)
    char_index = byte_col_to_char_index(line_text, position['column'])
    return line_region.a + char_index


@provide_fix_for('vala-lint', when=lambda error: error.get('fix') is not None)
def fix_vala_lint_mistake(error, view):
    fix = error['fix']
    start = _point_for_fix_position(view, fix['start'])
    end = _point_for_fix_position(view, fix['end'])
    yield TextRange(fix['replacement'], sublime.Region(start, end))
