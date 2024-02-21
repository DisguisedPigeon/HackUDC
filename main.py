from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/image")
def image_test():
    image = [i for i in os.listdir('static/images') if i.endswith('.jpg')][0]
    return render_template('image.html', user_image = image)

@app.route("/")
def root():
    image = [i for i in os.listdir('static/images') if i.endswith('.jpg')][0]
    return render_template('index.html', user_image = image)
