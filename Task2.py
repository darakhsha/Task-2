import requests
from bs4 import BeautifulSoup

url = "https://www.interviewbit.com/python-interview-questions/#python-pep8-and-its-importance"

r = requests.get(url)
htmlcontent = r.content

soup = BeautifulSoup(htmlcontent, "html.parser")


#first question and answer
q = soup.find('section', class_='ibpage-article-header')
cont = q.find_all('h3')
for cont in cont:
    print(cont.text[0:19])

s = soup.find('article', class_='ibpage-article')
contents = s.find_next('p')
for contents  in contents :
    print(contents.text)

