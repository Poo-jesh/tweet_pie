from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '69a103255588bfa095c76c8950958b50'

from tweet_plot import routes
