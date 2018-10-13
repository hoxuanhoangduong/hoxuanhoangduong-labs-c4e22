from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
# print(webpage_text.prettify)
soup = BeautifulSoup(webpage_text, "html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div", "section-content")
ul = div.find("ul")
# print(ul)
li_list = ul.find_all("li")
# print(li_list)
itunes_list =[]
x = 0
for li in li_list:
    x += 1
    a = li.h3.a
    Names = a.string
    linka = a["href"]
    a2 = li.h4.a
    Artists = a2.string
    linka2 = a2["href"]
    Chart = {
        "Ranking": x,
        "Names": Names,
        "Artists": Artists,
    }
    itunes_list.append(Chart)

pyexcel.save_as(records= itunes_list, dest_file_name="iTunes top songs2.xlsx")