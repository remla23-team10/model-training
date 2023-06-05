import os
import pytest
from src.models.train_model import train


@pytest.fixture()
def get_data_path():
    """
    Path that get_data.py saves the data
    """
    yield os.path.join("data", "external", "a1_RestaurantReviews_HistoricDump.tsv")


def test_data_exists(get_data_path):
    assert os.path.exists(get_data_path)

def test_train():
    # TODO: Report metrics
    accuracy, f1, precision, recall  = train()
    assert accuracy > 0.6

def test_nondeterminism_robustness():
    "Model Validation test"

    original_accuracy, _, _, _ = train()

    for seed in [10, 20, 30, 40, 50]:
        new_accuraccy, _, _, _ = train(seed)
        print(f"Accuracy with seed {seed} " + str(new_accuraccy), seed)
        print("Original accuracy " + str(original_accuracy))
        assert abs(original_accuracy - new_accuraccy) <= 0.15