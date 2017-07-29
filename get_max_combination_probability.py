
def max_combination_probability(max_number=45, max_number_select=6):
    end_number = max_number+1
    max_number_list = range(1, max_number+1)
    effect_number_list = max_number_list[(max_number-max_number_select):]
    max_number_select_list = range(1, max_number_select+1)

    fact = 1
    div = 1
    for num in effect_number_list:
        fact = fact * num
    for num in max_number_select_list:
        div = div * num

    max_combination = fact / div

    return max_combination


def main():
    max_combination = max_combination_probability()
    print max_combination


if __name__ == '__main__':
    main()