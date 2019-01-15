import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('integers', metavar='N', type=int, nargs='+')

# Arguments which are options, which take a value and store it in a variable
# e.g. foo is stored inside args.foo below
parser.add_argument('-f', '--foo', help='foo value')
parser.add_argument('-b', '--bar', help='bar value')
parser.add_argument('-z', '--baz', help='baz value')


# Arguments which are flags, which don't take a value but turns something on...
parser.add_argument('-t', '--turn-on', action='store_true')
parser.add_argument('-x', '--exclude', action='store_false')
parser.add_argument('-s', '--start', action='store_true')

parser.add_argument('files', help='list of file extensions', nargs='+')

args = parser.parse_args()
print(args)
