
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

# This script preprocess the string it recieve


def convert_lowercase(all_words):
    lower_words = []
    for word in all_words:
        if not word.isdigit():
            lower_words.append(word.lower())

    return lower_words


def lemmarize(lower_words):
    lemmatizer = WordNetLemmatizer()
    lemmarized_words = []
    for word in lower_words:
        lemmarized_words.append(lemmatizer.lemmatize(word))

    return lemmarized_words


# sentences = nltk.sent_tokenize(lines) #tokenize sentences
# print(sentences)



def run(paragraph):
    nouns = [] #empty to array to hold all nouns
    # reduce to same case
    # remove stop words
    # find nouns
    # remove numbers


    example_sent = paragraph
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '%','?', '!', ':', ';', '(', ')', '[', ']','<','>' '{', '}','the','aware'])

    word_tokens = word_tokenize(example_sent)
    lower_words = convert_lowercase(word_tokens)

    lemmarized_words = lemmarize(lower_words)


    filtered_sentence = [w for w in lemmarized_words if not w in stop_words]

    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(filtered_sentence))):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            nouns.append(word)

    return nouns

if __name__ == "__main__":
    example_sent = """ Hi, a lot of us may not be aware, but the situation of the Assam floods is quite grim. Year after year, we have faced the brunt and came back and rebuild our state, and as such, may have become oblivious for the national media to cover our situation. Most of us are still unaware of the situation that our state has to go through every year, worse than the floods that have occurred in the other states, due to the lack of the limelight in the national media.\n\n&amp;#x200B;\n\n[https://www.businesstoday.in/latest/trends/assam-flood-15-dead-43-lakh-people-affected-90-percent-kaziranga-park-inundated-flood-news/story/364653.html](https://www.businesstoday.in/latest/trends/assam-flood-15-dead-43-lakh-people-affected-90-percent-kaziranga-park-inundated-flood-news/story/364653.html)\n\n[https://www.ndtv.com/india-news/assam-flood-live-updates-11-killed-over-26-lakh-affected-as-flood-situation-worsens-2069542](https://www.ndtv.com/india-news/assam-flood-live-updates-11-killed-over-26-lakh-affected-as-flood-situation-worsens-2069542)\n\n&amp;#x200B;\n\nAll this aside, it is just a humble request from me to all to just stand by our state at this perilous hour, as we stood by together during the recent Chennai or Kerala floods.\n\n&amp;#x200B;\n\nKindly urge you to donate, whatever the capacity, as it will go a long way in rebuilding our state back to normalcy and help save the lives of lakhs of people.\n\n&amp;#x200B;\n\nHere are a few links that you can donate to:\n\nPAYTM: [https://paytm.com/helpinghand/assam-chief-minister-s-relief-fund](https://paytm.com/helpinghand/assam-chief-minister-s-relief-fund)\n\nCM’s Relief fund direct link: [https://cm.assam.gov.in/relieffund.php](https://cm.assam.gov.in/relieffund.php)\n\n&amp;#x200B;\n\nI have personally bared the brunt of the floods earlier and this is slated as a flood of even greater proportions. Any small contribution will really go a long way! As we can admire the beauty of the North-East, let’s also join hands together to save it!\n\n&amp;#x200B;\n\nThank you for your time to go through this!\n\n&amp;#x200B;\n\nEdit:\n\nFor those of you who are either residing outside India or do not want to contribute to the CM Fund, you can contribute to reputable and proven NGO's such as Goonj which I hear is doing brilliant work.\n\n&amp;#x200B;\n\nAs much as 90% of the Kaziranga National Park has been submerged and most of the districts are still struggling to get back to normalcy. All able bodied men, women and children are tirelessly working towards rescue and assistance activities.\n\n&amp;#x200B;\n\nOn the other hand, it is shameful and insensitive to still expect people to attend the National Register of Citizens (NRC) hearings at dire times like this.  On one hand they have lost their homes and belongings and on the other hand they are fighting to ensure that their names are on the NRC.  """

    run(example_sent)
