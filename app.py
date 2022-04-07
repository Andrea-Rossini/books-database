from flask import Flask, request, render_template, jsonify, redirect
import sqlite3 as sql
import json

app = Flask(__name__)

id=None

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def split_query(qr):
    qr = qr.split()
    return qr

def dic_fun(cur, data):
    ar = []
    for row in data:
        dic = {}
        for idx, i in enumerate(cur.description):
            dic[i[0]] = row[idx]
        ar.append(dic)
    return ar

def sqlquery(qry):
    conn = sql.connect('books.db')
    cur = conn.cursor()

    cur.execute(qry)

    rows=cur.fetchall()
    return jsonify(dic_fun(cur, rows))

@app.route("/")
def home():
    var = "This is a simple API that fetch infos about books, you can search by id, title or author"
    return render_template('home.html', var=var)

@app.route("/search", methods=["GET"])
def query():
    results = []
    title = request.args.get("title")
    author = request.args.get("author")
    category = request.args.get("category")
    isbn = request.args.get("isbn")
    q_dict = dict({})

    if title is not None:
        title_query = "title LIKE '%"+title+"%'"
        q_dict['title'] = title_query

    if author is not None:
        author_query = "authors LIKE '%" + author + "%'"
        q_dict['author'] = author_query

    if category is not None:
        category_query = "categories LIKE'%" + category
        q_dict['category'] = category_query

    if isbn is not None:
        isbn_query = "isbn LIKE '%" + isbn + "%'"
        q_dict['isbn'] = isbn_query

    q_string = "SELECT * FROM books WHERE "

    for idx, val in enumerate(q_dict.values()):
        if idx < len(q_dict.values())-1:
            q_string += val+" AND "
        else:
            q_string += val+";"

    """for el in q:
        for book in books:
                for el in q:
                    if str(book["id"]) == el or el.lower() in book["title"].lower() or el.lower() in book["author"].lower():
                        results.append(book)
                        break"""
    return sqlquery(q_string)


@app.route("/search", methods=["POST"])
def search():
    p_title = request.form.get("title")
    p_author = request.form.get("author")
    p_category = request.form.get("category")
    p_isbn = request.form.get("isbn")
    p_dict = {}
    p_string = "/search?"

    if p_title != "":
        title_par = "title="+p_title
        p_dict['title'] = title_par

    if p_author != "":
        author_par = "author=" + p_author
        p_dict['author'] = author_par

    if p_category != "":
        category_par = "id=" + p_category
        p_dict['category'] = category_par

    if p_isbn != "":
        isbn_par = "isbn=" + p_isbn
        p_dict['isbn'] = isbn_par

    for idx, val in enumerate(p_dict.values()):
        if idx < len(p_dict.values())-1:
            p_string += val+"&"
        else:
            p_string += val

    return redirect(p_string)

@app.route("/all", methods=["POST"])
def all():
    qry = "SELECT * FROM books;"
    return sqlquery(qry)

@app.route("/query", methods=["GET", "POST"])
def sqlquery1(var):
    conn = sql.connect('books.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM books WHERE LOWER(categories) LIKE '%"+var.lower()+"% OR LOWER(title) LIKE '%"+var.lower()+"% OR LOWER(authors) LIKE '%"+var.lower()+"% OR LOWER(average_rating) LIKE '%"+var.lower()+"% OR LOWER(isbn) LIKE '%"+var.lower()+"% OR LOWER(isbn13) LIKE '%"+var.lower()+"% OR LOWER(language_code) LIKE '%"+var.lower()+"% OR LOWER(num_pages) LIKE '%"+var.lower()+"% OR LOWER(ratings_count) LIKE '%"+var.lower()+"% OR LOWER(text_reviews_count) LIKE '%"+var.lower()+"% OR LOWER(publication_date) LIKE '%"+var.lower()+"% OR LOWER(publisher) LIKE '%"+var.lower()+"%")

    rows=cur.fetchall()
    return jsonify(dic_fun(cur, rows))


if __name__ == '__main__':
   app.run(debug=True)
