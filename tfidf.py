import math

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

def computeIDF(docList):

    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log((N / float(val)), 100 )*10000000
    return idfDict


def find_wordset(all_words):

    wordset = set([])

    for one_flair in list(all_words.values()):
        wordset = wordset.union(set(one_flair))

    return wordset


def all_worddict(wordset, flairs):
    """A list of all the words seperately for all the flairs
    Returns:
        dict: with key as flair

    """
    worddicts = {}
    for flair in flairs:
        worddicts[flair] = dict.fromkeys(wordset, 0)

    return worddicts


def find_all_tf(flairs, worddicts, all_words):
    all_tf = {}
    for flair in flairs:
        all_tf[flair] = computeTF(worddicts[flair],all_words[flair])
    return all_tf

def map_word(worddicts, all_words, flairs):


    for flair in flairs:
        for word in all_words[flair]:
            worddicts[flair][word] += 1

    return worddicts




def run(all_flair_text):
    flairs = []
    all_words = {}

    for flair, words in all_flair_text.items():
        flairs.append(flair)
        all_words[flair] = words

    wordSet = find_wordset(all_words)

    #bowA = a
    #bowB = b

    #wordDictA = dict.fromkeys(wordSet, 0)
    #wordDictB = dict.fromkeys(wordSet, 0)

    worddicts = all_worddict(wordSet, flairs)



    worddicts = map_word(worddicts,all_words,flairs)

    '''
    for word in bowA:
        wordDictA[word]+=1

    for word in bowB:
        wordDictB[word]+=1
    '''

    '''
    tfBowA = computeTF(wordDictA, bowA)
    tfBowB = computeTF(wordDictB, bowB)
    '''
    all_tfs = find_all_tf(flairs, worddicts, all_words)



    # idfs = computeIDF([wordDictA, wordDictB])
    # tfidfBowA = computeTFIDF(tfBowA, idfs)
    # tfidfBowB = computeTFIDF(tfBowB, idfs)
    idfs = computeIDF(list(all_tfs.values()))

    all_tfidf = {}


    for flair in flairs:
        all_tfidf[flair] = computeTFIDF(all_tfs[flair], idfs)





    return all_tfidf


if __name__ == "__main__":
    all_tfidf = run({'aa':['The', 'cat', 'sat', 'on', 'my', 'face'],'bb':['The', 'dog', 'sat', 'on', 'my', 'bed']})

    print(all_tfidf)

    print(sorted(all_tfidf['aa'].items(), key =
             lambda kv:(kv[1], kv[0])))
    '''
    print(sorted(b.items(), key =
             lambda kv:(kv[1], kv[0])))
    '''
