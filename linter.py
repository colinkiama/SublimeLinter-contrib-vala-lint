from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class __class__(Linter):
    cmd = 'io.elementary.vala-lint'
    regex = r'^\s*(?P<line>\d+)\.(?P<col>\d+)\s*(?:(?P<error>error)|(?P<warning>warn))\s*(?P<message>.+)'
    multiline = False
    defaults = {
        'selector': 'source.vala'
    }
