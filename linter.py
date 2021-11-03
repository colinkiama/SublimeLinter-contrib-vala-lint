from SublimeLinter.lint import Linter


class ValaLint(Linter):
    cmd = 'io.elementary.vala-lint ${file}'
    regex = r'^\s*(?P<line>\d+)\.(?P<col>\d+)\s*(?:(?P<error>error)|(?P<warning>warn))\s*(?P<message>(.\S{1,})+)\s*(?P<code>(.\S{1,})+)'
    multiline = False
    defaults = {
        'selector': 'source.vala'
    }
