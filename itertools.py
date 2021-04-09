# Task1 - 1 line
from itertools import groupby


lines = ('\n'
         'This is the\n'
         'first paragraph.\n'
         '\n'
         'This is the second.\n').splitlines()
# Use itertools.groupby and bool to return groups of
# consecutive lines that either have content or don't.
for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print(' '.join(frags))
# PRINTS:
# This is the first paragraph.
# This is the second.
