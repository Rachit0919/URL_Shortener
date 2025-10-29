from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello to python learners from RachitCodes'


@app.route("/about")
def about():
    return "This is an amazing code on Python - Exclusive"


@app.route("/home")
def home():
    return "This is Home Page"

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)