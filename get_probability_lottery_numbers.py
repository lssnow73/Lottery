from random import sample


def get_probability_lottery_numbers(select_numbers=6):
    lottery_number = sample(range(1, 45), 6)

    return lottery_number


def main():
    lottery_number = get_probability_lottery_numbers()

    print sorted(lottery_number)


if __name__ == '__main__':
    main()
