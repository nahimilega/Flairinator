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
    maintable = mydb["comments"]
    return maintable


def store_in_database(maintable, all_post_info):
    """

    """
    for post in all_post_info:
        maintable.insert_one(post)

def find_all_comments(id):
    maintable = intilise_database()
    r = praw.Reddit(client_id='z7qca-tKVKM3iA', \
                     client_secret='69ZHFSBGLJ_-EmZoV1pmdrOLCks', \
                     user_agent='davehodg/0.1'
                     )

    submission = r.submission(id=id)
    submission.comments.replace_more(limit=None)
    all_comment = []
    for comment in submission.comments.list():
        comment_data = find_comment_data(comment)
        comment_data['post_id'] = id
        all_comment.append()

    store_in_database(maintable,all_comment)

def find_comment_data(comment):
    return  {
        'body':comment.body,
        'time':comment.created_utc,
        'author':comment.author.name,
        'upvotes':comment.score,
    }


def run()
    find_all_comments(id)