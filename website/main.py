from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

@app.route("/stats")
def stats():
    print("ho")
    return render_template("stats.html")


if __name__ == "__main__":
    app.run(debug=True)