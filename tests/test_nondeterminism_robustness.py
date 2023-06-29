"""Test for nondeterminism robustness"""
import joblib
from src.models.train_model import train

def get_trained_model():
    """Load the model"""
    yield joblib.load('models/Classifier_Sentiment_Model.joblib')

def test_nondeterminism_robustness():
    "Model Validation test"

    original_accuracy, _, _, _ = train()

    for seed in [10, 20, 30, 40, 50]:
        new_accuraccy, _, _, _ = train(seed)
        # print(f"Accuracy with seed {seed} " + str(new_accuraccy), seed)
        # print("Original accuracy " + str(original_accuracy))
        assert abs(original_accuracy - new_accuraccy) <= 0.15
