#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

query = """select title, name
    from articles,
    authors where
    articles.author = authors.id;"""



def connect():
    """Connects do Database"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        return db,c
    except:
       "Unable to connect to database"

def make_query(query):
    """Makes query and return results"""
    db,c = connect()
    c.execute(query)
    return c.fetchall()
    db.close()



if __name__ == "__main__":
    results = make_query(query)
    print results
