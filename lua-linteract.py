#!/usr/bin/env python
# -*- coding: utf-8 -*-

# need to install [lupa](https://github.com/scoder/lupa) for bridging lua runtime

from pygments.lexers.scripting import LuaLexer
from lupa import LuaRuntime
from linteract import linteract

def main():
    context = { 'lexer': LuaLexer, }

    lua = LuaRuntime(unpack_returned_tuples=True)

    linteract(context, lua.execute, print_return=False)

if __name__ == '__main__':
    main()
