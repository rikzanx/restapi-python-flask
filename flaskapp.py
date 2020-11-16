import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# create tes data
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    res = {
        'api':'Flask Python',
        'version':'1.0.0'
    }
    # return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
    return jsonify(res)

@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/books', methods=['GET'])
def api_id():
    # Cek apakah ada field request dengan key id
    if 'id' in request.args:
        try:
            id = int(request.args['id'])
        except ValueError:
            return "Error: id is not number "
    else:
        return "Error: No id field "
    
    # Membuat variable baru untuk mengisi return 
    results=[]

    for book in books:
        if book['id'] == id:
            results.append(book)
    
    return jsonify(results)
app.run()