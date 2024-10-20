import argparse
import os
from collections.abc import Sequence

def _detect_line_end(lines: [str]) -> str:
    # Empty file
    if len(lines) == 0:
        return '\n'
    line = lines[0]
    # File with one line
    if not line[-1] == '\n':
        return '\n'
    return '\r\n' if line[-2:] == '\r\n' else '\n'

def _have_header(desired_header: [str], actual_lines: [str], eof: str) -> bool
    may_match = actual_lines[:2]
    if not len(desired_header) == len(may_match):
        return False
    stripped = [l.rstrip(eof) for l in may_match]
    return desired_header == stripped

def _write_lines(filename: str, lines: [str], eof: str):
    with open(filename, mode='w') as f:
        f.write(eof.join(lines))

def _process_file(header: [str], filename: str) -> bool:
    with open(filename, mode='rb') as f:
        original_lines = f.readlines()

    eof = _detect_line_end(original_lines)
    if not _have_header(header, original_lines, eof):
        res = header + original_lines
        _write_lines(filename, res, eof)
        return True

    return False

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        'header',
        help='The desired file-header in string'
    )
    args = parser.parse_args(argv)

    header_lines = arg.header.split()


if __name__ == '__main__':
    raise SystemExit(main())
