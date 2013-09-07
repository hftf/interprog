#!/usr/bin/env python3

import nexus

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('source', type=str, nargs=1,
                    help='source language')
parser.add_argument('target', type=str, nargs=1,
                    help='target language')
args = parser.parse_args()

src = sys.stdin.read()
tgt = src
sys.stdout.write(tgt)
