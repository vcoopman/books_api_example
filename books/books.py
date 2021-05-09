import hug
from db import init_db, get_db

@hug.startup()
def start_api(api):
    ''' initial api process'''

    init_db()


@hug.get('/books/{book_id}')
def get_book(
        book_id: hug.types.number
    ):
    '''Gets book information'''

    db = get_db()

    with db:
        with db.cursor() as cur:
            sql = "SELECT * FROM book WHERE id = %s"
            cur.execute(sql, (book_id, ))
            result = cur.fetchone()

            if not result:
                return { 'msg': "Book not found" }

            return { 'book' : dict(result) }
