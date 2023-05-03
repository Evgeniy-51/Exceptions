import parser as p
import file_writer as w

msg = '''
Введите через пробел в одну строку следующие данные:
Фамилия Имя Отчество дата_рождения номер_телефона пол
ПРИМЕР:
Иванов Иван Иванович  01.07.2000 4623464236 m
или Иван Иванович Иванов ...
Номер телефона - целое число от 6 до 12 символов
При вводе иностранных имен и отчеств, отсутствующих в
базе, корректная работа программы не гарантирована.
Данные можно вводить в произвольном порядке
'''
print(msg)
inp_str = input(">> ")

# inp_str1 = "  Иванов Сергей Иванович  11.07.2000 m 675342567524"
# inp_str2 = "  22.02.1997  Петр  сергеевич сидоров  m 623667734"
# inp_str3 = " f  12/11/1975  5827457423  Нина Павловна  Бубенкова"

def run():
    inp_lst = inp_str.split()
    if p.amount_data_validator(inp_lst):
        data = p.data_obj()
        p.create_sex(inp_lst, data)
        p.create_bday(inp_lst, data)
        p.create_phone(inp_lst, data)
        p.create_FIO(inp_lst, data)
        w.write_data(data)
