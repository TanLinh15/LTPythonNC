import requests
from bs4 import BeautifulSoup
import os

# Khai báo url
url = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages'
# gán r = requests.get
r = requests.get(url)
# gán suop=BeautifulSuop( là 1 gói python để phân tích các cú pháp HTML)
suop = BeautifulSoup(r.text, 'html.parser')
# gán images bằng suop.find_all để tìm tất cả các tệp img
images = suop.find_all('img')

for images in images:
    name= images['alt']
    link=('https://developer.mozilla.org'+images['src'])
    print(name,link)
    with open(name.replace(' ','-').replace('/', '')+'.jpg','wb') as f:
        im = requests.get(link)
        f.write(im.content)