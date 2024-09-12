# Parsing xml
# https://stackoverflow.com/questions/31276001/parse-xml-sitemap-with-python

import requests
import pandas as pd
import xmltodict

url = "https://www.gov.uk/sitemap.xml"
res = requests.get(url)
raw = xmltodict.parse(res.text)

data = [[r["loc"], r["lastmod"]] for r in raw["sitemapindex"]["sitemap"]]
print("Number of sitemaps:", len(data))
df = pd.DataFrame(data, columns=["links", "lastmod"])

"""
 	links 	lastmod
0 	https://www.gov.uk/sitemaps/sitemap_1.xml 	2024-09-12T02:50:03+00:00
1 	https://www.gov.uk/sitemaps/sitemap_2.xml 	2024-09-12T02:50:03+00:00
2 	https://www.gov.uk/sitemaps/sitemap_3.xml 	2024-09-12T02:50:03+00:00
3 	https://www.gov.uk/sitemaps/sitemap_4.xml 	2024-09-12T02:50:03+00:00

"""
