import requests
import pymongo
import time
import json


count = 0

subreddit = 'r/india/'

headers = {'User-agent': 'Analyze22 reddit22'}



links = ["https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522AskIndia%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Non-Political%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522%255BR%255Deddiquette%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Scheduled%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Photography%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Science%252FTechnology%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Politics%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Business%252FFinance%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Policy%252FEconomy%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Sports%2522&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%253A%2522Food%2522&restrict_sr=1"]





links = ["https://www.reddit.com/r/india/search.json?q=flair_name%3A%22AskIndia%22&restrict_sr=1",
'https://www.reddit.com/r/india/search.json?q=flair_name%3A"Non-Political"&restrict_sr=1',
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22%5BR%5Deddiquette%22&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22Scheduled%22&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22Photography%22&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22Science%2FTechnology%22&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22Politics%22&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22Business%2FFinance%22&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22Policy%2FEconomy%22&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22Sports%22&restrict_sr=1",
"https://www.reddit.com/r/india/search.json?q=flair_name%3A%22Food%22&restrict_sr=1"]














'''


links = ['https://www.reddit.com/r/india/hot.json',
         'https://www.reddit.com/r/india/top.json',
         'https://www.reddit.com/r/india/new.json',
         'https://www.reddit.com/r/india/rising.json',
         'https://www.reddit.com/r/india/controversial.json',
         ]

'''

# rising

def intilise_database():
    """
    Initilse the database and make a table instance

    Returns
        pymongo object of the table

    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient['subreddit']
    maintable = mydb["posts"]
    return maintable

def _requests(link):
    """
    Make request

    Args:
        link (str): Link to make the response
    Returns:
        server response

    """
    response = requests.get(link, headers = headers)
    if response.status_code != 200:
        print(("Request to %s unsuccessful reason %s") % (link, response.status_code)  )
        time.sleep(3)
        return _requests(link)
    return response


def find_info_from_response(response, link2):
    """
    Args:
        Get Json object

    Returns:
        list of dict of all the data
    """
    all_posts_this_page = []
    next_link, post_list =  remove_useless_stuff(response, link2)

    for post in post_list:
        info = find_info_from_post(post)
        if info != {}:
            all_posts_this_page.append(info)
    return next_link, all_posts_this_page


def find_info_from_post(post):
    """
    Returns a dict of all the data
    """
    post = post['data']
    text = ''
    if post['is_self']:
        text = post['selftext']
    try:
        info = {
            'text': text,
            'post_id':post['id'],
            'title':post['title'],
            'flair':post['link_flair_text'],
            'author': post['author'],
            'time': post['created_utc'],
            'over_18': post['over_18'],
            'no_comments':post['num_comments'],
            'upvote':post['ups'],
        }
        return info
    except:
        print(post['url'])
        return {}

def remove_useless_stuff(response, link2):
    '''
    return list of postes
    '''
    next_link = get_next_link(response['data']['after'], link2)
    response = response['data']['children']
    return next_link, list(response)

def get_next_link(after, link):
    print(after)
    if after is None:
        return 'end'
    next_link = link + '&after=' + after
    return next_link


def store_in_database(maintable, all_post_info):
    """

    """
    for post in all_post_info:
        maintable.insert_one(post)


def run():
    global count
    maintable = intilise_database()
    for link in links:
        link2 = link + '?&t=all'
        sort_list = [ '' , '&sort=top', '&sort=new', '&sort=comments']
        for t in sort_list:
            link2 = link2 + t
            print(link2)
            next_link = link2
            while True:
                response = _requests(next_link)
                response = json.loads(response.text)
                next_link, all_post_info = find_info_from_response(response, link2)
                count += len(all_post_info)
                print(count)
                store_in_database(maintable,all_post_info)
                if next_link == 'end':
                    break

if __name__ == "__main__":
    run()
