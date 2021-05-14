import sqlite3
#connect tweets.db database

con=sqlite3.connect("tweetsNormalized.db")
cur = con.cursor()

def twitterData():
    con=sqlite3.connect("tweetsNormalized.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tweets_users_normalized(
        id INT,
        user INT,
        screen_name TEXT,
        created_at TEXT,
        full_text TEXT,
        source TEXT,
        text TEXT,
        is_quote_status INT,
        quote_count INT,
        reply_count INT,
        retweet_count INT,
        favorite_count INT)""")
    con.commit()
    con.close()


twitterData()
