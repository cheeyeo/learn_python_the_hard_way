import sys
import getopt

def main():
  # Grab all the options apart from the filename
  args = sys.argv[1:]

  for arg in args:
    if arg == '-h':
      print("""
        usage: python test_sysargs.py [-h] [-f FOO] [-b BAR] [-z BAZ] [-t] [-x] [-s]

        optional arguments:
          -h, --help         show this help message and exit
      """)

if __name__ == '__main__':
  main()
