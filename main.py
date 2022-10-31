# /usr/bin/main.py
# -*- coding="utf-8" -*-

import flask
from flask import Flask
import time
import random

app = Flask(__name__,static_url_path='/static',static_folder='static',template_folder='templates')

@app.route('/up.php')
def up():
    return flask.render_template('up.html')

@app.route('/down.php')
def down():
    return flask.render_template('down.html')

@app.route('/up')
def upd():
    return flask.render_template('up.html')

@app.route('/down')
def downd():
    return flask.render_template('down.html')

@app.route('/index.php')
def fakechoose():
    return flask.render_template('index.html')

@app.route('/')
def home():
    return flask.render_template('index.html')

# 上传表单
@app.route("/upload.php",methods=['POST'])
def uploadfile():
    uploaded_file = flask.request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename+str(time.localtime())+str(random.randint(1, 100)))
        #保存文件
        return "文件上传成功了!"
    else:
        return "文件上传失败了!"

def main():
    app.run()

if __name__=="__main__":
    main()