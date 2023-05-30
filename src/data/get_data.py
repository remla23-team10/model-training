# -*- coding: utf-8 -*-
"""This module downloads the data from the SurfDrive"""
import os
import urllib.request

if __name__ == '__main__':
    URL = "https://filesender.surf.nl/download.php?token=615ad465-952d-404a-807c-a407f22b74de&files_ids=13929500"
    FILENAME = "data/external/a1_RestaurantReviews_HistoricDump.tsv"

    if not os.path.exists('data/external'):
        os.makedirs('data/external')
    downloaded_file, headers = urllib.request.urlretrieve(URL, FILENAME)
