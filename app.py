from flask import Flask, Response
from flask_cors import CORS
import json
import logging

from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.imdb_users_resource import IMDBUserResource
from application_services.UsersResource.user_service import UserResource
from database_services.RDBService import RDBService as RDBService

from application_services.post_resource import PostResource
import datetime
import time

from flask import Flask, redirect, url_for, request, render_template, Response

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


# @app.route('/')
# def hello_world():
#     return '<u>Hello World!</u>'


# @app.route('/imdb/artists/<prefix>')
# def get_artists_by_prefix(prefix):
#     res = IMDBArtistResource.get_by_name_prefix(prefix)
#     rsp = Response(json.dumps(res), status=200, content_type="application/json")
#     return rsp


# @app.route('/users')
# def get_users():
#     res = UserResource.get_by_template(None)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp

# @app.route('/imdb/users/<prefix>')
# def get_users_by_prefix(prefix):
#     res = IMDBUserResource.get_by_name_prefix(prefix)
#     rsp = Response(json.dumps(res), status=200, content_type="application/json")
#     return rsp

# @app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
# def get_by_prefix(db_schema, table_name, column_name, prefix):
#     res = RDBService.get_by_prefix(db_schema, table_name, column_name, prefix)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp


# get all posts with no parent
@app.route('/api/posts', methods = ['GET'])
def get_store():
    res = PostResource.get_by_template(None)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

# get all post title include substr
@app.route('/api/posts/<substr>', methods = ['GET'])
def get_post_by_prefix(substr):

    res = PostResource.get_by_title_substr(substr)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

# get all post under <parent_pid>
@app.route('/api/posts/<parent_pid>/comments', methods = ['GET'])
def get_by_parentPid(parent_pid):
    res = PostResource.get_by_template({'parent_pid':parent_pid})
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp
    

@app.route('/api/posts' , methods=['post'])
def create_post():
    
    pid = int(PostResource.get_next_id("pid")[0]["max_id"]) + 1 if PostResource.get_next_id("pid")[0]["max_id"] != None else 0
    parent_pid = request.form.get('parent_pid')
    uni = request.form.get('uni')
    title = request.form.get('title')
    text = request.form.get('text')
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    PostResource.post_posts({
            'pid' : pid,
            'parent_pid': parent_pid,
            'uni':uni,
            'title': title,
            'text': text,
            'time': timestamp
            })

    return f"[{title}] are now posted by {uni}!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
