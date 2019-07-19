import requests
import pymongo
import time
import json


count = 0

subreddit = 'r/india/'

headers = {'User-agent': 'Analyze reddit'}

link = 'https://www.reddit.com/r/india.json'


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


def find_info_from_response(response):
    """
    Args:
        Get Json object

    Returns:
        list of dict of all the data
    """
    all_posts_this_page = []
    next_link, post_list =  remove_useless_stuff(response)

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
    try:
        info = {
            'text': post['selftext'],
            'title':post['title'],
            'flair':post['link_flair_text'],
            'author': post['author'],
            'time': post['created_utc'],
            'url':post['url'],
            'over_18': post['over_18'],
            'no_comments':post['num_comments'],
            'upvote':post['ups'],
        }
        return info
    except:
        return {}

def remove_useless_stuff(response):
    '''
    return list of postes
    '''
    next_link = get_next_link(response['data']['after'])
    response = response['data']['children']
    return next_link, list(response)

def get_next_link(after):
    print(after)
    next_link = link + '?after=' + after
    return next_link


def store_in_database(maintable, all_post_info):
    """

    """
    for post in all_post_info:
        maintable.insert_one(post)


def run():
    global count
    maintable = intilise_database()
    next_link = link

    while True:
        response = _requests(next_link)
        response = json.loads(response.text)
        next_link, all_post_info = find_info_from_response(response)
        count += len(all_post_info)
        print(count)
        store_in_database(maintable,all_post_info)

if __name__ == "__main__":
    run()
