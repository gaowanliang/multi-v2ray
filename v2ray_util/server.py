#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from flask import Flask, request
app = Flask(__name__)


@app.route('/fcu', methods=['POST'])
def index():
    if request.method == 'POST':
        if(request.form['pwd'] == '770ee90773804e85'):
            p = os.popen('v2ray fcu')
            x = p.read()
            os.popen('sudo systemctl restart v2ray.service')
            return x
    return "404 Not Found"


@app.route('/ll', methods=['POST'])
def i():
    if request.method == 'POST':
        if(request.form['pwd'] == '770ee90773804e85'):
            p = os.popen('v2ray ll')
            x = p.read()
            return x
    return "404 Not Found"


@app.route("/info", methods=['POST'])
def info():
    if request.method == 'POST':
        if(request.form['pwd'] == '770ee90773804e85'):
            p = os.popen('v2ray info')
            x = p.read()
            return x
    return "404 Not Found"


@app.route("/del/<index>", methods=['POST'])
def delu(index):
    if request.method == 'POST':
        if(request.form['pwd'] == '770ee90773804e85'):
            p = os.popen('v2ray delu '+index)
            x = p.read()
            os.popen('sudo systemctl restart v2ray.service')
            return x
    return "404 Not Found"


@app.route("/ban/<index>", methods=['POST'])
def ban(index):
    if request.method == 'POST':
        if(request.form['pwd'] == '770ee90773804e85'):
            p = os.popen('v2ray ban '+index)
            x = p.read()
            os.popen('sudo systemctl restart v2ray.service')
            return x
    return "404 Not Found"



@app.route("/restart", methods=['POST'])
def restart():
    if request.method == 'POST':
        if(request.form['pwd'] == '770ee90773804e85'):
            os.popen('sudo systemctl restart v2ray.service')
            return "done"
    return "404 Not Found"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
