# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

def divide(a, b):
    return a / b


def concat(a, b):
    return a + b


def file_writer(url):
    file = open(url)
    file.write('#hello')


# print(divide(3, 0))
# print(concat(2, '5'))
file_writer("task2.txt")
