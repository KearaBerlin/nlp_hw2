import argparse
import math
import copy
import sys
import random
import numpy as np
import nltk
from sklearn.model_selection import train_test_split
from nltk.util import bigrams
from nltk.lm.preprocessing import padded_everygram_pipeline, pad_both_ends
from nltk.lm import MLE, StupidBackoff

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

train_bigram = {}
test_bigram = {}

lms = {}

for filepath in filepaths:

    train_bigram, train_vocab = padded_everygram_pipeline(2, train[filepath])

    # lm = MLE(2)
    lm = StupidBackoff(order=2)
    lm.fit(train_bigram, train_vocab)
    lms[filepath] = lm
    print(lm.vocab)

for label in filepaths:
    test_bigram, test_vocab = padded_everygram_pipeline(2, test[label])

    num_correct = 0
    for sentence in test_bigram:
    # for sentence in test[label]:

        sentence = [ngram for ngram in sentence]
        # bigram_sentence = list(bigrams(pad_both_ends(sentence, n=2)))

        best_perplexity = math.inf
        best_filepath = ""
        for (filepath, model) in lms.items():
            perplexity = model.perplexity(sentence)
            # perplexity = model.perplexity(bigram_sentence)

            if best_perplexity > perplexity:
                best_perplexity = perplexity
                best_filepath = filepath

        if label == best_filepath:
            num_correct = num_correct+1

    accuracy = num_correct/len(test[label])
    print(accuracy)

