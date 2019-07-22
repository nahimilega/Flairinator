import pickle
import os
import preprocess_test as ppt
from sklearn import *
from collections import Counter

# Na challa
def load(clf_file):
    with open(clf_file) as fp:
        clf = c.load(fp)
    return clf


def make_wordset():
    wordset = []
    f = open("final.txt", "r")
    for x in f:
        wordset.append(x[:-1])
    return wordset





def make_feature_matrix(all_comment_words, wordset):
    feature_matrix = []
    for word in wordset:
        feature_matrix.append(all_comment_words.count(word))

    return feature_matrix





if __name__ == "__main__":

    clf = pickle.load(open('text-classifier.mdl', 'rb'))
    d = make_wordset()
    features = []
    inp = """Life Pro Tip India - If you're getting spammed with "Personal Loan" calls, don't hang up or pick and abruptly cut the call. Pick the call, say you want the loan badly and tell them you're jobless and don't have any collateral. They're mark you as Junk on their CRM and steer clear of you."""
    all_comment_words = ppt.run(inp)
    feature_matrix = make_feature_matrix(all_comment_words, d)
    res = clf.predict([features])
    print(res)