# Author Lauri Putkonen

# With argparse can write user-friendly command line interfaces.
# https://docs.python.org/dev/library/argparse.html
# Program defines what arguments are required on command line

import argparse

# prog="words" define name for program in print - default = sys.argv[0] aka filename
# usage="random text" overwrite default message on top of print
example = argparse.ArgumentParser(description="Print something",
                                  prog="Parsearg example",
                                  usage="%(prog)s prints",
                    # formatter_class value define how much information print shows
                                  formatter_class=argparse.RawTextHelpFormatter 
                                  )


# Add some argument options to print
# first parameter is name/flags.
# With "-" symbol you make optional arguments
# Without "-" symbol you can create positional argument to command -
# Example example.add_argument("start/stop") when its required with command
# nargs = how many arguments expected
example.add_argument("-s", "--s", "-S", help="Print random text", action="store_true")
example.add_argument("-m", help="Print %(prog)ss", action="store_true")
example.add_argument("-n", "-num", type=int, help="Sum numbers", nargs=2, 
                     metavar=("n1", "n2"))
example.add_argument("-v", "-version", action="version", version="%(prog)ss 0.1")


args = example.parse_args() # Save input
if args.m:
    print("This is example message")

if args.s:
    print("This is random text")

if args.n:
    print(args.n[0], "+", args.n[1], "=", args.n[0] + args.n[1])
