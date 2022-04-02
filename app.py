from flask import Flask, request, render_template, jsonify, redirect

app = Flask(__name__)

id=None

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

books = [
    {'id': 0, 'title':'I promessi sposi', 'author':'Alessandro Manzoni'},
    {'id': 1, 'title':'La divina commedia', 'author':'Dante Alighieri'},
    {'id': 2, 'title':'Il decamerone', 'author':'Francesco Petrarca'},
    {'id': 3, 'title':'Il codice Da Vinci', 'author':'Dan Brown'},
    {'id': 4, 'title':'Il giro del mondo in 80 giorni', 'author':'Jules Verne'},
    {'id': 5, 'title':'L\'alchimista', 'author':'Paulo Coelho'},
    {'id': 6, 'title':'Harry Potter e la Pietra Filosofale', 'author':'J.K. Rowling'},
    {'id': 80, 'title':'Ottanta', 'author':'Ottantesimi'}
]
def split_query(qr):
    qr = qr.split()
    return qr

@app.route("/")
def home():
    var = "This is a simple API that fetch infos about books, you can search by id, title or author"
    return render_template('home.html', var=var)

@app.route("/search", methods=['GET'])
def query():
    results = []
    q = split_query(request.args.get("q"))
    for book in books:
        for el in q:
            if str(book["id"]) == el or el.lower() in book["title"].lower() or el.lower() in book["author"].lower():
                results.append(book)
                break
    return jsonify(results)
    #return "q = "+request.args.get("q")+"\nsplitted = "+str(q)


@app.route("/search", methods=["POST"])
def search():
    q = request.form.get("q")
    return redirect("/search?q="+str(q))

@app.route("/all", methods=["POST"])
def all():
    return jsonify(books)


if __name__ == '__main__':
   app.run(debug=true)
