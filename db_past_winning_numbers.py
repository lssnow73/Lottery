import os
import sqlite3
from get_past_winning_numbers import get_past_winning_numbers_from_web


def db_create(file_name):
    con = sqlite3.connect(file_name)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS TBLWinNumbers (
        turn VARCHAR(10),
        numbers VARCHAR(30))''')

    return con, cur


def db_open(file_name):
    con = sqlite3.connect(file_name)
    cur = con.cursor()

    return con, cur


def db_load(cursor):
    cursor.execute('SELECT * FROM TBLWinNumbers')
    records = cursor.fetchall()

    return records


def db_insert_all(cursor, numbers_array):
    for turn in sorted(numbers_array.keys()):
        str_numbers = str(numbers_array[turn])[1:-1]

        cursor.execute("INSERT INTO TBLWinNumbers VALUES (?, ?);", (turn, str_numbers))


def db_delete_for_entry(cursor):
    cursor.execute('DELETE FROM TBLWinNumbers')


def db_save(conn):
    conn.commit()


def main():
    numbers = []
    file_name = 'past_winning_number.db'
    numbers_array = get_past_winning_numbers_from_web()

    if os.path.isfile(file_name):
        (conn, cursor) = db_open(file_name)
    else:
        (conn, cursor) = db_create(file_name)

    db_delete_for_entry(cursor)
    db_insert_all(cursor, numbers_array)
    db_save(conn)

    records = db_load(cursor)

    for row in records:
        (turn,numbers) = row
        print turn, numbers


if __name__ == '__main__':
    main()
