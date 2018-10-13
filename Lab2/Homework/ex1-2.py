from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")

soup = BeautifulSoup(webpage_text, "html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div", "section-content")
ul = div.find("ul")
li_list = ul.find_all("li")

options = {
    'default_search':'ytsearch',
    'max_download':1,
    'format':'bestaudio/audio'
}

for li in li_list:
    a = li.h3.a
    Names = a.string
    linka = a["href"]
    a2 = li.h4.a
    Artists = a2.string
    linka2 = a2["href"]
    Chart = {
        "Names": Names,
        "Artists": Artists,
    }
    d = YoutubeDL(options)
    d.download([Names + Artists])
    
