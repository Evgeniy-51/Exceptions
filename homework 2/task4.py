# Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. 
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

class EmptyString(Exception):
    pass

def inp_data():
    while True:
        try:
            data = input("Ввод данных: ")
            if not data:
                raise EmptyString()
        except EmptyString:
            print("Строка не должна быть пустой!")

inp_data()
