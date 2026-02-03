import logging


def binary_search(_arr: list[int], target: int) -> int:
    """
    Бинарный поиск в отсортированном массиве.
    Сложность: O(log n)
    :param _arr: Входящий массив
    :param target: искомое значение
    :return: Индекс найденного элемента
    """
    total_ops = 0
    left, right = 0, len(_arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if _arr[mid] == target:
            total_ops += 1
            logging.info(f"Кол-во операций: {total_ops} размер массива {len(_arr)}")
            return mid
        elif _arr[mid] < target:
            total_ops += 1
            left = mid + 1
        else:
            total_ops += 1
            right = mid - 1
    logging.info(f"Кол-во операций: {total_ops} размер массива {len(_arr)} цель не найдена")
    return -1
