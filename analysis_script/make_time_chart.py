import datetime
import random
import matplotlib.pyplot as plt
import pymongo

from datetime import datetime
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




db = intilise_database()
# make up some data
ll = []
for post in db.find():
    timestamp = post['time']
    dt = datetime.fromtimestamp(timestamp)
    ll.append(dt.hour)

cc = Counter(ll)
x = []
y = []
for i in range(24):
    x.append(str(i)+":00" )
    y.append(cc[i])

plt.xlabel('Time (Hours) in UTC')
plt.ylabel('No of posts')
plt.plot(x,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()