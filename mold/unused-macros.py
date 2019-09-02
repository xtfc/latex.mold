
# unused-macros.py [file]
# if file is not given, ourmacros.sty is used

import re

def macros_in_file(file):
  newcommand_re = re.compile(r'\\(re)?newcommand{\\([^}]+)}')
  macros = []
  with open(file, 'r') as file:
    for line in file:
      line = line.strip()
      match = newcommand_re.match(line)
      if match:
        macros.append(match[2])
  return macros

def contents(file):
  with open(file, 'r') as file:
    return file.read()

def main():
  import sys
  import glob

  args = sys.argv
  file = args[1] if len(args) > 1 else 'ourmacros.sty'

  macros = [[macro, False] for macro in macros_in_file(file)]

  tex_file_contents = [contents(file) for file in glob.glob('*.tex')]
  for file_contents in tex_file_contents:
    for i, (macro, _) in enumerate(macros):
      if re.match(r'(.*\n)*.*\\' + macro + r'(\(|\)|{| |\$|\\|\n|\]|\[|_)', file_contents, re.MULTILINE):
        macros[i][1] = True

  for macro, found in macros:
    if not found:
      print(macro)


if __name__ == '__main__':
  main()
