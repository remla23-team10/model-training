"""This module preprocesses the data"""
import os

import joblib
import pandas as pd

from restaurant_preprocessing import Preprocessing


if __name__ == "__main__":
    pandas_dataset = pd.read_csv('data/external/a1_RestaurantReviews_HistoricDump.tsv',
                          delimiter = '\t', quoting = 3,
                          dtype={'Review': str, 'Liked': bool})
    preprocesser = Preprocessing()
    corp = preprocesser.preprocess_dataset(pandas_dataset)
    if not os.path.exists('data/processed'):
        os.makedirs('data/processed')
    joblib.dump(corp, 'data/processed/corpus.joblib')
