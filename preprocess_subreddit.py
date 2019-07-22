from collections import Counter
import preprocess_flair as ppf
import tfidf


flairs = ['Photography','Politics', 'Non-Political', 'AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance', 'Science/Technology', 'Scheduled', 'Sports', 'Food' ]


def wri(flair_words, filename):
    cc = Counter(flair_words)
    with open(filename, mode='w') as f:
        for k,v in  cc.most_common():
            f.write( ("%s   %s\n") % (k,v))


def run():

    for flair in flairs:
        flair_words = ppf.run(flair)
        filename = flair[1]+ flair[-1] + '.txt'
        print(flair)
        wri(flair_words,filename)

    # a,b = tfidf.run(sports_posts,food_posts)

if __name__ == "__main__":
    run()