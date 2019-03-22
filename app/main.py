from flask import Flask, render_template, request

from ozon import create_book, add_book, search_books


def main():
    app = Flask(__name__)

    books_list = []

    war_and_piece = create_book(
        'Война и мир',
        'Толстой',
        1000,
        True,
        'война, любовь'
    )

    anna_karenina = create_book(
        'Анна Каренина',
        'Толстой',
        500,
        False,
        'поезд, любовь'
    )

    idiot = create_book(
        'Идиот',
        'Достоевский',
        700,
        True,
        'роман, любовь, драма, достоевский'
    )

    crime_and_justice = create_book(
        'Преступление и наказание',
        'Достоевский',
        700,
        False,
        'роман, достоевский, драма'
    )

    add_book(books_list, war_and_piece)
    add_book(books_list, anna_karenina)
    add_book(books_list, idiot)
    add_book(books_list, crime_and_justice)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:

            results = search_books(books_list, search)
            return render_template('index.html', books=results, search=search)
        return render_template('index.html', books=books_list)

    app.run(port=9876, debug=True)


if __name__ == '__main__':
    main()