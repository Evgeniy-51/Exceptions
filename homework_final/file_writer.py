from errors import *


def isExisting(filename: str, note: str) -> bool:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line == note:
                    return True
            return False
    except FileNotFoundError as e:
        print(f"{e}  Ошибка открытия файла")


def write_data(data):
    filename = f"./res_folder/{data.surname}.txt"
    note = f"{data.surname.capitalize()} {data.name.capitalize()} {data.patronymic.capitalize()} {data.birthday} {data.phone} {data.sex}\n"
    try:
        with open(filename, "a+", encoding='utf-8') as file:
            if not isExisting(filename, note):
                file.write(note)
                print("Запись успешно добавлена!")
            else:
                raise ExistingEntry()
    except FileNotFoundError as e:
        print(f"{e}  Ошибка открытия файла")
    except ExistingEntry:
        print(f"Такая запись уже существует")
