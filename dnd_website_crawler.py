from bs4 import BeautifulSoup as bs
import urllib3

# initialize urllib3
http = urllib3.PoolManager()

url = 'http://dnd.wizards.com/articles/unearthed-arcana/'
base_url = 'http://dnd.wizards.com'

# store UA page with urllib3
response = http.request('GET',url)

# create BS object with UA page content
soup = bs(response.data, features='lxml')

# find 'article-feature' DIV and store it
feature = soup.find_all('div',{'class': 'article-feature'})[0]

# parse and store the article title
article_title = feature.div.div.h4.a.text

# parse and store the article URL
article_link = base_url + feature.article.div.a.get('href')

