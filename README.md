
# subreddit-analyzer

Website url: [https://vast-plateau-92435.herokuapp.com/](https://vast-plateau-92435.herokuapp.com/) </br>

**Instructions to use website**
You can either enter the text of the post for which you want to know flair, or you can enter the URL of a valid reddit post. Make sure to select TEXT or URL from the dropdown. </br>
**After clicking on search button wait for 15 sec**

</br>



**Note**: Unfortunately I could not add the graph of the analysis of the data in the website because of memory problems. (I used up all 500 MB of memory provided by heroku, just barely managed to fit the website)
You can find all the graphs(that were to be posted on website) inside graph folder
## Directory Structure
Note: All the scripts are make by taking an assumption that the txt files needed are in the same directory as that of script.
**Website**: Contains the website (Made using flask) </br>
**tfidf**: Scripts to compute TF-IDF </br>
**tfs**: Contains files having TF-IDF value of all the words in a flair </br>
**wordcloud**: Word cloud of all the flairs </br>
**useless**: Contains some random scripts that were once used during development </br>
**storing_scripts**: Scripts used for scraping the reddit posts and comments </br>


## Installation

Download this repository
```
$ git clone https://github.com/nahimilega/subreddit-analyzer.git
```
Create a python virtual environment and activate it:
```
python3 -m venv ven
source ven/bin/activate
cd ven/
```

Use the package manager pip to install dependencies of this project
```
$ pip install -r requirements.txt
```

To run the website -
```
$ cd website
$ python deploy.py

```


## Database Model
(Note - I could not upload the comment db because of github limit of 100 mb)
#### Database name - Subreddit

**Collections**
**posts2** : Stores all the scraped posts

'post_id': post id  </br>
'author': name of the author , </br>
'title': Title of the post, </br>
'flair': Flair of the post, </br>
'time': Time of creation of the post(UTC), </br>
'over_18': (bool) is the post over 18, </br>
'num_comment': Number of comments on the post, </br>
'upvote': Upvotes on the posts, </br>

**comments**: Store all the comments of all the scraped posts
'body': Body of the comment, </br>
'time': Time of comment creation(UTC), </br>
'author': Author of comment, </br>
'upvotes': Upvotes on the comment, </br>

## Algorithms

## Data Collection

## Libraries Used
This project relies on Flask with Jinja for handling the web display and serving of pages. PRAW was used to scrape data from the reddit. For preprocessing of text, nltk is used.

## Major Learnings

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
