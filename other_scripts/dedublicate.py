import pymongo
import json
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

def intilise_database2():
    """
    Initilse the database and make a table instance

    Returns
        pymongo object of the table

    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient['subreddit']
    maintable2 = mydb["posts2"]
    return maintable2

def store_in_database(maintable, all_post_info):
    """

    """

    maintable.insert_one(post)


if __name__ == "__main__":
    all_id = []
    count = 0
    maintable = intilise_database()
    maintable2 = intilise_database2()
    for post in maintable.find():
        if post['post_id'] not in all_id:
            count+=1
            store_in_database(maintable2, post)
            all_id.append(post['post_id'])
    print(count)