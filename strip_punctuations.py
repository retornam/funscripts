from string import punctuation
import sys


def strip_punctuation(s):
    s = str(s)
    return ''.join(c for c in s if c not in punctuation)


print strip_punctuation(sys.argv[1:])

