import os
import pytest


@pytest.fixture()
def get_data_path():
    """
    Path that get_data.py saves the data
    """
    yield os.path.join("data", "external", "a1_RestaurantReviews_HistoricDump.tsv")


def test_data_exists(get_data_path):
    assert os.path.exists(get_data_path)
