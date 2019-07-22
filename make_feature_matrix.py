import pymongo
import csv
import preprocess_test as ppt
import tfidf
from collections import Counter



flairs = ['Politics','Photography', 'Non-Political', 'AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance', 'Science/Technology', 'Scheduled', 'Sports', 'Food' ]


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




def make_wordset():
    wordset = []
    f = open("final.txt", "r")
    for x in f:
        wordset.append(x[:-1])
    return wordset


def make_feature_matrix(all_comment_words, wordset):
    feature_matrix = []
    for word in wordset:
        feature_matrix.append(all_comment_words.count(word))

    return feature_matrix


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


def run(flair,wordset):
    post_db = intilise_database('posts2')
    comment_db = intilise_database('comments')
    flair_feature_matrix = []
    count = 0
    gg = post_db.find({'flair':flair}).count()
    gg = int(gg*0.4)
    print(gg)
    cursor = post_db.find({'flair':flair},no_cursor_timeout=True).sort([ ('no_comments', pymongo.DESCENDING), ('upvote', pymongo.DESCENDING) ])
    for post in cursor:
        post_id = post['post_id']
        title = post['title']
        text = post['text']
        print(post_id)
        all_comment_words = get_comments(comment_db, post_id,title,text)
        feature_matrix = make_feature_matrix(all_comment_words, wordset)
        flair_feature_matrix.append(feature_matrix)
        if count == gg:
            print(count)
            break
        count += 1
    cursor.close()


    return flair_feature_matrix

def write_in_csv(filename, flair_feature_matrix):

    with open(filename, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(flair_feature_matrix)
    csvFile.close()


if __name__ == "__main__":
    wordset = make_wordset()
    for flair in flairs:
        flair_feature_matrix = run(flair,wordset)
        file_name = filename = flair[1]+ flair[-1] + '.csv'
        write_in_csv(file_name, flair_feature_matrix)
        print(flair)