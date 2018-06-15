'''
Created on 2018/05/08

@author: nemoto
'''
import re
import urllib
import csv
from time import sleep
from bs4 import BeautifulSoup

att_f = open('senya_att.csv', 'a')
nw_f = open('senya_nw.csv', 'a')

w1 = csv.writer(att_f, lineterminator='\n')
w2 = csv.writer(nw_f, lineterminator='\n')

# 最初と最後+1を入力する
for num in range(1450, 1675):

    night = str("%04d" % num)
    url = "https://1000ya.isis.ne.jp/"+night+".html"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html5lib")

    title = soup.title.string
    title_arr = re.split("[『』|]", title)
    book_title = title_arr[1]
    book_author = title_arr[2]

    top = soup.find("div", id="top")
    # if top is not None:
    index_code = top.find("img").get("src")[-6:-4]
    att_row = [book_title, book_author, index_code]
    print(att_row)
    w1.writerow(att_row)

    sleep(0.5)

    renkan = soup.find("div", class_="entry-content")
    for link in renkan.findAll("a"):
        if link.get("href") is not None:
            if "html" in link.get("href"):
                night_target = link.get("href")[-9:-5]
                link_row = [night, night_target, 1]
                print(link_row)
                w2.writerow(link_row)

    sleep(0.5)

att_f.close()
nw_f.close()