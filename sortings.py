#! /usr/bin/python3.13
import logging

logging.basicConfig(level=logging.INFO)
unsorted_array = [3, 2, 9, 5, 4, 7, 22, 44, 6, 1, 0]


def selection_sort(_array: list[int]) -> tuple[int, ...]:
    """
        Сложность: O(n²) в любом случае.
    :param _array: Входящий массив
    :return: отсортированный массив
    """
    _array = _array.copy()
    n = len(_array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if _array[min_idx] > _array[j]:
                min_idx = j
        _array[i], _array[min_idx] = _array[min_idx], _array[i]
    return tuple(_array)


def bubble_sort(_array: list[int]) -> tuple[int, ...]:
    """
    В худшем случае: O(n²)
    В лучшем случае (уже отсортирован): O(n) с оптимизацией
    :param _array: Входящий массив
    :return: Отсортированный массив
    """
    _array = _array.copy()
    n = len(_array)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if _array[j] > _array[j + 1]:
                _array[j], _array[j + 1] = _array[j + 1], _array[j]
                swapped = True
        if not swapped:
            break
    return tuple(_array)


def quick_sort(_array: list[int]) -> list[int]:
    """
    Средняя сложность: O(n log n)
    Худший случай (уже отсортирован, плохой выбор pivot): O(n²)
    Память: O(log n) для рекурсии (в in-place версии)
    Нестабильная сортировка
    :param _array: Входящий массив
    :return: Отсортированный список
    """
    _array = _array.copy()
    if len(_array) <= 1:
        return _array

    pivot = _array[len(_array) // 2]
    left = [x for x in _array if x < pivot]
    middle = [x for x in _array if x == pivot]
    right = [x for x in _array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    logging.info(f"Selection sort: {selection_sort(unsorted_array)} оригинал {unsorted_array}")
    logging.info(f"Bubble sort: {bubble_sort(unsorted_array)} оригинал {unsorted_array}")
    logging.info(f"Quick sort: {quick_sort(unsorted_array)} оригинал {unsorted_array}")
