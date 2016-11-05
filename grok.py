#
# Make sure BeautifulSoup is installed, eg:
# pip install beautifulsoup4
#
from bs4 import BeautifulSoup

current_html = ''
with open('list', 'r') as myfile:
  current_html = myfile.read()

print(current_html)

soup = BeautifulSoup(current_html, 'html.parser')

for i in soup.select('div.shelfStat'):
  print(i.select('a.actionLinkLite')[0].string)
  print(i.select('div.smallText.greyText')[0].string.strip().replace('books', ''))
