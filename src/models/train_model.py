"""This module trains the model"""
import json
import os

import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def load_data():
    corpus = joblib.load('data/processed/corpus.joblib')
    dataset = pd.read_csv('data/external/a1_RestaurantReviews_HistoricDump.tsv',
                          delimiter = '\t', quoting = 3,
                          dtype={'Review': str, 'Liked': bool})
    cv = CountVectorizer(max_features = 1440)
    return corpus, dataset, cv

def get_split(random_state=42):
    """Get the train/test split"""
    corpus, dataset, cv = load_data()
    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values
    return train_test_split(X, y, test_size = 0.20, random_state = random_state)

def train_data(random_state=42):
    """Train the model"""
    X_train, X_test, y_train, y_test = get_split(random_state=random_state)

    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    return classifier, X_test, y_test

def accuracy(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    return accuracy_score(y_test, y_pred)

if __name__ == '__main__':
    # Load data
    corpus, dataset, cv = load_data()

    # Train
    classifier, X_test, y_test = train_data()

    # Save model
    joblib.dump(cv, 'data/processed/BoW_Vectorizer.joblib')
    joblib.dump(classifier, 'models/Classifier_Sentiment_Model.joblib')

    # Save metrics
    y_pred = classifier.predict(X_test)
    # print(accuracy_score(y_test, y_pred))

    if not os.path.exists('models/metrics'):
        os.makedirs('models/metrics')
    with open('models/metrics/Classifier_Sentiment_Model.json', 'w', encoding='utf-8') as file:
        json.dump({"accuracy": accuracy_score(y_test, y_pred)}, file)
