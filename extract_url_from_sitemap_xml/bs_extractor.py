import requests
from bs4 import BeautifulSoup
import pandas as pd


def SoupObject(url):
    r = requests.get(url).text
    return BeautifulSoup(r, "lxml")


def UrlCollector(soupobject):
    urls_from_xml = []
    loc_tags = soupobject.find_all("loc")
    for loc in loc_tags:
        urls_from_xml.append(loc.get_text())
        print("URL adding : ", loc.get_text())
    print("All URLs are added!")
    return urls_from_xml


def WriteCSV(urllist):
    df = pd.DataFrame(urllist)
    df.to_csv("sitemap.csv")


if __name__ == "__main__":
    # url = "https://www.themajesty.xyz/sitemap.xml"
    url = input("Please Write Your URL:\n")

    soup = SoupObject(url)
    urllist = UrlCollector(soup)
    WriteCSV(urllist)

    pass
