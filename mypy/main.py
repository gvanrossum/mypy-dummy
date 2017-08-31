#!/usr/bin/env python

import sys

def main():
    sys.stderr.write("Mypy-lang is no longer supported. "
                     "Please run 'pip uninstall mypy-lang' "
                     "and 'pip install mypy'\n")
    sys.exit(2)

if __name__ == '__main__':
    main()
