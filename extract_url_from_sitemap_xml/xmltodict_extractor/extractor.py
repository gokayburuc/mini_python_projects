import xmltodict
import requests


url = "https://www.themajesty.xyz/sitemap.xml"

req = requests.get(url).content
sitemap = xmltodict.parse(req)

# write into file
with open("sitemap_dict.txt", "w") as wf:
    print(sitemap, file=wf)

# show urls
for x in sitemap["sitemapindex"]["sitemap"]:
    print("URL Found :\t", x['loc'])


def getXml(url):
    req = requests.get(url).content
    sitemap = xmltodict.parse(req)
    return sitemap
