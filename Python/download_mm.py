import urllib.request
import os

def get_page(url):
    pass


def download_mm(folder='OOXX', pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx"
    page_num = int(get_page(url))

    for i in range(page_num):
        page_num -= i
        page_url 