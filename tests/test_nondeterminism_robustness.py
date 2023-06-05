import os
import sys
sys.path.append('src')
import joblib
from src.models.train_model import train_data, accuracy, get_split
import pytest

def get_trained_model():
    """Load the model"""
    yield joblib.load('models/Classifier_Sentiment_Model.joblib')

def test_nondeterminism_robustness():
    """Test the model's robustness to nondeterminism"""
    trained_model, X_test, y_test = train_data()
    acc_trained = accuracy(trained_model, X_test, y_test)

    for seed in [1, 2, 3]:
        trained_new, X_test, y_test = train_data(random_state=seed)
        # Print type of trained_new
        print(type(trained_new))
        acc_trained_new = accuracy(trained_new, X_test, y_test)
        print(f"Difference in accuracy for seed {seed}: {acc_trained_new - acc_trained}")
        assert abs(acc_trained_new - acc_trained) < 0.05


