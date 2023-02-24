import argparse
import sys
import nltk

nltk.download('punkt')

parser = argparse.ArgumentParser()
parser.add_argument('filepath')
parser.add_argument('-test', '--testfile')

args = parser.parse_args()

def read_file(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        filepaths = [line.strip() for line in f.readlines()]
    return filepaths

filepaths = read_file(args.filepath)

# read in files
files = []
for filepath in filepaths:
    lines = read_file(filepath)
    sentences = [nltk.tokenize.word_tokenize(line) for line in lines]
    print(sentences[0])
# each line is a sample
# throw out samples that are <= 2 words

if args.testfile:
    train = [] # TODO read in all data from filepaths
    test = [] # read from args.testfile
else:
    train = [] # TODO get 90% of data from each filepaths
    test = [] # remaining 10% from each of filepaths

# if __name__ == "__main__":
#     files_filepath = sys.argv[1]
