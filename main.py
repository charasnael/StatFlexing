from flask import Flask, render_template, request
import json
app = Flask(__name__)
with open('readbooks.json', encoding='utf8') as file:
    books = json.load(file)

# Access the list of books in the JSON data

# Pass the list of books to the template
@app.route('/')
def book_details():
    # Get the selected sort option from the form
    sort_option = request.args.get('sort_option', default='Author')
    sort_order = request.args.get('sort_order', default='asc')

    # Toggle sort_order between 'asc' and 'desc' if not sorting by ReadFor
    next_sort_order = 'desc' if (sort_order == 'asc' and sort_option != 'ReadFor') else 'asc'

    # Sort the books based on the selected option and sort order
    if sort_option == 'ReadFor':
        # Reverse the sorting order for ReadFor
        sorted_books = sorted(books, key=lambda x: x[sort_option], reverse=(sort_order == 'asc'))
    else:
        sorted_books = sorted(books, key=lambda x: x[sort_option], reverse=(sort_order == 'desc'))

    print("Sort Option:", sort_option)
    print("Sort Order:", sort_order)
    print("Sorted Books:", sorted_books)  # Print sorted books for debugging

    return render_template('book.html', books=sorted_books, sort_option=sort_option, sort_order=next_sort_order)
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()