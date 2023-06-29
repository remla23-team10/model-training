"""Test data validity"""
import os
import pytest
from src.models.train_model import train


@pytest.fixture(name="data_path")
def get_data_path():
    """
    Path that get_data.py saves the data
    """
    yield os.path.join("data", "external", "a1_RestaurantReviews_HistoricDump.tsv")

def test_data_exists(data_path):
    """
    Test that the data file exists
    """
    assert os.path.exists(data_path)

def test_train():
    """
    Test that the training rutine works and returns an accuracy > 0.6
    """
    accuracy, _, _, _ = train()
    assert accuracy > 0.6
