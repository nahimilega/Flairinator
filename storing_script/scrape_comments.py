import praw
import pymongo

# This post is used to scrape comments

def intilise_database():
    """
    Initilse the database and make a table instance

    Returns
        pymongo object of the table

    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient['subreddit']
    maintable = mydb["comments"]
    post_table = mydb['posts2']
    return maintable, post_table


def store_in_database(maintable, all_post_info):
    """

    """
    for post in all_post_info:

        maintable.insert_one(post)

def find_all_comments(submission, post_id):


    submission.comments.replace_more(limit=None)
    all_comment = []
    for comment in submission.comments.list():
        comment_data = find_comment_data(comment)
        comment_data['post_id'] = post_id
        all_comment.append(comment_data)

    return all_comment


def find_comment_data(comment):

    try:
        author = comment.author.name
    except:
        author = None


    info =  {
        'body':comment.body,
        'time':comment.created_utc,
        'author':author,
        'upvotes':comment.score,
    }
    return info



def update_post(submission, ids, post_table):

    post_table.update_one({'post_id':ids},{'$set':{'upvote_ratio':submission.upvote_ratio}})
    post_table.update_one({'post_id':ids},{'$set':{'spoiler':submission.spoiler}})




def run():
    maintable, post_table = intilise_database()

    r = praw.Reddit(client_id='', # Fill ME
                     client_secret='',
                     user_agent=' Reddit Analyze/1.3'
                     )

    count = 1
    for post in post_table.find():
        if count > 4224:
            submission = r.submission(id=post['post_id'])
            update_post(submission, post['post_id'], post_table)
            all_comment =  find_all_comments(submission, post['post_id'])


            store_in_database(maintable,all_comment)
            print(count)
        count += 1


if __name__ == "__main__":
    run()