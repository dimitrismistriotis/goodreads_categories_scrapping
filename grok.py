#
# Make sure BeautifulSoup is installed, eg:
# pip install beautifulsoup4
#
from bs4 import BeautifulSoup

def list_file_to_csv_entries(filename):
  current_html = ''
  with open('list', 'r') as myfile:
    current_html = myfile.read()

  # print(current_html)

  soup = BeautifulSoup(current_html, 'html.parser')

  for i in soup.select('div.shelfStat'):
    category = i.select('a.actionLinkLite')[0].string
    number_of_books = i.select('div.smallText.greyText')[0].string.replace('books', '').replace(',', '').strip()
    print('"{0}","{1}"'.format(category, number_of_books))

list_file_to_csv_entries('list')
