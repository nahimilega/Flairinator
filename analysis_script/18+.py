import matplotlib.pyplot as plt
import pymongo



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





post = intilise_database('posts2')

over =  post.find({'spoiler': True}).count()
print(over)
alll =  post.find({}).count()

ookk = over*100/alll


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'over_18', ''
sizes = [ookk, 100-ookk ]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()