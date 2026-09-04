from itertools import chain

import sublime
import sublime_plugin

from SublimeLinter.lint import persist, util
from SublimeLinter.lint.quick_fix import apply_edits

from .linter import fix_vala_lint_mistake


class ValaLintFixAllCommand(sublime_plugin.TextCommand):
    def is_enabled(self):
        return bool(self.fixable_errors())

    def description(self):
        return 'Vala-Lint: Fix All Auto-Fixable Problems'

    def run(self, edit):
        errors = self.fixable_errors()
        if not errors:
            sublime.status_message('vala-lint: No auto-fixable problems found.')
            return

        edits = list(chain.from_iterable(
            fix_vala_lint_mistake(error, self.view) for error in errors
        ))
        apply_edits(self.view, edits)
        sublime.status_message(
            'vala-lint: Fixed {} problem{}.'.format(
                len(errors), '' if len(errors) == 1 else 's'
            )
        )

    def fixable_errors(self):
        filename = util.canonical_filename(self.view)
        return [
            error
            for error in persist.file_errors.get(filename, [])
            if error.get('linter') == 'vala-lint' and error.get('fix') is not None
        ]
