import sqlite3

conn = sqlite3.connect('tweets_prediction.db')
print("db created successfully")


conn.execute('''
CREATE TABLE TWEETS
( query TEXT NOT NULL,
tweet_text TEXT NOT NULL,
logistic_prediction INT NOT NULL,
naive_bayes_prediction INT NOT NULL,
random_forest_prediction INT NOT NULL
)
''')

print("Table created successfully.....")