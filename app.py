from flask import Flask

app = Flask(__name__)

@app.route("/")
def my_first_app():
    with open("/todo-db/example.txt", "r") as fp:
         html = ""
         for line in fp:
             html += "<p>{0}</p>".format(line)
         return html
    #return "<h1>Hello World</h1>"

@app.route("/second-app")
def my_second_app():
    return "<h2>Second app is ready</h2>"
