from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)

def show_wordcloud(data,file_name, title = None ):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40,
        scale=3,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.savefig(file_name + '.png')



flairs = ['Photography','Politics', 'Non-Political', 'AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance', 'Science/Technology', 'Scheduled', 'Sports', 'Food' ]

for flair in flairs:
    wordset = []
    filename = flair[1]+ flair[-1]
    f = open(filename + ".txt", "r")
    for x in f:
        g = x.split("   ")

        wordset.append(g[0])
    show_wordcloud(wordset,file_name=filename)
#show_wordcloud(Samsung_Reviews_positive['Reviews'])