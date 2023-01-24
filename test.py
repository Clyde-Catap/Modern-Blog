import datetime

from flask import Flask, render_template
import requests
import time
import pandas as pd

CONTENT_API = 'https://api.npoint.io/33ec397d16be22f81da9'
data = requests.get(CONTENT_API)
data_json = data.json()


print(data_json)

for x in data_json:
    print(x['title'])

today = datetime.datetime.now()
print(today.strftime("%H:%M:%S"))
print(today.strftime("%b %d %Y"))

print(today.date())

@app.route(f'/post/<int:index>')
def post(index):
    data = requests.get(CONTENT_API)
    data_json = data.json()
    today = datetime.datetime.now()
    date = today.strftime("%H:%M:%S")
    tim = today.strftime("%b %d %Y")
    post = None
    for x in data.json():
        if x["id"] == index:
            post = x
    return render_template("post.html", post=post, date=date , tim=tim)
