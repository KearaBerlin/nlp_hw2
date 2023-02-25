import argparse
import sys
import random
import numpy as np
import nltk
from sklearn.model_selection import train_test_split
# Hi
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

# read in files, which will be a dictionary of lists of sentences;
# each list of sentences is a list of tokens.
author_datasets = {}
for filepath in filepaths:
    sentences = extract_sentences(filepath)
    author_datasets[filepath] = sentences

# train / test split
if args.testfile:
    train = author_datasets
    test = extract_sentences(args.testfile)
else:
    train = {} # get 90% of data from each file
    test = {} # remaining 10% from each file
    for filepath in filepaths:
        train_test = train_test_split(author_datasets[filepath], test_size=0.1)
        train[filepath] = train_test[0]
        test[filepath] = train_test[1]

for filepath in filepaths:
    print(f"{filepath} Train: {len(train[filepath])} Test: {len(test[filepath])}")
