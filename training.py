import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

from preprocessing import Preprocessing

dataset = pd.read_csv('a1_RestaurantReviews_HistoricDump.tsv', delimiter = '\t', quoting = 3)

preprocesser = Preprocessing()

corpus = preprocesser.preprocess_dataset(dataset)

X = preprocesser.fit_transform(corpus)
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

classifier = GaussianNB()
classifier.fit(X_train, y_train)

preprocesser.save_vectorizer("BoW_Vectorizer.pkl")
joblib.dump(classifier, 'Classifier_Sentiment_Model') 

y_pred = classifier.predict(X_test)

print(accuracy_score(y_test, y_pred))