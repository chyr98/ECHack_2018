import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer 
import pickle
import string

REAL_PATH = './../news_scraper/thestar.csv'
FAKE_PATH = './../theonionscraper/page_data.csv'

real_df = pd.read_csv(REAL_PATH)
print(len(real_df.index))
fake_df = pd.read_csv(FAKE_PATH)
print(len(fake_df.index))
doc_df = fake_df.append(real_df)
print(len(doc_df.index))
print(np.array(doc_df)[323:325])

doc_df_array = np.array(doc_df)

vectorizer = CountVectorizer()

print(doc_df_array[0][2])
for i in range(len(doc_df_array)):
    print(i)
    
    doc_df_array[i][0] = ((str)(doc_df_array[i][0])).translate(None, string.punctuation)
    print(doc_df_array[i][2])
    doc_df_array[i][2] = ((str)(doc_df_array[i][2])).translate(None, string.punctuation)


left_vec_df = vectorizer.fit_transform(doc_df_array[:,0]).toarray()
right_vec_df = vectorizer.fit_transform(doc_df_array[:,2]).toarray()
vec_df = np.concatenate((left_vec_df, right_vec_df), axis=1)


X = vec_df
y = np.array(doc_df['classification'])
X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

clf = svm.SVC()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)

print(accuracy)

pickle.dump(clf, open("./model", 'wb'))



