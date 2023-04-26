# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке. Если длины массивов
# не равны, необходимо как-то оповестить пользователя. Важно: При выполнении метода единственное исключение,
# которое пользователь может увидеть - RuntimeException, т.е. ваше.

class RuntimeException(Exception):
    def __init__(self, msg=None):
        self.message = msg if msg else "Unknown error"

    def __str__(self):
        return self.message


class DiffLengths(Exception):
    pass

class ZeroDivision(Exception):
    pass


def diff_arrays(arr1, arr2):
    res_arr = []
    try:
        if len(arr1) != len(arr2):
            raise DiffLengths()
        else:
            for i in range(len(arr1)):
                if arr2[i] == 0:
                    raise ZeroDivision()
                res_arr.append(arr1[i] / arr2[i])
        return res_arr
    except DiffLengths:
        raise RuntimeException("Lengths are different")
    except ZeroDivision:
        raise RuntimeException("Division by zero")
    except:
        raise RuntimeException()


arr1 = [3, 6, 7, 3, 7]
arr2 = [5, 6, 4, 2, 8]
print(diff_arrays(arr1, arr2))
