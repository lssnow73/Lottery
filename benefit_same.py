import os
import sqlite3
from db_past_winning_numbers import *


def benefit_same(diff_num=0):
    same_num = 0

    same_turns = set()

    file_name = 'past_winning_number.db'
    (conn, cursor) = db_open(file_name)

    records = db_load(cursor)

    for row in records:
        (turn, numbers) = row
        numbers_list = []
        for num in numbers.split(','):
            numbers_list.append(int(num.encode()))

        for next_row in records:
            (next_turn, next_numbers) = next_row
            next_numbers_list =[]

            if turn == next_turn:
                continue

            for next_num in next_numbers.split(','):
                next_numbers_list.append(int(next_num.encode()))

            same_num = set(numbers_list) - set(next_numbers_list)

            if len(same_num) <= diff_num:
                same_turn = sorted([int(turn),int(next_turn)])
                same_turns.add(tuple(same_turn))

    return records, list(same_turns)


def main():
    same_turns = []
    same_rounds = []

    records, same_turns = benefit_same(1)

    for turn in same_turns:
        (prev_turn, next_turn) = turn
        print turn, "\t", records[prev_turn-1]
        print "\t\t\t", records[next_turn-1]


if __name__ == '__main__':
    main()

