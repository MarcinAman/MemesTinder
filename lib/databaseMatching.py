import sqlite3
from sqlite3 import Error


def add_meme_to_db(db_file, meme_src, meme_alt):
    conn = create_connection(db_file)
    exec_tuple = (meme_src, meme_alt)
    conn.execute('INSERT INTO Memes VALUES (NULL,?,?)', exec_tuple)

    conn.commit()
    conn.close()


def add_user_to_db(db_file, user_name, user_surname):
    conn = create_connection(db_file)
    exec_tuple = (user_name, user_surname)
    conn.execute('INSERT INTO Viewiers VALUES (NULL,?,?)', exec_tuple)

    conn.commit()
    conn.close()


# noinspection SqlNoDataSourceInspection
def add_to_database(viewer_id, meme_src, preference,db_file):
    conn = create_connection(db_file)

    meme_tuple = (meme_src,)
    meme_cursor = conn.execute('Select MemeID from Memes where Source like (?)', meme_tuple)

    meme_cursor_head = meme_cursor.fetchone()[0]

    conn.execute('INSERT INTO Views VALUES (NULL,?,?,?)',
                 (preference, viewer_id, meme_cursor_head))

    conn.commit()
    conn.close()


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def create_database(db_name):
    file = open('config.sql', 'r')
    sqlFile = file.read()
    file.close()

    sqlCommands = sqlFile.split(";")

    conn = create_connection(db_name)
    for command in sqlCommands:
        try:
            conn.execute(command)
        except Error as e:
            pass

    conn.commit()
    conn.close()
