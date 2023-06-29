# -*- coding: utf-8 -*-
"""This module downloads the data from the SurfDrive"""
import os
import urllib.request
import dvc
import gdown

if __name__ == '__main__':
    URL = "https://drive.google.com/file/d/1Uz3o1T1yItRZxAUHTCUoDP3ktglJ0uLO"
    FILENAME = "data/external/a1_RestaurantReviews_HistoricDump.tsv"

    if not os.path.exists('data/external'):
        os.makedirs('data/external')
    gdown.download(URL, FILENAME, quiet=True)