def fibonachi(max_value):
    first_elem = 0
    second_elem = 1
    while second_elem <= max_value:
        first_elem, second_elem = second_elem, first_elem + second_elem
        yield first_elem


def non_stop_numbers(count_of_numbers, max_value):
    number = 1
    for _ in range(count_of_numbers):
        yield number

        if number == max_value:
            number = 1
        else:
            number += 1


if __name__ == "__main__":
    max_value = input('Введите значение в ряду Фибоначи, '
                      'за которое мы не полезем в расчетах: ')

    try:
        max_value = int(max_value)
    except ValueError as e:
        print("Были введены некоректные данные, "
              "ставим по умолчанию 21.")
        max_value = 21

    for i in fibonachi(max_value):
        print(i)

    count_of_numbers = input('Задайте количество чисел '
                             'в циклической последовательности: ')

    max_value = input("Задайте максимальное значение числа в цикле: ")

    try:
        count_of_numbers = int(count_of_numbers)
        max_value = int(max_value)
    except ValueError as e:
        print("Были введены некоректные данные, "
              "ставим по умолчанию количество 12, а максимальное значение 3.")
        count_of_numbers = 12
        max_value = 3

    for i in non_stop_numbers(count_of_numbers, max_value):
        print(i)
