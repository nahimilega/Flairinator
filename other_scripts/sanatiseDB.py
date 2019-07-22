import pymongo
import json


# There are some rogure flaires in the subreddit
# Convert those rouge flairs to the mainstram
# flairs to avoid wasting of data



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
    maintable = intilise_database()
    result = maintable.update({'flair':'politics'},{'$set':{'flair':'Politics'}},multi=True)
    result = maintable.update({'flair':'POLITICS'},{'$set':{'flair':'Politics'}},multi=True)
    result = maintable.update({'flair':'Demonetization'},{'$set':{'flair':'Politics'}},multi=True)
    result = maintable.update({'flair':'Policy'},{'$set':{'flair':'Policy/Economy'}},multi=True)

    result = maintable.update({'flair':'Food &amp; Drink'},{'$set':{'flair':'Food'}},multi=True)
    result = maintable.update({'flair':':food: Food &amp; Drinks'},{'$set':{'flair':'Food'}},multi=True)
    result = maintable.update({'flair':'Policy &amp; Economy'},{'$set':{'flair':'Policy/Economy'}},multi=True)
    result = maintable.update({'flair':'/r/all'},{'$set':{'flair':'Non-Political'}},multi=True)
    result = maintable.update({'flair':'r/all'},{'$set':{'flair':'Non-Political'}},multi=True)

    result = maintable.update({'flair':'AMA'},{'$set':{'flair':'AskIndia'}},multi=True)
    result = maintable.update({'flair':'Casual AMA 9¾/10'},{'$set':{'flair':'AskIndia'}},multi=True)
    result = maintable.update({'flair':'AMA Concluded'},{'$set':{'flair':'AskIndia'}},multi=True)
    result = maintable.update({'flair':'Politics [OLD]'},{'$set':{'flair':'Politics'}},multi=True)
    result = maintable.update({'flair':'Science &amp; Technology'},{'$set':{'flair':'Science/Technology'}},multi=True)

    result = maintable.update({'flair':'Food Shitpost'},{'$set':{'flair':'Food'}},multi=True)
    result = maintable.update({'flair':'Food?'},{'$set':{'flair':'Food'}},multi=True)
    result = maintable.update({'flair':'FOOD &amp; DRINK'},{'$set':{'flair':'Food'}},multi=True)
    result = maintable.update({'flair':'FOOD'},{'$set':{'flair':'Food'}},multi=True)
    result = maintable.update({'flair':'Food/Drink'},{'$set':{'flair':'Food'}},multi=True)
    result = maintable.update({'flair':'🐢 are friends not food'},{'$set':{'flair':'Food'}},multi=True)


    result = maintable.update({'flair':'Politics -- Source in comments'},{'$set':{'flair':'Politics'}},multi=True)
    result = maintable.update({'flair':'Original Comics'},{'$set':{'flair':'Non-Political'}},multi=True)
    result = maintable.update({'flair':'Lifehacks'},{'$set':{'flair':'Non-Political'}},multi=True)
    result = maintable.update({'flair':'40 Martyrs'},{'$set':{'flair':'Non-Political'}},multi=True)
    result = maintable.update({'flair':'Goal Achieved!!!'},{'$set':{'flair':'Non-Political'}},multi=True)
    result = maintable.update({'flair':'Official Sadness Thread'},{'$set':{'flair':'Non-Political'}},multi=True)
    result = maintable.update({'flair':'Original Comics'},{'$set':{'flair':'Non-Political'}},multi=True)

    print(result)
