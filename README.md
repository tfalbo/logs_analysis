# Udacity - Logs Analysis

This project is part of [Udacity's Full Stack Nanodegree](https://br.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

# What?

A logs analysis script. It makes queries on a database to check statistics and errors on an articles website.

# How?

It's made with Python 3 and psycopg.
The database used is a PostgreSQL.


# Where?

The project runs on a Vagrant machine. For running it, you're gonna need Vagrant and Virtual Box.
After cloning the repository do:
```
$ vagrant up
$ vagrant ssh
```

Into the machine, you need to load the database into the vagrant machine.
The database file is available for download [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
After downloading the file, put it into the vagrant directory and then run:

```
$ psql -d news -f newsdata.sql
```

Now, for running the script just do:

```
$ python logs_analysis.py
```
