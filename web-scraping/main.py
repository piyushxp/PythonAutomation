


import requests
from bs4 import BeautifulSoup
url = 'https://internshala.com/internships/software%20development-internship-in-hyderabad'

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

title = soup.title
# print(title)


print(soup.find('span').get_text())


#to be continued