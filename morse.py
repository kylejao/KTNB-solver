#!/usr/bin/env python

HELP = """
    [hh] Help
    [qq] Quit

    Input (Code): <0|1|.|->... ...
        For dots, use '0' or '.'.
        For dashes, use '1' or '-'.
        Example: 010 ..--
"""

CHAR2CODE = {
  'A': '.-',     'B': '-...',   'C': '-.-.', 
  'D': '-..',    'E': '.',      'F': '..-.',
  'G': '--.',    'H': '....',   'I': '..',
  'J': '.---',   'K': '-.-',    'L': '.-..',
  'M': '--',     'N': '-.',     'O': '---',
  'P': '.--.',   'Q': '--.-',   'R': '.-.',
  'S': '...',    'T': '-',      'U': '..-',
  'V': '...-',   'W': '.--',    'X': '-..-',
  'Y': '-.--',   'Z': '--..'}

CODE2CHAR = {v: k for k, v in CHAR2CODE.iteritems()}


def run():
  while True:
    _input = raw_input("[MORSE] Code: ")
    if not _input:
      continue
    if _input == 'hh':
      print HELP
      continue
    if _input == 'qq':
      break

    try:
      for token in _input.split():
        print CODE2CHAR[token.replace('0', '.').replace('1', '-')]
    except Exception as e:
      print "Invalid code: ", e
      continue


def main():
  run()

if __name__ == "__main__":
	main()
