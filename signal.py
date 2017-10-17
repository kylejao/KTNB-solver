#!/usr/bin/env python

HELP = """
    [hh] Help
    [qq] Quit
    [rr] Reset

    Input (Letters): <a-z>...
"""

WORDS = [
  'about', 'after', 'again', 'below', 'could',
  'every', 'first', 'found', 'great', 'house',
  'large', 'learn', 'never', 'other', 'place',
  'plant', 'point', 'right', 'small', 'sound',
  'spell', 'still', 'study', 'their', 'there',
  'three', 'thing', 'think', 'three', 'water',
  'where', 'which', 'world', 'would', 'write',
]


def run():
  i, words = 0, set(WORDS)
  while True:
    _input = raw_input("[SIGNAL] #{} Letters: ".format(i+1))
    if not _input:
      continue
    if _input == 'hh':
      print HELP
      continue
    if _input == 'qq':
      break
    if _input == 'rr':
      i, words = 0, set(WORDS)
      print "Restarted"
      continue

    letters = set(_input)
    for w in list(words):
      if w[i] not in letters:
        words.discard(w)

    print "Possible Answers: ", list(words)
    i += 1


def main():
  run()


if __name__ == "__main__":
	main()
