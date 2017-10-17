#!/usr/bin/env python

RED = map(set, ['C', 'B', 'A', 'AC', 'B', 'AC', 'ABC', 'AB', 'B'])
BLUE = map(set, ['B', 'AC', 'B', 'A', 'B', 'BC', 'C', 'AC', 'A'])
DARK= map(set, ['ABC', 'AC', 'B', 'AC', 'B', 'BC', 'AB' , 'C', 'C'])

HELP = """
    [rr] Reset
    [qq] Quit

    Input (Color + ABC): <<b|r|d><a|b|c> ...
      For colors, use 'b' for blue, 'r' for red, and 'd' for dark (black).
      Example: 'ra bb dc' for red-A, blue-B, and then dark-C.
"""


def run():
  lists = {'R': RED[:], 'L': BLUE[:], 'D': DARK[:]}
  while True:
    _input = raw_input("[SEQUENTIAL WIRE] Color + ABC: ")
    if not _input:
      continue
    if _input == 'hh':
      print HELP
      continue
    if _input == 'rr':
      lists = {'R': RED[:], 'L': BLUE[:], 'D': DARK[:]}
      print "Restarted"
      continue

    for token in _input.upper().split():
      try:
        color, abc = token[0], token[1]
        colors = lists[color]
        print '1 (cut)' if abc in colors[0] else '0 (keep)'
        colors.pop(0)
      except Exception as e:
        print "Invalid input: ", e
        continue


def main():
  run()

if __name__ == "__main__":
	main()
