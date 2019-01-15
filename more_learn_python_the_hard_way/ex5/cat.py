import argparse

parser = argparse.ArgumentParser()

parser.add_argument('files', type=str, nargs='+', help='Single file or list of files to concat.')
parser.add_argument('-o', '--output', help='Output file to concat to or leave blank for STDOUT')
parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
parser.add_argument('-n', '--number', action='store_true', help='Print line numbers')

args = parser.parse_args()

# Need to remove the args.output from the args.input list
# if using same file extensions such as *.txt as input...
try:
  args.files.remove(args.output)
except ValueError:
  if args.verbose:
    print(">>> Output file does not exist or not specified!")

if args.verbose:
  print(">>> ARGS ARE: {}\n".format(args))

# Temp string holder for file contents from input
output = ''
line_number = 1

for input_file in args.files:
  try:
    with open(input_file) as f:
      if args.number:
        for line in f.readlines():
          output += f"{line_number}\t{line}"
          line_number += 1
      else:
        output += f.read()
  except FileNotFoundError:
    if args.verbose:
      print("File not found. Skipping to next one.")
    continue

if args.output != None:
  if args.verbose:
    print(f"Writing output to {args.output}")

  with open(args.output, "w") as f:
    f.write(output)
else:
  if args.verbose:
    print(">>> Showing output to stdout")
  print(output)
