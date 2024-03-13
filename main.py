from flask import Flask, render_template
import json
app = Flask(__name__)
with open('readbooks.json') as file:
    books = json.load(file)

# Access the list of books in the JSON data

# Pass the list of books to the template
@app.route('/')
def book_details():
    
    return render_template('book.html', books=books)


if __name__ == '__main__':
    app.run()