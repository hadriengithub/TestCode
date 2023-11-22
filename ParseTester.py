import argparse

# create the parser and add arguments
parser = argparse.ArgumentParser(description="This is a XOR script")
parser.add_argument('string', type=str)

# parse and stock data in args
args = parser.parse_args()

# get the parsed data
print(args.string)
