import os
import sqlite3
from get_past_winning_numbers import get_past_winning_numbers_from_web
from db_past_winning_numbers import *

UNIT_INT = 50


def get_probability_each_number():
    unit = 0
    numbers = []
    each_numbers = {}

    file_name = 'past_winning_number.db'

    if os.path.isfile(file_name):
        (conn, cursor) = db_open(file_name)
    else:
        numbers_array = get_past_winning_numbers_from_web()
        (conn, cursor) = db_create(file_name)
        db_delete_for_entry(cursor)
        db_insert_all(cursor, numbers_array)
        db_save(conn)

    records = db_load(cursor)

    for i in range(0, 45+1):
        each_numbers[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for row in records:
        (turn,numbers) = row
        unit = int(int(turn)/UNIT_INT)
        for num in numbers.split(','):
            key = int(num.encode())
            each_numbers[key][unit] = int(each_numbers[key][unit]) + 1

    return unit,each_numbers


def main():
    unit = 0

    unit,each_numbers = get_probability_each_number()

    for num in each_numbers.keys():
        print num,
        for i in range(0, unit):
            print "\t%-d  "%(each_numbers[num][i] - int(UNIT_INT/10)),
        print ""


if __name__ == '__main__':
    main()
