import argparse
import sys
import random
import numpy as np
import nltk
from sklearn.model_selection import train_test_split

nltk.download('punkt')

parser = argparse.ArgumentParser()
parser.add_argument('filepath')
parser.add_argument('-test', '--testfile')

args = parser.parse_args()

def read_file(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        filepaths = [line.strip() for line in f.readlines()]
    return filepaths

def extract_sentences(filepath):
    lines = read_file(filepath)
    sentences = [nltk.tokenize.word_tokenize(line) for line in lines]
    sentences = [s for s in sentences if len(s) > 2]
    return sentences

filepaths = read_file(args.filepath)

# read in files, which will be a list of lists; each nested list is a list of sentences;
# each list of sentences is a list of tokens.
files = [[] for i in range(len(filepaths))]
for (i, filepath) in enumerate(filepaths):
    sentences = extract_sentences(filepath)
    files[i] = sentences

# train / test split
if args.testfile:
    train = []
    for (label, sentences) in enumerate(files):
        data = [(s, label) for s in sentences]
        train.extend(data)
    test = extract_sentences(args.testfile)
else:
    train = [] # get 90% of data from each filepaths
    test = [] # remaining 10% from each of filepaths
    for (label, sentences) in enumerate(files):
        data = [(s, label) for s in sentences]
        train_test = train_test_split(data, test_size=0.1)
        train.extend(train_test[0])
        test.extend(train_test[1])

print(f"Train: {len(train)} Test: {len(test)}")
