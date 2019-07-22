import pymongo

import preprocess_text as ppt
import tfidf
from collections import Counter

def intilise_database(db_name):
    """
    Initilse the database and make a table instance

    Returns
        pymongo object of the table

    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient['subreddit']
    maintable = mydb[db_name]
    return maintable


def get_comments(comment_db, post_id, title, text):
    if title is None:
        title = ''
    if text is None:
        text = ''

    all_comment_words = []

    all_word = ppt.run(text)
    all_comment_words.extend(all_word)

    all_word = ppt.run(title)
    all_comment_words.extend(all_word)

    for comment in comment_db.find({'post_id':post_id}):
        text = comment['body']
        all_word = ppt.run(text)
        all_comment_words.extend(all_word)
    return all_comment_words


def run(flair):
    post_db = intilise_database('posts2')
    comment_db = intilise_database('comments')
    all_posts = []

    for post in post_db.find({'flair':flair}):
        post_id = post['post_id']
        title = post['title']
        text = post['text']
        print(post_id)
        all_posts.extend(get_comments(comment_db, post_id,title,text))

    return all_posts


'''
    print("#########SPORTS_DONE#############")
    with open("sport.txt", mode='w') as f:
        for k,v in flg.most_common():
            f.write( ("%s   %s\n") % (k,v))
    food_posts = []
    for post in post_db.find({'flair':'Food'}):
        post_id = post['post_id']
        print(post_id)
        food_posts.extend(get_comments(comment_db, post_id))

    a,b = tfidf.run(sports_posts,food_posts)
    cc = Counter(food_posts)

    with open("food.txt", mode='w') as f:
        for k,v in  cc.most_common():
            f.write( ("%s   %s\n") % (k,v))



    print(len(food_posts))
    print(len(cc))

    print("######################################################")
    print("######################################################")
    ggg = sorted(a.items(), key =
             lambda kv:(kv[1], kv[0]))
    print(ggg)
    with open("sporttf.txt", mode='w') as f:
        for k,v in ggg:
            f.write( ("%s   %s\n") % (k,v))
    print("######################################################")

    lll = sorted(b.items(), key =
             lambda kv:(kv[1], kv[0]))

    with open("foodttf.txt", mode='w') as f:
        for k,v in lll:
            f.write( ("%s   %s\n") % (k,v))
'''


if __name__ == "__main__":
    run('Sports')

