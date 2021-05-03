import hug
from db import init_db, get_db

@hug.startup()
def start_api(api):
    ''' initial api process'''

    try:
        init_db()

    except Exception:
        print("Error start_api")
        raise


@hug.get('/books/{book_id}')
def get_book(
        book_id: hug.types.number
    ):
    '''Gets book information'''

    db = get_db()
    row = db.execute(
        "SELECT * FROM book WHERE id = ?",
        (book_id, )
    ).fetchone()

    if not row:
        return { 'msg': "Book not found" }

    book = dict(zip(row.keys(), row))
    return { 'book' : book }
