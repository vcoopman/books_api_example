import pymysql

def get_db():
    ''' creates db connection '''

    db = pymysql.connect(user='root',
                         password='root',
                         host='db',
                         database='books_service',
                         cursorclass=pymysql.cursors.DictCursor
                        )
    return db

def init_db():
    ''' initializes the db '''

    # read sql file
    sql_file = open('schema.sql', 'r').read()

    # get commands from file
    sql_commands = sql_file.split(';')

    db = get_db()
    cur = db.cursor()

    # execute each command
    for command in sql_commands:
        if command.strip() != '':
            cur.execute(command)

    db.commit()
