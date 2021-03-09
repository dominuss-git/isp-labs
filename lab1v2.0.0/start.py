# !/usr/bin/env/ "pip3 install --no-cache-dir flask"
# !/usr/bin/env/ python3
from collections import namedtuple
from flask import Flask, render_template, redirect, url_for, request
# from storage import MongoService

app = Flask(__name__)

name = []
name.append("")

# storage = MongoService.get_instance()

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
    # for i in storage.get_data():
    #     messages.append(Message(*i))
    return render_template("main.html", messages=messages, name=name[0])

@app.route('/add_message',  methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    id_ = len(messages) + 1
    mode = False
    messages.append(Message(id_, text, tag, mode))
    # storage.save_data({"id_": id_, "text": text, "tag": tag, "mode": mode})
    return redirect(url_for('main'))

@app.route('/check',  methods=['POST'])
def check():
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host="192.168.31.5", port=8080, debug=True, use_reloader=True)
