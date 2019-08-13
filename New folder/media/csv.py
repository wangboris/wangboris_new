from bs4 import BeautifulSoup
import json,re,csv
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from urllib.parse import urlparse, parse_qs
import os
with open("lawyers.csv",mode="r",encoding="utf-8") as f:
    reader=csv.reader(f,delimiter=",")
    for row_index, row_data in enumerate(reader):
        barcard,fullname,end_page=row_data
        print([barcard,fullname,end_page])

print("Product details extracted successfully!")