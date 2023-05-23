# Урок № 11. Функции

# Задание # 1


tmp = []
def fac(a):
    b = 1
    for i in range(1, a + 1):
        b = b * i
        tmp.insert(0, b)

fac(int(input("Введи число: ")))
print(tmp)


# Задание # 2


import collections
command = None

def create():
    last = collections.deque(pets, maxlen=1)[0]
    print("ID", last + 1)
    newpets = {
        last + 1:
            {
                input("Имя питомца: "): {
                    "Вид питомца": input("Вид питомца: "),
                    "Возраст питомца": int(input("возраст питомца: ")),
                    "Имя владельца": input("Имя владельца: ")
                },
            }
    }

    pets[last + 1] = newpets[last + 1]
    print("Питомец добавлен под ID:", last + 1)
    return

def read():
    nick = pets[int(command)].keys()
    nick = str(list(nick))[2:-2]  # кличка
    print(f"Это {pets[int(command)][nick]['Вид питомца']} "
          f"по кличке \"{nick}\".Возраст питомца:"
          f" {pets[int(command)][nick]['Возраст питомца']} "
          f"{get_suffix(pets[int(command)][nick]['Возраст питомца'])}. "
          f"Имя владельца: {pets[int(command)][nick]['Имя владельца']}")
    up = input("Хотите внести изменения?(y/n): ")
    if up == "y":
        updata()
    else:
        print("Ok")
    return

def updata():
    uppets = {
        int(command):
            {
                input("Имя питомца: "): {
                    "Вид питомца": input("Вид питомца: "),
                    "Возраст питомца": int(input("возраст питомца: ")),
                    "Имя владельца": input("Имя владельца: ")
                },
            }
    }
    pets[int(command)] = uppets[int(command)]
    print("Питомец изменен")
    return

def delete():
    pets.pop(int(input("Введите ID удаляемого питомца: ")))
    print("питомец удален из базы")

def get_pet():
    print("False")
    print("Питомца с таким ID в базе нет")
    a = input("Хотите добавить питомца?(y/n)?: ")
    if a == "y":
        create()
    else:
        print("Жаль")
    return

def get_suffix(age):
    nick = pets[int(command)].keys()
    nick = str(list(nick))[2:-2]
    age = int(pets[int(command)][nick]['Возраст питомца'])
    if age == 1 and age != 11:
        suf = "год"
    elif 2 <= age <= 4 or age <= 1:
        suf = "года"
    else:
        suf = "лет"
    return suf

def pets_list():
    for i in pets.items():
        print(i[0], i[1])

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 4,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "Желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}

while command != "stop":
    command = input("Введтие команду \"commands\" - для просмотра команд): ")
    if command == "commands":
        print(f"commands - выводит все команды;\n"
              f"id - для ввода ID питомца:\n"
              f"pets_list - выводит список всех питомцев:\n"
              f"create - добавить питомца\n"
              f"updata - изменить данные питомца\n"
              f"delete - удалить питомца\n"
              f"stop - завершение программы\n")

    if command == "create":
        create()
    if command == "updata":
        updata()
    if command == "delete":
        delete()
    if command == "pets_list":
        pets_list()
    if command == "id":
        while command != pets:
            command = int((input("введите ID питомца: ")))
            if command not in pets:
                get_pet()
            else:
                read()
                break




