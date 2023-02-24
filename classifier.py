import argparse
import sys
import numpy as np
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
# files = np.empty
files = [[] for i in range(len(filepaths))]
for (i, filepath) in enumerate(filepaths):
    lines = read_file(filepath)
    sentences = [nltk.tokenize.word_tokenize(line) for line in lines]
    files[i] = sentences
    # files = np.concatenate((files, sentences), axis=1)
print(len(files))

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
