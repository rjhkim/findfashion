import os

from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)

@app.route("/", methods=['GET', 'POST'])
def index():



    return render_template('index.html')

# mongodb database
db = client.flask_database

# This is a collection called table
table = db.table

if __name__ == "__main__":
    app.run(debug=True)