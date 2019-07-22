import praw
import pymongo



def intilise_database():
    """
    Initilse the database and make a table instance

    Returns
        pymongo object of the table

    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient['subreddit']
    maintable = mydb["posts2"]
    return maintable


def store_in_database(maintable, all_post_info):
    """

    """
    for post in all_post_info:
        maintable.insert_one(post)



def find_info_from_post_depricated(post):
    """
    Returns a dict of all the data
    """
    post = post['data']
    try:
        info = {
            'text': post['selftext'],
            'title':post['title'], #ok
            'flair':post['link_flair_text'], #ok
            'author': post['author'], # ok
            'time': post['created_utc'],  # ok
            'url':post['url'], # noneed
            'over_18': post['over_18'], #ok
            'no_comments':post['num_comments'], # ok
            'upvote':post['ups'], # ok
        }
        return info
    except:
        return {}

def find_info_from_post(submission):
    info = {
        'post_id':submission.id,
        'author':submission.author.name,
        'title':submission.title,
        'flair':submission.link_flair_text,
        'time': submission.created_utc,
        'over_18': submission.over_18,
        'num_comment':submission.num_comments,
        'upvote':submission.score,

        'text':submission.selftext,
    }
    return info






if __name__ == "__main__":


    r = praw.Reddit(client_id='z7qca-tKVKM3iA', \
                        client_secret='69ZHFSBGLJ_-EmZoV1pmdrOLCks', \
                        user_agent='archit/2.1'
                        )


    count = 1

    maintable = intilise_database()
    c = [aa for aa in r.subreddit('india').top('all')]
    print(len(c))
    '''
    for submission in r.subreddit('india').top('all')::
        info = find_info_from_post(submission)
        maintable.insert_one(info)
        count += 1
        print(count)

    '''

    print(count)
