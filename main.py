import requests
from bs4 import BeautifulSoup
import re
import os
directory =  r"your_directory" #directory where you've saved all txt files from final.py file
roi = 'no info on the website'
for file_name in os.listdir(directory):
    if file_name.endswith(".txt"):
        file_path = os.path.join(directory, file_name)
        with open(file_path, "r", encoding="utf-8") as file:
            contents = file.read()
            txtlink = re.findall(r"https://12min.com/\S+", contents)
            link = txtlink[0]
            print(link)
            page = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(page.content, "html.parser")
            reads = soup.select_one('span b').text
            if soup.find('strong', string='ISBN:'):
                if soup.find('strong', string='ISBN:').find_next().text == '':
                    isbn = roi
                else:
                    isbn = soup.find('strong', string='ISBN:').find_next().text
            else:
                isbn = roi
            if soup.find('strong', string='Publisher:'):
                if soup.find('strong', string='Publisher:').find_next().text == '':
                    publisher = roi
                else:
                    publisher = soup.find('strong', string='Publisher:').find_next().text
            else:
                publisher = roi
            with open(file_path, "a", encoding="utf-8") as txtfile:
                txtfile.write(f"Number of reads: {reads}\n")
                txtfile.write(f"ISBN: {isbn}\n")
                txtfile.write(f"Publisher: {publisher}\n\n")
                for element in soup.find(class_='col-lg-12').find_all(["p", "h2", "li"]):
                    txtfile.write(element.text + "\n\n")
