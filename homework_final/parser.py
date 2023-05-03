from errors import *
import re
import datetime
import pickle


class data_obj():
    def __init__(self):
        self.name = None
        self.patronymic = None
        self.surname = None
        self.sex = None
        self.phone = None
        self.birthday = None


def amount_data_validator(data: list) -> bool:
    try:
        if len(data) > 6:
            raise OverData()
        if len(data) < 6:
            raise NotEnoughData
    except OverData:
        raise RuntimeException("Ошибка: присутствуют лишние поля")
    except NotEnoughData:
        raise RuntimeException("Ошибка: введите все необходимые данные")
    return True


def create_sex(inp: list, out: data_obj):
    try:
        isValid = False
        for index, item in enumerate(inp):
            if item in ("m", "f"):
                out.sex = item
                inp.pop(index)
                isValid = True
                break
        if not isValid:
            raise InvalidData
    except InvalidData:
        raise RuntimeException("Недостаточно данных: отсутствует информация 'пол'")


def create_bday(inp: list, out: data_obj):
    try:
        isValid = False
        pattern = "(\d{2}(?:\.|\/)){2}\d{4}"
        for index, item in enumerate(inp):
            if re.fullmatch(pattern, item):
                if 1900 < int(item[-4:]) <= datetime.datetime.now().year:
                    out.birthday = item.replace("/", ".")
                    inp.pop(index)
                    isValid = True
                    break
                else:
                    raise InvalidYear
        if not isValid:
            raise InvalidData
    except InvalidData:
        raise RuntimeException("Недостаточно данных: отсутствует информация 'дата'")
    except InvalidYear:
        raise RuntimeException("Ошибка: Неправильно указан год")


def create_phone(inp: list, out: data_obj):
    try:
        isValid = False
        pattern = "\\b\d{6,12}\\b"
        for index, item in enumerate(inp):
            if re.fullmatch(pattern, item):
                out.phone = item
                inp.pop(index)
                isValid = True
                break
        if not isValid:
            raise InvalidPhoneNumber
    except InvalidPhoneNumber:
        raise RuntimeException("Недостаточно данных: отсутствует номер телефона")


def get_namelist() -> list:
    try:
        with open("names.bin", "rb") as file:
            return pickle.load(file)
    except IOError:
        raise RuntimeException("Ошибка получения данных из файла names.bin")


def get_patronymic() -> list:
    try:
        with open("patronymic.bin", "rb") as file:
            return pickle.load(file)
    except IOError:
        raise RuntimeException("Ошибка получения данных из файла patronymic.bin")


def create_FIO(inp: list, out: data_obj):
    namelist = get_namelist()
    patronymic = get_patronymic()
    inp = [x.lower() for x in inp]

    for index, elem in enumerate(inp):
        if out.name is None:
            for name in namelist:
                if elem == name:
                    out.name = elem
                    break
        if out.patronymic is None:
            for patr in patronymic:
                if elem == patr:
                    out.patronymic = elem
                    break
        if index == 0 and out.name is None and out.patronymic is None:
            out.surname = elem
        elif index == 1 and out.name is None and out.patronymic is None:
            out.patronymic = elem
        elif index == 2 and out.name is None:
            out.name = elem
        elif index == 2 and out.surname is None:
            out.surname = elem
