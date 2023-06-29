# -*- coding: utf-8 -*-
"""This module downloads the data from the SurfDrive"""
import os
import urllib.request

if __name__ == '__main__':
    URL = "https://filesender.surf.nl/download.php?token=53ba886c-54c3-43f0-a2ce-6b94bbaf5953&files_ids=14624784"
    FILENAME = "data/external/a1_RestaurantReviews_HistoricDump.tsv"

    if not os.path.exists('data/external'):
        os.makedirs('data/external')
    downloaded_file, headers = urllib.request.urlretrieve(URL, FILENAME)
