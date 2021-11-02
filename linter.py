from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class __class__(Linter):
    cmd = 'io.elementary.vala-lint'
    regex = r''
    multiline = False
    defaults = {
        'selector': 'source.vala'
    }
