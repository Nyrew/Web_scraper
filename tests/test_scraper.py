import os
from scraper.scraper import scrape

def test_scraper():
    scrape()
    assert os.path.exists("data/data.json")