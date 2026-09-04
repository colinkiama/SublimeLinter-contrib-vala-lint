SublimeLinter-contrib-vala-lint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-vala-lint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-vala-lint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [vala-lint](https://github.com/vala-lang/vala-lint). It will be used with files that have the “vala” syntax.

You can install the [Vala-TMBundle package](https://packagecontrol.io/packages/Vala-TMBundle) to automatically assign the "vala" syntax to Vala files.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `vala-lint` is installed on your system. There are installation instsructions here: https://github.com/vala-lang/vala-lint

This plugin requires a `vala-lint` build that supports `--stdin` and `--json-output`. If your `vala-lint` predates those options, upgrade it before using this plugin.

In order for `vala-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Quick fixes
For mistakes that `vala-lint` can auto-fix (e.g. trailing whitespace), this plugin exposes a SublimeLinter quick fix so they can be applied individually from the "SublimeLinter: Quick Fix" command / context menu.

To fix every auto-fixable mistake in the current file at once, run **Vala-Lint: Fix All Auto-Fixable Problems** from the Command Palette.

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
