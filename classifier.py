import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filepath')
parser.add_argument('-test', '--test')

args = parser.parse_args()

print(args.filepath)
print(args.test)

filepaths = []
with open(args.filepath, 'r') as f:
    filepaths = [line.strip() for line in f.readlines()]

print(filepaths)

# if __name__ == "__main__":
#     files_filepath = sys.argv[1]
