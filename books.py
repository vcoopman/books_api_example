import hug
from db import init_db, get_db


# book = {
#     'msg': "this is a book"
# }

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

    with db:
        with db.cursor() as cur:
            sql = "SELECT * FROM book WHERE id = %s"
            cur.execute(sql, (book_id, ))
            result = cur.fetchone()

            if not result:
                return { 'msg': "Book not found" }

            print(result)
            # book = dict(zip(row.keys(), row))

            return { 'book' : dict(result) }