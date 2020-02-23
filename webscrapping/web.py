
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv
session = HTMLSession()

urls = []

for i in range(1,51):
     urls.append(f"http://books.toscrape.com/catalogue/page-{i}.html")
    
csv_file = open('book.csv' , 'w')
csv_writer= csv.writer(csv_file, lineterminator='\n')

csv_writer.writerow(['TITLE' , 'PRICE' , 'IMAGEURL'])
count = 1
for url in urls:
    source = session.get(url).html.html
    soup = BeautifulSoup(source , 'lxml')

    box = soup.find('ol')
    elements = box.find_all('li')
    title = []
    picture = []
    cost = []
    for element in elements:
        name = element.select('h3 a')[0]['title']
        title.append(name)
        image = element.select('img')[0]['src']
        image_url = r'http://books.toscrape.com/'+image
        picture.append(image_url)
        price = element.find('p' , class_='price_color').text
        cost.append(price)
        csv_writer.writerow([name, price, image_url])
        print(count, end='')
        count+=1

csv_file.close()


#     response = requests.get(url)
#     data = response.text
#     soup = BeautifulSoup(data, 'lxml')
#     print(soup.prettify())
#     print('.......................................................')
    # title=soup.find_all(class_="row")
    # for i in title:
    #     print(i.get_text())

# n=int(input("ENTER THE FIRST PAGE YOU WANT TO VISIT"))
# m=int(input("ENTER THE LAST PAGE YOU WANT TO VISIT"))
# for i in range(n,m+1):
#     url= "https://www.freepik.com/search?dates=any&format=search&page={}&query=wallpaper&selection=1&sort=popular&type=vector".format(i)
#     response = requests.get(url)
#     data = response.text
#     soup = BeautifulSoup(data, 'lxml')
#     print(soup.prettify())
#     print('......................................................................................')


