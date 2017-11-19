#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

# What are the most popular three articles of all time?
three_most_read =  """select articles.title, count(*) as num
    from articles, log
    where log.status like '%200%'
    and log.path like concat('/article/', articles.slug)
    group by articles.title, log.path order by  num desc limit 3"""

queries = [three_most_read]




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
    for query in queries:
        result = make_query(query)
        print result
