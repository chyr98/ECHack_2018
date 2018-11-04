import pickle
import pandas as pd
import numpy as np
import sklearn.feature_extraction.text import CountVectorizer

PATH = 

model = pickle.load(open("model",'rb'))

input_article = pandas.read_csv(PATH)
input_array = np.array(input_article)

input_array[0] = (str)(input_array[0]).translate(None, string.punctuation)
input_array[2] = (str)(input_array[2]).translate(None, string.punctuation)

vectorizer = CountVectorizer()

left_input = vectorizer.fit_transform(input_array[:,0]).toarray()
right_input = vectorizer.fit_transform(input_array[:,2]).toarray()

input_vec = np.concatenate((left_input,right_input), axis=1)

input_vec = input_vec.reshape(len(input_vec),-1)

prediction = model.predict(input_vec)
print(prediction)
