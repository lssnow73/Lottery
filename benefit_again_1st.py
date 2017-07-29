import os
import sqlite3
from db_past_winning_numbers import *

UNIT_INT = 50


def benefit_again_1st():
    same_num = 0
    same_turn = []
    each_numbers = {}

    file_name = 'past_winning_number.db'
    (conn, cursor) = db_open(file_name)

    records = db_load(cursor)

    print records[0], records[1]

    for i in range(0, 45+1):
        each_numbers[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for row in range(len(records)):
        numbers_list = []
        next_numbers_list = []
        (turn, numbers) = records[row]
        (next_turn, next_numbers) = records[row + 1]

        for num in numbers.split(','):
            numbers_list.append(int(num.encode()))

        for next_num in next_numbers.split(','):
            next_numbers_list.append(int(next_num.encode()))

            same_num = set(numbers_list) - set(next_numbers_list)

            if len(same_num) <= 1:
                same_turn.append((int(turn),int(next_turn)))


    for row in records:
        (turn,numbers) = row
        unit = int(int(turn)/UNIT_INT)
        for num in numbers.split(','):
            key = int(num.encode())
            each_numbers[key][unit] = int(each_numbers[key][unit]) + 1

    return unit,each_numbers

def main():
    same_turns = []
    same_rounds = []

    same_turns = benefit_again_1st()

    for same in same_turns:
        for next_same in same_turns:
            pass
        pass

    print same_turns


if __name__ == '__main__':
    main()
