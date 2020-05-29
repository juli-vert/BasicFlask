from app import app
import flask_login
import json
from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)

from models import User
from flask_cors import CORS, cross_origin
import jinja2
from yaml import safe_load

@app.route('/')
def defaultSite():
    session.permanent = True
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    global _db
    if request.method == 'GET':
        return render_template('login.html', logout=request.args.get('logout'))
    else:
        return redirect(url_for('protected'), code=307)

@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for('login', logout="True"), code=307)

@app.route('/protected', methods=['GET'])
@flask_login.login_required
def search():
    uid = flask_login.current_user.id
    usr = ''
    #usr = get user from database
    return render_template('main.html', user=usr)