# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке. Если длины массивов
# не равны, необходимо как-то оповестить пользователя.

def diff_arrays(arr1, arr2):
    res_arr = []
    if len(arr1) != len(arr2):
        return "Lengths are different"
    else:
        for i in range(len(arr1)):
            res_arr.append(arr1[i] - arr2[i])
        return res_arr


arr1 = [3, 6, 7, 3, 7]
arr2 = [5, 6, 4, 7, 8]
print(diff_arrays(arr1, arr2))
