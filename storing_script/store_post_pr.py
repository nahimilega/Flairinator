import praw
import pymongo


r = praw.Reddit(client_id='z7qca-tKVKM3iA', \
                    client_secret='69ZHFSBGLJ_-EmZoV1pmdrOLCks', \
                    user_agent='davehodg/0.1'
                    )


count = 0
cc =  list(r.subreddit('india').submissions(1475280000, 1480550400))
print(len(cc))


print(count)