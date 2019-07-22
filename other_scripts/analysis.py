import pymongo
import json
from collections import Counter

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


if __name__ == "__main__":
    all_id = []
    count = 0
    ccc = 0
    maintable = intilise_database()
    #maintable2 = intilise_database2()
    for post in maintable.find():
        if post['over_18']:
            ccc +=1
        all_id.append(post['flair'])
    print(len(all_id))
    cc = Counter(all_id)
    print(cc)
    print(ccc)