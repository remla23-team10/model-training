# -*- coding: utf-8 -*-
import urllib.request

if __name__ == '__main__':
    URL = "https://filesender.surf.nl/download.php?token=615ad465-952d-404a-807c-a407f22b74de&files_ids=13929500"
    FILENAME = "data/external/a1_RestaurantReviews_HistoricDump.tsv"
    downloaded_file = urllib.request.urlretrieve(URL, FILENAME)
