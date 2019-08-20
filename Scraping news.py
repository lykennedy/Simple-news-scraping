import requests
from bs4 import BeautifulSoup
from os.path import join
import sys
import os
import pandas


def file_exist():
    return os.path.isfile(r"C:\Users\Kennedy\Desktop\news.txt") and os.path.getsize(r"C:\Users\Kennedy\Desktop\news.txt") > 0


def write(news):
    print("Creating a new file...")
    path = r"C:\Users\Kennedy\Desktop"
    name = 'news.txt'
    if file_exist():
        file = open(join(path, name), 'w')
        file.close()
    for x in news:
        try:
            file = open(join(path, name), 'a')
            file.write(x + '\n')
            file.close()
        except:
            print("Something went wrong..")
            sys.exit(0)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get('https://www.wane.com/', headers=headers)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
news = []
contents = soup.find_all('h3', {'class': 'article-list__article-title'})
for content in contents:
    d = {}
    if content.has_attr('href'):
        print(True)
    d["Headline:"] = content.find('a').text.replace("\n", '').replace('\t', '')

    try:
        d["Link:"] = content.find('a')['href']
    except:
        d["Link:"].append(None)

    print(d)
    news.append(d)
df = pandas.DataFrame(news)
if os.path.isfile(r'C:\Users\Kennedy\PycharmProjects\Scanning faces\news1.csv'):
    os.remove(r'C:\Users\Kennedy\PycharmProjects\Scanning faces\news1.csv')

df['Link:'] = '=HYPERLINK("' + df['Link:'] + '")'
df.to_csv('news1.csv')



