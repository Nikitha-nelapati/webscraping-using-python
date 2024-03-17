import requests
from bs4 import BeautifulSoup
url="https://www.geeksforgeeks.org/java/"
r=requests.get(url)
htmlContent=r.content
print(htmlContent)
soup=BeautifulSoup(r.content,'html.parser' )
for i in soup.find_all('code'):
    print(i.get('href'))    

titles = soup.title
print(titles.string)

print(soup.find('p'))
print(soup.find_all('p'))
a = soup.find_all('p')
for i in a:
   print(i)
print(i.get('class'))
#print(soup.find('p')['class'])
print(soup.find('p').get_text())
print(soup.get_text())
anchor = soup.find_all('a')
print(anchor)
all = set()
for i in anchor:
    all.add(i.get('href'))