# -*- coding: utf-8 -*-
from time import sleep
from urllib2 import urlopen

RECENT_ROUND = 758
#RECENT_ROUND = 7


def get_page(url, url_variable):
    url_complete = url + str(url_variable)

    try:
        page = urlopen(url_complete)
        text = page.read().decode('cp949')

    except:
        page = urlopen(url_complete)
        text = page.read().decode('cp949')

    return text


def get_past_winning_number_info(text, url_variable):
    numbers = []
    number_info = []

    find_text = str(url_variable) + '회 당첨번호'
    find_text = find_text.decode('utf-8')
    start_pos = text.find(find_text)
    end_pos = text.find(u'1인당 당첨금액')

    number_info_str = text[start_pos:end_pos]
    number_info = number_info_str.split()

    return number_info


def get_past_winning_number_round(number_info):
    number_round = []
    swap_numbers = []
    number_round = number_info[2].split('+')
    numbers = number_round[0].split(',')

    for num in range(len(numbers)):
        swap_numbers.append(int(numbers[num]))

    return swap_numbers


def get_past_winning_numbers_from_web():
    numbers_array = {}
    fail_round = []
    fail_round2 = []

    for cnt in range(1, RECENT_ROUND+1):
        try:
            text = get_page('http://nlotto.co.kr/gameResult.do?method=byWin&drwNo=', cnt)
            number_info = get_past_winning_number_info(text, cnt)

            numbers = get_past_winning_number_round(number_info)
            numbers_array[cnt] = numbers
        except:
            try:
                text = get_page('http://nlotto.co.kr/gameResult.do?method=byWin&drwNo=', cnt)
                number_info = get_past_winning_number_info(text, cnt)

                numbers = get_past_winning_number_round(number_info)
                numbers_array[cnt] = numbers
            except IndexError:
                numbers_array[cnt] = [0,0,0,0,0,0]
                fail_round.append(cnt)

    sleep(1)

    for cnt in fail_round:
        try:
            text = get_page('http://nlotto.co.kr/gameResult.do?method=byWin&drwNo=', cnt)
            number_info = get_past_winning_number_info(text, cnt)
            numbers = get_past_winning_number_round(number_info)
            numbers_array[cnt] = numbers
        except:
            try:
                text = get_page('http://nlotto.co.kr/gameResult.do?method=byWin&drwNo=', cnt)
                number_info = get_past_winning_number_info(text, cnt)
                numbers = get_past_winning_number_round(number_info)
                numbers_array[cnt] = numbers
            except IndexError:
                numbers_array[cnt] = [0, 0, 0, 0, 0, 0]
                print 'Fail round:', str(cnt)

    sleep(1)

    for cnt in fail_round2:
        try:
            text = get_page('http://nlotto.co.kr/gameResult.do?method=byWin&drwNo=', cnt)
            number_info = get_past_winning_number_info(text, cnt)
            numbers = get_past_winning_number_round(number_info)
            numbers_array[cnt] = numbers
        except:
            try:
                text = get_page('http://nlotto.co.kr/gameResult.do?method=byWin&drwNo=', cnt)
                number_info = get_past_winning_number_info(text, cnt)
                numbers = get_past_winning_number_round(number_info)
                numbers_array[cnt] = numbers
            except IndexError:
                numbers_array[cnt] = [0, 0, 0, 0, 0, 0]
                print 'Fail round:', str(cnt)

    return numbers_array


def main():
    numbers_array = get_past_winning_numbers_from_web()
    for turn in numbers_array.keys():
        print turn,numbers_array[turn]


if __name__ == '__main__':
    main()
