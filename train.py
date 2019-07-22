
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import csv
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from collections import Counter
from sklearn import svm

import pickle as c



flairs = ['Photography','Politics', 'Non-Political', 'AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance', 'Science/Technology', 'Scheduled', 'Sports', 'Food' ]

flair_label = {'Photography':1,'Politics':2, 'Non-Political':3, 'AskIndia':4, '[R]eddiquette':5, 'Policy/Economy':6, 'Business/Finance':7, 'Science/Technology':8, 'Scheduled':9, 'Sports':10, 'Food':11 }



def save(clf, name):
    f = open(name, 'wb')
    c.dump(clf, f)
    print('saved')


def convert_to_int(data):
    new = []
    for l in data:
        pp = list(map(int, l))
        sum = 0
        for aa in pp:
            sum += aa
            if sum != 0:
                new.append(pp)
                break
    return new


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    return convert_to_int(your_list)

def make_label(flair, no):
    label = []
    for i in range(no):
        label.append(flair_label[flair])
    return label

def run():
    labels = []
    feature = []
    for flair in flairs:
        file_name = flair[1]+ flair[-1] + '.csv'
        data = read_csv(file_name)
        feature.extend(data)
        labels.extend(make_label(flair, len(data)))
    return feature, labels






if __name__ == "__main__":
    features, labels = run()
    print("got")
    x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.1)
    print(Counter(y_train))
    print(Counter(y_test))
    print(len(x_test[1]))
    print(len(x_train[1]))
    print("break")
    clf = MultinomialNB()
    # clf = svm.SVC(kernel='poly')
    clf.fit(x_train, y_train)

    preds = clf.predict(x_test)
    print(accuracy_score(y_test, preds))
    save(clf, "text-classifier1.mdl")
    print(confusion_matrix(y_test, preds))