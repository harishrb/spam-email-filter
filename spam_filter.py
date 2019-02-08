import os
from collections import Counter

def dict():
    path = 'data/emails/'
    files = os.listdir(path)
    emails = [path + email for email in files]
    words = []

    for email in emails:
        f = open(email)
        words += f.read().split(" ")

    for i, word in enumerate(words):
        if not words[i].isalpha():
            words[i] = ""

        
    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(2000)

def dataset(dictionary):
    path = 'data/emails/'
    files = os.listdir(path)
    emails = [path + email for email in files]
    feature_vec = []
    labels = []

    for email in emails:
        data = []
        f = open(email)
        words = f.read().split(" ")

        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_vec.append(data)

        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)

    return feature_vec, labels

d = dict()
features, labels = dataset(d)


print('Feature vector length: ', len(features))
print('Label length: ', len(labels))


