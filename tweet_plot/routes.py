from tweet_plot import app
from flask import flash, redirect, render_template, url_for
from tweet_plot.forms import Search
from os import path
import json
from tweet_plot.tweet import Analyzer


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('search.html')


@app.route('/search', methods=["GET", "POST"])
def search():
    form = Search()
    if form.validate_on_submit():
        if form.username.data:
            label = ["Positive", "Negative", "Neutral"]
            val = Analyzer(str(form.username.data))
            colour = ["#00a200", "#c90000", "#0001bc"]
            return render_template('search.html', form=form, label=label, colour=colour, val=val)
        else:
            flash('Enter a username', 'danger')
            return render_template('search.html', form=form, val='Null')
    else:
        return render_template('search.html', form=form, val='Null')
