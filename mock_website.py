


import preprocess_test as ppt



flairs = ['Photography','Politics', 'Non-Political', 'AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance', 'Science/Technology', 'Sports', 'Food' ]


# This script contains the mock of the code that is used in the website to process the request by the user


def read_file(filename):
    flair_tfs = {}
    f = open(filename, "r")

    for x in f:
        g = x.split("   ")
        flair_tfs[g[0]] = float(g[1][:-1])

    return flair_tfs


def load_tfs():
    all_tf = {}
    for flair in flairs:
        filename = flair[1]+ flair[-1]+ 'tf' + '.txt'
        all_tf[flair] = read_file(filename)

    return all_tf


def got_word(word,all_tf, value):

    for k, v in all_tf.items():
        value[k] += v[word]
    return value

def define_final_value(val):
    fv = {}
    for flair in flairs:
        fv[flair] = val
    return fv

def find_flair(wordset, all_tf, new):
    final_value = define_final_value(1)
    for one_word in new:
        word_value = define_final_value(1)
        for word in wordset:
            if one_word in word or word in one_word :
                word_value = got_word(word, all_tf, word_value)

        for flair in flairs:
            final_value[flair] = final_value[flair]*word_value[flair]

    return final_value



if __name__ == "__main__":
    all_tf = load_tfs()
    wordset = list(all_tf['Politics'].keys())
    print("loading")
    inp = """IPS Blocking REDDIT - Post here with details please"""
    all_comment_words = ppt.run(inp)
    new = []
    for i in all_comment_words:
        new.append(i[1:])
    final_value = find_flair(wordset, all_tf, new)
    c = sorted(final_value.items(), key =
            lambda kv:(kv[1], kv[0]))
    print(type(c))
    print(c[-2][0])
    print(c[-1][0])
    print(c[-3][0])
