import sqlite3 as sql
from flask import jsonify
import json

def sqlquery(qry):
    conn = sql.connect('books.db')
    cur = conn.cursor()

    cur.execute(qry)

    rows=cur.fetchall()
    return dic_fun(cur, rows)

def dic_fun(cur, data):
    ar = []
    for row in data:
        dic = {}
        for idx, i in enumerate(cur.description):
            dic[i[0]]=row[idx]
        ar.append(dic)
    return ar
qry = "SELECT * FROM books WHERE title LIKE '%Harry%'"
print (json.dumps(sqlquery(qry), indent=4))


