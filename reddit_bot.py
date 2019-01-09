import praw
from bs4 import BeautifulSoup as bs
import urllib3
import pdb
import re
import os
import time

def scrapePage():
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
    article_info = [article_title, article_link]
    return article_info




if not os.path.isfile('articles_posted.txt'):
    articles_posted = []
else:
    with open('articles_posted.txt','r') as f:
        articles_posted = f.read()
        articles_posted = articles_posted.split('\n')
        articles_posted = list(filter(None, articles_posted))

article_info = scrapePage()

if article_info[0] not in articles_posted:
    print(article_info)
    reddit = praw.Reddit('bot1')

    subreddit = reddit.subreddit('pythonforengineers')

    for submission in subreddit.hot(limit=5):
        print(submission.permalink)