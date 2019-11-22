from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://tobyrush.com/theorypages/index.html'

base_url = 'https://tobyrush.com/theorypages/'
file_type_to_dl = 'pdf'
dl_dir = '/Users/xxx/Downloads/'

driver = webdriver.Chrome()
driver.get(url)
content = driver.page_source

soup = BeautifulSoup(content)

links = soup.find_all('a')

requied_files = [link.attrs['href'] for link in links if link.attrs['href'].endswith(file_type_to_dl)]

for file in requied_files:
    download_me = base_url + file
    dest_file = re.findall('[^/]+$', file)[0]
    print("Downloading", download_me, end=' ... ')
    try:
        urllib.request.urlretrieve(base_url+file, dl_dir+dest_file)
    except:
        print("Can't download file!")
    else:
        print("Ok!")

