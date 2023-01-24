from flask import Flask, render_template, request
import requests
import time
import datetime
import smtplib

CONTENT_API = 'https://api.npoint.io/33ec397d16be22f81da9'


my_email = "cataptrial@gmail.com"
password = "ogkilmewyhynbjns"

app = Flask(__name__)

@app.route('/')
def home():
    data = requests.get(CONTENT_API)
    data_json = data.json()
    today = datetime.datetime.now()
    date = today.strftime("%H:%M:%S")
    tim = today.strftime("%b %d %Y")
    return render_template("index.html", blog=data_json , date=date, tim=tim)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


# @app.route('/1')
# def post():
#     return render_template("post.html")
#

@app.route('/<int:index>')
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

@app.route("/form-entry", methods=["POST", "GET"])
def form_entry():
    data = request.form
    username = data['name']
    email = data['email']
    phone = data["phone"]
    mess = data["message"]
    print(username)
    print(email)
    print(phone)
    print(mess)
    print('Working')

    conection = smtplib.SMTP("smtp.gmail.com", 587)
    conection.starttls()
    conection.login(user=my_email, password=password)
    conection.sendmail(from_addr=my_email, to_addrs="clydebryoncatap@gmail.com", msg="Subject: Registration Success!!\n\n"
                                                                                     f"Hello! {username}\n"
                                                                                     f"Your email: {email}\n"
                                                                                     f"Password: {password}"
                                                                                     f"Message: {mess}")
    conection.quit()


    return render_template("contact.html", msg_sent=True)


if __name__ == "__main__":
    app.run(debug=True)

