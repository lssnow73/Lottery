from db_past_winning_numbers import *
from get_probability_each_number import *


def main():
    unit = 0

    unit, each_numbers = get_probability_each_number()
    for num in each_numbers.keys():
        print num,
        for i in range(0, unit):
            print "\t%-d  "%(each_numbers[num][i] - int(UNIT_INT/10)),
        print ""


if __name__ == '__main__':
    main()
