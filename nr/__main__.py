# The MIT License (MIT)
#
# Copyright (c) 2018 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import sys

commands = [
  'admin',
  'archive',
  'grablicense',
  'jiratime',
  'py.blob',
  'versionupgrade'
]

command_map = {
  'grablicense': 'tools.grablicense',
  'jiratime': 'tools.jiratime',
  'versionupgrade': 'tools.versionupgrade'
}

def main(prog=None, argv=None):
  parser = argparse.ArgumentParser(prog=prog)
  parser.add_argument('command', choices=commands, nargs='?')
  parser.add_argument('argv', nargs='...')
  args = parser.parse_args(argv)
  if not args.command:
    parser.print_usage()
    sys.exit(0)
  module_name = 'nr.' + command_map.get(args.command, args.command)
  module = __import__(module_name, fromlist=[None])
  sys.exit(module.main(parser.prog + ' ' + args.command, args.argv))

if __name__ == '__main__':
  sys.exit(main())
