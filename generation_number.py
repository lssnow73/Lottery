import time
from random import sample
from get_probability_lottery_numbers import get_probability_lottery_numbers


START_NUMBER = 1
END_NUMBER = 45

MODE_RANDOM = 1
MODE_PROBABILITY = 2

DEFAULT_MAX_SEL_NUMBERS = 6


def get_lottery_number_set(get_number_mode=MODE_RANDOM, selected_numbers=DEFAULT_MAX_SEL_NUMBERS):

    lottery_number = set([])

    if get_number_mode == MODE_RANDOM:
        lottery_number = sample(range(START_NUMBER, END_NUMBER), DEFAULT_MAX_SEL_NUMBERS)

    else:
        lottery_number = get_probability_lottery_numbers(selected_numbers)

    return sorted(lottery_number)


def main():

    start_time = time.time()

    for repeat in range(1,999999):
        lottery_number = get_lottery_number_set(MODE_RANDOM, DEFAULT_MAX_SEL_NUMBERS)

    end_time = time.time()
    print end_time - start_time

if __name__ == '__main__':
    main()
