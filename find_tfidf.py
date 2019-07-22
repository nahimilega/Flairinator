
import tfidf


flairs = ['Photography','Politics', 'Non-Political', 'AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance', 'Science/Technology', 'Scheduled', 'Sports', 'Food' ]



def transfer(word, no):
    li = []
    for i in range(no):
        li.append(word)
    return li

def read_file(filename):
    flair_words = []
    f = open(filename, "r")
    for x in f:
        g = x.split("   ")

        li = transfer(g[0], int(g[1][:-1]))
        flair_words.extend(li)

    return flair_words


def get_all_words():
    all_words = {}
    for flair in flairs:
        filename = flair[1]+ flair[-1] + '.txt'
        all_words[flair] = read_file(filename)
    return all_words

def write(all_tfidf):
    for flair in flairs:
        ggg = sorted(all_tfidf[flair].items(), key =
                lambda kv:(kv[1], kv[0]))
        filename = flair[1]+ flair[-1] + 'tf' + '.txt'
        with open(filename, mode='w') as f:
            for k,v in ggg:
                f.write( ("%s   %s\n") % (k,v))



def run():
    all_words = get_all_words()
    all_tfidf = tfidf.run(all_words)
    print('####################################writing')
    write(all_tfidf)

if __name__ == "__main__":
    run()



