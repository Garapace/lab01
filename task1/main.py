from random import randint

""" Лаба 1. Git, Python. Реализовать алгоритм Евклида.
Алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел """


def euclid_algorithm(num1, num2):
    if num1 == 0 or num2 == 0:
        return max(num1, num2)
    else:
        if num1 > num2:
            return euclid_algorithm(num1 - num2, num2)
        else:
            return euclid_algorithm(num1, num2 - num1)


def main():
    start = input("нужно ввести два числа для работы алгоритма.\n1 - использовать генератор | 2 - ввести самому\n")
    while start != "1" and start != "2":
        start = input("целое число броуу, 1 или 2\n1 - использовать генератор | 2 - ввести самому\n")

    if start == "1":
        num1 = randint(0, 1000)
        num2 = randint(0, 1000)
    else:
        num1 = int(input("введите первое число\n"))
        num2 = int(input("введите второе число\n"))

    print(f"НОД для чисел {num1} и {num2}\t-\t{euclid_algorithm(num1, num2)}")


if __name__ == "__main__":
    main()
