#! /usr/bin/python3.13
import logging

from searches import binary_search

logging.basicConfig(level=logging.INFO)


def get_element(_arr: list[int], index: int) -> int:
    """
    Характеристики алгоритмов O(1):
    - Время выполнения не зависит от размера входных данных
    - Выполняют фиксированное количество операций
    - Нет циклов, зависящих от размера входных данных
    - Часто используют заранее известные индексы или ключи
    :param _arr: Входящий массив
    :param index: Индекс элемента который нужно вернуть
    :return:
    """
    return _arr[index]


def get_length(_arr: list[int]) -> int:
    """
    O(1)
    :param _arr: Входящий массив
    :return: Длина массива
    """
    return len(_arr)


def sum_array(_arr: list[int]) -> int:
    """
    Демонстрация линейной сложности O(n)
    :param _arr: Входящий массив
    :return: Сумма элементов в массиве.
    """
    total = 0
    total_ops = 0
    for num in arr:
        total += num
        total_ops += 1
    logging.info(
        f"При линейной сложности количество операций равно размеру массива\n"
        f"над которым производятся действия. Размер массива {len(_arr)} Количество операций {total_ops}\n"
    )
    return total


# O(n^2)
def get_pairs(_arr: list[int]):
    """
    пример кода с временной сложностью O(n²) (квадратичная сложность)
    """
    total_ops = 0
    for i in range(len(_arr)):
        for j in range(len(_arr)):
            logging.debug(f"Вывод программы с квадратичной сложностью ({_arr[i]}, {_arr[j]})")
            total_ops += 1
    logging.info(f"Общее кол-во операций {total_ops} длина входящего массива {len(_arr)}")


# O(n³) - три вложенных цикла по n итераций каждый
def triple_nested_loop(_arr: list[int]) -> int:
    """
        Самый простой пример кубической сложности три вложенных цикла
    :param _arr:  Входящий массив
    :return: Количество операций с массивом
    """
    n = len(_arr)
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    logging.info(f"O(n^3) размер: {len(_arr)} кол-во операций: {count}")
    return count


arr = [1, 2, 3, 4]
big_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
value = get_element(_arr=arr, index=0)
logging.info(f"Результат выполнения кода где сложность O(1) {value}")
value = get_length(arr)
logging.info(f"Результат выполнения кода где сложность O(1) {value}")
get_pairs(arr)
sum_array(_arr=arr)
triple_nested_loop(_arr=arr)
# O(log n)
binary_search(_arr=arr, target=3)
binary_search(big_array, target=7)
binary_search(big_array, target=12)