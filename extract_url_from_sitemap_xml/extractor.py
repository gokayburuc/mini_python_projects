import xmltodict
import requests


url = "https://www.themajesty.xyz/sitemap.xml"

sitemap = xmltodict.parse(requests.get(url).text)
# urls = [url["loc"] for url in sitemap["urlset"]["url"]]
#
# for x in urls:
#     print(x)


for t in sitemap:
    print(t)
