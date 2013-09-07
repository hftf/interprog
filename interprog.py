#!/usr/bin/env python3

"""
Entry point for InTERProg
"""

import nexus

import argparse
import imp
import sys

def load_language(name):
    """ Load the specified language, and return a pair of functions
    implementing parsing and rendering. """
    parse = imp.load_source(name + "_parse", name + '/parse.py')
    render = imp.load_source(name + "_render", name + '/render.py')
    return (parse.parse, render.render)

# Load languages
LANGUAGE_NAMES = ['basic']
LANGUAGES = {}
for l in LANGUAGE_NAMES:
    LANGUAGES[l] = load_language(l)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, nargs=1,
                        help='source language')
    parser.add_argument('target', type=str, nargs=1,
                        help='target language')
    args = parser.parse_args()

    src = sys.stdin.read()
    tgt = src
    sys.stdout.write(tgt)
