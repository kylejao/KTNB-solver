#!/usr/bin/env python

from collections import Counter

HELP = """
    [hh] Help
    [qq] Quit
    [rr] Reset

    Setting (Last Digit): <0-9>
    Input (Wire colors): <w|d|b|r|y>... ...
        For colors, use 'w' for white, 'd' for dark (black), 'b' for blue, 'r' for red, and 'y' for yellow.
"""

LAST_DIGIT = None


def solve3(s, counter):
  if counter['r'] == 0:
    return 2
  elif s[-1] == 'w':
    return -1
  elif counter['b'] > 1:
    return 'last blue'
  else:
    return -1


def solve4(s, counter):
  if counter['r'] > 1 and LAST_DIGIT & 1:
    return 'last red'
  elif counter['r'] == 0 and s[-1] == 'y':
    return 1
  elif counter['b'] == 1:
    return 1
  elif counter['y']:
    return 'last'
  else:
    return 2


def solve5(s, counter):
  if s[-1] == 'd' and LAST_DIGIT & 1:
    return 4
  elif counter['r'] == 1 and counter['y'] <= 1:
    return 1
  elif counter['d'] == 0:
    return 2
  else:
    return 1


def solve6(s, counter):
  if counter['y'] == 0 and LAST_DIGIT & 1:
    return 3
  elif counter['y'] == 1 and counter['w'] > 1:
    return 4
  elif counter['r'] == 0:
    return -1
  else:
    return 4


def solve(s):
  s = s.lower()
  method = (solve3, solve4, solve5, solve6)[len(s)-3]
  return method(s, Counter(s))


def run():
  _input = None
  while _input != 'qq':
    _input = raw_input("[SIMPLE WIRE] Last digit: ")
    if not _input:
      continue
    if _input == 'hh':
      print HELP
      continue
    if _input == 'qq':
      break
    if _input == 'rr':
      print "Restarted"
      continue

    try:
      if 9 < int(_input):
        raise Exception("Too large")
      LAST_DIGIT = int(_input)
    except Exception as e:
      print "Invalid input: ", e
      continue

    while True:
      _input = raw_input("[SIMPLE WIRE] Wire colors: ")
      if _input == 'hh':
        print HELP
        continue
      if _input == 'qq':
        break
      if _input == 'rr':
        print "Restarted"
        break

      for token in _input.split():
        print solve(token)


def main():
  run()

if __name__ == "__main__":
	main()
