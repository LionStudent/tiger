from flask import Flask

from flask import request

from flask import jsonify


import store


app = Flask(__name__)


@app.after_request

def after_request(response):

  response.headers.add('Access-Control-Allow-Origin', '*')

  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')

  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

  return response


@app.route('/')

def welcome():

    return '''

<html>

    <head></head>

    <body>

        <h1>COVID-19 REST API</h1>

        <p>Welcome to the "COVID-19 Data" mirocservice endpoint.</p>

    </body>

</html>

'''


@app.route('/receiveAllPosts', methods=['GET'])

def getPosts():

    name = request.args.get('name')

    posts = store.searchTextData(name)

    return jsonify(posts)

