"""This module trains the model"""
import json
import os

import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def train(seed=0):
    """Trains the model and saves it to disk"""
    # Load data
    corpus = joblib.load('data/processed/corpus.joblib')
    dataset = pd.read_csv('data/external/a1_RestaurantReviews_HistoricDump.tsv',
                          delimiter = '\t', quoting = 3,
                          dtype={'Review': str, 'Liked': bool})
    count_vectorizer = CountVectorizer(max_features = 1440)

    # Train
    x_train_array = count_vectorizer.fit_transform(corpus).toarray()
    y_values = dataset.iloc[:, -1].values
    x_train, x_test, y_train, y_test = train_test_split(x_train_array, y_values, test_size = 0.20, random_state = seed)

    classifier = GaussianNB()
    classifier.fit(x_train, y_train)

    # Save model
    joblib.dump(count_vectorizer, 'data/processed/BoW_Vectorizer.joblib')
    joblib.dump(classifier, 'models/Classifier_Sentiment_Model.joblib')

    return evaluate_model(classifier, x_test, y_test)

def evaluate_model(classifier, x_test, y_test):
    """Evaluates the model and returns the metrics"""
    y_test_prediction = classifier.predict(x_test)

    res_accuracy = accuracy_score(y_test, y_test_prediction)
    res_f1 = f1_score(y_test, y_test_prediction)
    res_precision = precision_score(y_test, y_test_prediction)
    res_recall = recall_score(y_test, y_test_prediction)

    return res_accuracy, res_f1, res_precision, res_recall

if __name__ == '__main__':
    accuracy, f1_sc, precision, recall = train()

    if not os.path.exists('models/metrics'):
        os.makedirs('models/metrics')
    with open('models/metrics/Classifier_Sentiment_Model.json', 'w', encoding='utf-8') as file:
        json.dump({"accuracy": accuracy, "f1-score": f1_sc, "precision": precision, "recall": recall}, file)
