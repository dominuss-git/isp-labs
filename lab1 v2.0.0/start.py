from collections import namedtuple
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

name = []
name.append("")

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/accept' , methods=["POST"])
def accept():
    name.clear()
    name.append(request.form['name'])
    return redirect("main")

Message = namedtuple('Message', 'id_ text tag mode')
messages = []

@app.route('/main',  methods=['GET'])
def main():
    return render_template("main.html", messages=messages, name=name[0])

@app.route('/add_message',  methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    id_ = len(messages) + 1
    mode = False
    messages.append(Message(id_, text, tag, mode))
    return redirect(url_for('main'))

@app.route('/check',  methods=['POST'])
def check():
    print("hyi")
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)