#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
from prompt_toolkit.contrib.shortcuts import get_input
from prompt_toolkit.history import History
from pygments.style import Style
from pygments.token import Token
from pygments.styles.default import DefaultStyle

class DocumentStyle(Style):
    styles = {
        Token.Menu.Completions.Completion.Current: 'bg:#00aaaa #000000',
        Token.Menu.Completions.Completion: 'bg:#008888 #ffffff',
        Token.Menu.Completions.ProgressButton: 'bg:#003333',
        Token.Menu.Completions.ProgressBar: 'bg:#00aaaa',
    }
    styles.update(DefaultStyle.styles)

def linteract(input_context, run=None, print_return=True):

    context = { 'message': '>>> ',
                'history': History(),
                'style': DocumentStyle,
                'enable_system_prompt': True, }

    context.update(input_context)

    while True:
        try:
            text = get_input(**context)
        except EOFError:
            break
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            continue

        if run:
            try:
                if print_return:
                    print(run(text))
                else:
                    run(text)
            except:
                print(traceback.format_exc(), end='')
