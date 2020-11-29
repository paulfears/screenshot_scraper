import requests
from bs4 import BeautifulSoup
import random
import urllib.request


def getUrl():
  letters = "abcdefghijklmnopqrstuvwxyz1234567890"
  url = ""
  for i in range(random.randint(4,7)) :
    url+=random.choice(letters)
  print(url)
  return url


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
for i in range(100):
  end = getUrl()
  req = requests.get("https://prnt.sc/"+end, headers=headers)

  soup = BeautifulSoup(req.text, features="html5lib")
  try:
    img_url = soup.find(id='screenshot-image')['src']
  except TypeError:
    continue
  if img_url == "//st.prntscr.com/2020/08/01/0537/img/0_173a7b_211be8ff.png":
    continue
  try:
    urllib.request.urlretrieve(img_url, "imgs/"+end+'.'+img_url.split('.')[-1])
  except urllib.error.HTTPError:
    with open('forbidden.txt', 'a') as f:
      f.write(img_url+"\n")