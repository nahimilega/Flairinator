from flask import Flask, render_template, request
import json
import preprocess_test as ppt
import requests



flairs = ['Photography','Politics', 'Non-Political', 'AskIndia', '[R]eddiquette', 'Policy/Economy', 'Business/Finance', 'Science/Technology', 'Sports', 'Food' ]



app = Flask(__name__)

carrier = {}

@app.route("/")
def home():
    carrier['all_tf'] = load_tfs()
    return render_template("home.html")


@app.route("/result", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        # print(request.json)
        ok = request.json
        #ok['query']
        #ook['query']
        wordset = list(carrier['all_tf']['Politics'].keys())
        print(ok)
        if ok["option"] == 'URL':
            inp = get_text_from_url(ok["query"])
        else:
            inp = str(ok['query'])

        if inp is None:
            return {'flair': 'Invalid DATA' ,'percent': ok['query']  }


        all_comment_words = ppt.runn(inp)
        new = []
        for i in all_comment_words:
                new.append(i[1:])
        final_value = find_flair(wordset, new)
        c = sorted(final_value.items(), key =
                lambda kv:(kv[1], kv[0]))

        final_flair = c[-2][0]+ ', ' + c[-1][0] + ', ' + c[-3][0]
        result = {'flair': str(final_flair) ,'percent': ok['query']  }
        return result

@app.route("/stats")
def stats():
    print("ho")
    return render_template("stats.html")



def get_text_from_url(url):
    if url[-1] == "/":
        url = url[:-1]
    try:
        r = requests.get(url+'.json',headers = {'User-agent': 'Analyze22 reddit22'})
        if r.status_code !=200:
            return None
        resp = json.loads(r.text)
    except:
        return None

    try:
        self_text = resp[0]['data']['children'][0]['data']['selftext']
    except:
        self_text = ''
    title = resp[0]['data']['children'][0]['data']['title']
    return title + self_text



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


def got_word(word, value):

    for k, v in carrier['all_tf'].items():
        value[k] += v[word]
    return value

def define_final_value(val):
    fv = {}
    for flair in flairs:
        fv[flair] = val
    return fv

def find_flair(wordset, new):
    final_value = define_final_value(1)
    for one_word in new:
        word_value = define_final_value(1)
        for word in wordset:
            if one_word in word or word in one_word :
                word_value = got_word(word, word_value)

        for flair in flairs:
            final_value[flair] = final_value[flair]*word_value[flair]

    return final_value







if __name__ == "__main__":
    app.run(debug=True)