import bs4
import urllib3

"""
html = open("AWC - ADDS METARs.html").read()
soup = bs4.BeautifulSoup(html)
soup = bs4.BeautifulSoup(html, "lxml")
tag_list = soup.find_all("p", clear="both")
tag = tag_list[0]
tag = tag.next_sibling
tag = tag.next_sibling
tag = tag.next_sibling
tag = tag.lstrip("\n")
"""

# http://www.aviationweather.gov/metar/data?ids=VNKT&format=raw&date=0&hours=0

def current_weather(code):

    
    pm = urllib3.PoolManager()

    url_begin = "http://www.aviationweather.gov/metar/data?ids="
    url_end = "&format=raw&date=0&hours=0"
    myurl = url_begin + code + url_end
    html = pm.urlopen(url=myurl, method="GET").data
    soup = bs4.BeautifulSoup(html, "lxml")
    tag_list = soup.find_all("p", clear="both")
    tag = tag_list[0]
    tag = tag.next_sibling
    tag = tag.next_sibling
    tag = tag.next_sibling
    tag = tag.lstrip("\n")

    return tag




