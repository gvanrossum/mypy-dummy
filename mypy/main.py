#!/usr/bin/env python

import sys

def main():
    message = "'mypy-lang' is no longer supported -- the current pip package is 'mypy'"
    banner = '=' * len(message)
    sys.stderr.write(banner + '\n')
    sys.stderr.write(message + '\n')
    sys.stderr.write(banner + '\n\n')
    sys.stderr.write("Please run\n"
                     "    python3 -m pip uninstall mypy-lang\n"
                     "followed by\n"
                     "    python3 -m pip install mypy\n")
    sys.exit(2)

if __name__ == '__main__':
    main()
