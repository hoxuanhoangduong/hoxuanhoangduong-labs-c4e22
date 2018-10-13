from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")

soup = BeautifulSoup(webpage_text, "html.parser")
table = soup.find("table", style = "border-top: solid 1px #e6e6e6;border-left:solid 1px #cccccc;border-bottom:solid 1px #cccccc")
tr_list = table.find_all("tr")

data_list = []
for tr in tr_list:
    td_list = tr.find_all("td")
    subject_list = tr.find_all(text = True)
    for subject in subject_list:
        subject_data = {
            '':subject,
        }
        data_list.append(subject_data)

    for td in td_list:
        # print(td.prettify)
        quy4 = td_list[1].string
        quy1 = td_list[2].string
        quy2 = td_list[3].string
        quy3 = td_list[4].string
        data = {
            'Qúy 4-2016': quy4,
            'Quý 1-2017': quy1,
            'Quý 2-2017': quy1,
            'Quý 3-20117': quy3,
        }
        data_list.append(data)
pyexcel.save_as(records= data_list, dest_file_name="data.xlsx")
# print(data_list)
