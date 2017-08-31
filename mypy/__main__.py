"""Mypy type checker command line tool."""

from mypy.main import main

def console_entry() -> None:
    main()

if __name__ == '__main__':
    main()
