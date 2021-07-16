# app.py

from flask import Flask, render_template, redirect, url_for, jsonify, request
from talk_mashup_bot import talk_mashup_bot

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/talk/new')
def new_talk():
    title = talk_mashup_bot.generateTitle()
    return render_template('new_talk.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)