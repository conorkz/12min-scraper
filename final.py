import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import pytz
import os
directory =  r"your_directory"
roi = 'no info on the website'
for x in range(1, 26):
    url = f'https://12min.com/categories/all?page={x}'
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")
    a = soup.select('a.library-box')
    for b in a:
        link = 'https://12min.com' + b['href'].replace(' ', '%20')
        if b.select_one('img'):
            cover = b.select_one('img')['src']
        else:
            cover = roi
        if b.select_one('p.mb-fix'):
            author = b.select_one('p.mb-fix').text.strip()
        else:
            author = roi
        if b.select_one('h3'):
            title = b.select_one('h3').text.strip()
        else:
            title = roi
        bf = re.sub(r"[^\w\s]", "", title)
        current_time = datetime.now(pytz.timezone('Europe/Berlin'))
        berlin = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        file_name = os.path.join(directory, f"{bf}.txt")
        suffix = 1
        while os.path.exists(file_name):
            file_name = os.path.join(directory, f"{bf} ({suffix}).txt")
            suffix += 1
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Title: {title}\n")
            file.write(f"Author: {author}\n")
            file.write(f"Link: {link}\n")
            file.write(f"Book cover: {cover}\n")
            file.write(f"Berlin time: {berlin}\n")
    print(f'page {x} is done')