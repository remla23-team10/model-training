from pprint import pprint
from src.models.train_model import train

def test_cv_features():
    """Test the model's accuracy with different number of features in the CountVectorizer"""
    accuracies = {}
    for cv_features in range(100, 2000, 100):
        new_accuracy, _, _, _ = train(cv_features=cv_features)
        accuracies[cv_features] = new_accuracy
    pprint(accuracies)
    # TODO Somehow do something with this