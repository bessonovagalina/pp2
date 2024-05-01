# Databases

# Lets imagine a database with students
# Such a database will contain:
# - name
# - ID
# - study year
# - phone number

# Lets take a spreadsheet as an example of a database
# Table represents one class of entities (e.g. students)
# Rows in the table represent instances of this class, i.e.
# individual entities (students). Rows are also called records or tuples
# Columns represent attributes related to these entities

# RDB - Relational Database
# Relational databases store data also in tables. 

# RDBMS - Relational Database Management System

# CRUD - Create, Read, Update, Delete
# CRUD describes 4 main operations with the database

# PostgreSQL (also known as Postgres) will be used as our RDBMS

# To start, we need:
# - Download and install PostreSQL
#   - During installation you can leave everything on default
#   - Remember/Write down the password that you set during the installation
# - Install psycopg2 package
#   - pip install psycopg2 (or pip3)
#   - or
#   - pip install psycopg2-binary (or pip3)

import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='suppliers', 
    user='postgres', 
    password='241540G@ly@'
    )

# Create a cursor to work with the database
cur = conn.cursor()

# Querying the database
cur.execute('SELECT Version()')

db_ver = cur.fetchall()

print(db_ver)





