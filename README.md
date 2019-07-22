
# subreddit-analyzer

Website url: [https://vast-plateau-92435.herokuapp.com/](https://vast-plateau-92435.herokuapp.com/)

## Directory Structure
Note: All the scripts are make by taking an assumption that the txt files needed are in the same directory as that of script.
Website: Contains the website (Made using flask)
tfidf: Scripts to compute TF-IDF
tfs: Contains files having TF-IDF value of all the words in a flair
wordcloud: Word cloud of all the flairs
useless: Contains some randon scripts that were once used during development
storing_scripts: Scripts used for scraping the reddit posts and comments


## Database Model
(Note - I could not upload the comment db because of github limit of 100 mb)
#### Database name - Subreddit

**Collections**
**posts2** : Stores all the scraped posts

'post_id': post id,
'author': name of the author ,
'title': Title of the post,
'flair': Flair of the post,
'time': Time of creation of the post(UTC),
'over_18': (bool) is the post over 18,
'num_comment': Number of comments on the post,
'upvote': Upvotes on the posts,

**comments**: Store all the comments of all the scraped posts
'body': Body of the comment,
'time': Time of comment creation(UTC),
'author': Author of comment,
'upvotes': Upvotes on the comment,





## Referances:

Reddit API:
https://www.reddit.com/wiki/search#wiki_search_api

Text Classification Algorithm:
http://www.imedpub.com/articles/an-efficient-classification-model-for-unstructured-text-document.pdf
https://towardsdatascience.com/pre-processing-in-natural-language-machine-learning-898a84b8bd47
https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
https://en.wikipedia.org/wiki/Document_classification
https://medium.com/mlrecipies/document-classification-using-machine-learning-f1dfb1171935
https://towardsdatascience.com/algorithms-for-text-classification-part-1-naive-bayes-3ff1d116fdd8
https://www.scitepress.org/Papers/2016/59077/59077.pdf

WebApp:
https://www.tutorialspoint.com/flask/flask_sending_form_data_to_template.htm
