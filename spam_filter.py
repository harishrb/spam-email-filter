import os
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


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


x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size = 0.2)

model = MultinomialNB()
model.fit(x_train, y_train)
pred = model.predict(x_test)
print(pred)
print(accuracy_score(y_test, pred))


while True:
    features = []
    message = raw_input('Message: ').split(' ')
    if message[0] == 'exit':
        joblib.dump(model, 'spam_filter.pkl')
        print('Exiting... Model saved as spam_filter.pkl')
        break
    else:
        for word in d:
            features.append(message.count(word[0]))
        result = model.predict([features])
        if result == 0:
            print('Not Spam!')
        else:
            print("Spam!")