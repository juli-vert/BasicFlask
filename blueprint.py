import flask_login
import json
from flask import (Flask, json, make_response, redirect, 
                Response, send_from_directory, url_for, 
                request, render_template, flash, session, 
                jsonify, Blueprint)

from models import User
from flask_cors import CORS, cross_origin

bprint = Blueprint('blueprint', __name__, url_prefix='/api')


@bprint.route('/function', methods=['POST'])
@cross_origin()
@flask_login.login_required
def function():
    if request.method == 'POST':
        userid = ''
        return jsonify(uid=userid)