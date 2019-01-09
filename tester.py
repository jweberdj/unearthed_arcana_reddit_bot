import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('dnd')

posts = []
url = 'http://dnd.wizards.com/articles/unearthed-arcana/'
for result in subreddit.search(url, sort='relevance', time_filter='month'):
    print(result)
