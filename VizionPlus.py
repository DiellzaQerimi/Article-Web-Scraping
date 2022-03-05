import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('articles.db')
c = conn.cursor()

headers = {
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1'
}

r = requests.get('https://www.vizionplus.tv/kategori/aktualitet/vendi/')
soup = BeautifulSoup(r.content, 'lxml')
products = soup.find_all('h2', {'class' : 'genpost-entry-title'})

headerlinks = []

for item in products:
    for link in item.find_all('a', href = True):
        headerlinks.append(link['href'])


for link in headerlinks:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')
    Title = soup.find('h1').text
    Article = soup.find('div', {'class':'entry-content'})
    #print(Title)
    for art in Article.find_all('p'):
        art = art.text
        print(art)
        print("Number of occurrences of the word ...", art.count("ri"))


    # c.execute('''INSERT INTO VizionPlus VALUES(?,?)''', (Title,art))
    # conn.commit()


