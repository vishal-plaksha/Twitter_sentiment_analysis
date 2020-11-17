from flask import Flask, render_template, request, redirect, url_for

from joblib import load
from get_tweets import get_related_tweets

lr_pipeline = load("text_classification.joblib")
nb_pipeline = load("text_classification_nb.joblib")
rf_pipeline= load('text_classification_rf.joblib')
import sqlite3



def requestResults(query):
    tweets = get_related_tweets(query)
    tweets['query'] =  query
    tweets['Logistic_prediction'] = lr_pipeline.predict(tweets['tweet_text'])
    tweets['naive_bayes_prediction'] = nb_pipeline.predict(tweets['tweet_text'])
    tweets['random_forest_prediction'] = rf_pipeline.predict(tweets['tweet_text'])
    del tweets['created_at']
    del tweets['tweet_id']
    conn = sqlite3.connect('tweets_prediction.db')
    #print("db connected successfully")

    tweets.to_sql('TWEETS' , conn , if_exists= 'append' , index = False)
    del tweets['query']

    return tweets


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        query = request.form['search']
        return redirect(url_for('success', name=query))


@app.route('/success/<name>')
def success(name):
    # return "<xmp>" + str(requestResults(name)) + " </xmp> "
    tweet_frame = requestResults(name)
    return render_template('view.html', tables=[tweet_frame.to_html()])


if __name__ == '__main__':
    app.run(debug=True)

# tweets= requestResults("donald trump")
# print(type(tweets))
