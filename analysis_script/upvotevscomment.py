import numpy as np
import matplotlib.pyplot as plt
import pymongo

# Make chart of comments vs upvotes for all the flair
# All charts in graph folder

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



def make_graph(c,u, xx):
    N = 11
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27       # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = u
    rects1 = ax.bar(ind, yvals, width, color='c')
    zvals = c
    rects2 = ax.bar(ind+width, zvals, width, color='y')

    ax.set_ylabel('Average Number')
    ax.set_xticks(ind+width/2)
    ax.set_xticklabels( xx)
    ax.legend( (rects1[0], rects2[0]), ('Upvotes', 'Comments') )

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)


    plt.show()



flairs = ['Photography','Politics', 'Non-Political', 'AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance', 'Science/Technology', 'Scheduled', 'Sports', 'Food' ]


if __name__ == "__main__":
    xticket = tuple(flairs)
    db = intilise_database()
    final_comment = []
    final_upv = []
    for flair in flairs:
        count = db.find({'flair':flair}).count()
        comment = 0
        upvotes = 0
        for post in db.find({'flair':flair}):
            comment += post['no_comments']
            upvotes += post['upvote']

        comment = int(comment/count)
        upvotes = int(upvotes/count)
        final_comment.append(comment)
        final_upv.append(upvotes)






    make_graph(final_comment,final_upv,xticket)

