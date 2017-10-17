#!/usr/bin/env python

HELP = """
    [hh] Help
    [qq] Quit
    [rr] Reset

    Setting (Last digit of serial#, parallel port, #batteries): <s<0-9>|pp|b<0-9>> ...  (order doesn't matter)
        For last digit of serial#, use 's' followed by a digit.
        For parallel port, use 'pp'. 
        For #batteries, use 'b' followed by a digit.
        Example: 'l8 b4' means last digit 8, no parallel port, and 4 batteries.
    Input (Wire colors): <w|b|r|p|d|x>... ...
        For colors, use 'w' for white, 'b' for blue, 'r' for red, and 'p' for purple (blue + red).
        For being lighting and starred, use 'd' for being lighting (deng), and 'x' for being starred (xing).
"""

LAST_DIGIT = None
PARALLEL_PORT = None
NUM_BATTERIES = None

GUIDE = {}
GUIDE[(True, True, 'P')] = 'D'
GUIDE[(True, True, 'R')] = 'B'
GUIDE[(True, True, 'B')] = 'P'
GUIDE[(True, True, 'W')] = 'B'

GUIDE[(True, False, 'P')] = 'P'
GUIDE[(True, False, 'R')] = 'C'
GUIDE[(True, False, 'B')] = 'D'
GUIDE[(True, False, 'W')] = 'C'

GUIDE[(False, True, 'P')] = 'S'
GUIDE[(False, True, 'R')] = 'B'
GUIDE[(False, True, 'B')] = 'P'
GUIDE[(False, True, 'W')] = 'D'

GUIDE[(False, False, 'P')] = 'S'
GUIDE[(False, False, 'R')] = 'S'
GUIDE[(False, False, 'B')] = 'S'
GUIDE[(False, False, 'W')] = 'C'


def solve(s):
  if len(s) > 3:
    raise Exception("Token too long")
  s = set(s.upper())
  is_starred = 'X' in s
  is_lighting = 'D' in s
  s.discard('X')
  s.discard('D')
  return GUIDE[(is_starred, is_lighting, 'W' if len(s) == 0 else s.pop())]


def run():
  _input = None
  while _input != 'qq':
    _input = raw_input("[COMPLEX WIRE] Last digit of serial#, parallel port, #battery: ")
    if not _input:
      continue
    if _input == 'qq':
      break
    if _input == 'hh':
      print HELP
      continue
    if _input == 'rr':
      print "Restarted"
      continue

    cut = {'P': False}
    try:
      for token in _input.split():
        if token.lower() == 'pp':
          cut['P'] = True
        elif token[0].lower() == 'b':
          cut['B'] = int(token[1]) >= 2
        elif token[0].lower() == 's':
          cut['S'] = int(token[1]) & 1
        else:
          raise Exception("Unrecongized input: " + token)
    except Exception as e:
      print "Invalid input: ", e
      continue

    if len(cut) != 3:
      print "Not enough info"
      continue

    cut.update({'C': True, 'D': False})
    while True:
      _input = raw_input("[COMPLEX WIRE] Wire colors: ")
      if not _input:
        continue
      if _input == 'qq':
        break
      if _input == 'hh':
        print HELP
        continue
      if _input == 'rr':
        print "Restarted"
        break
      for token in _input.split():
        try:
          print '1 (cut)' if cut[solve(token)] else '0 (keep)'
        except Exception as e:
          print "Invalid input: ", e


def main():
  run()

if __name__ == "__main__":
	main()
