#Homework 1
def chisl(a):
    if a == 0:
        return 1
    return chisl(a-1) * a
b = int(input())
for i in range(b, 0, -1):
    print(chisl(i))

#Homework 2
pets = {
    1: {
        'Мухтар': {
                'Вид питомца': 'Собака',
                'Возраст питомца': 9,
                'Имя владельца': 'Павел'
            },
        },
    2: {
        'Каа': {
                'Вид питомца': 'желторотый питон',
                'Возраст питомца': 19,
                'Имя владельца': 'Саша'
            },
        },
}

def get_suffix(age):
    if age == 1:
        return 'год'
    elif age > 1 and age < 5:
        return 'года'
    else:
        return 'лет'

def create():
    print('Команда "Добавить"')
    key = input('Кличка питомца:')
    fields = ['Вид питомца', 'Возраст питомца', 'Имя владельца']
    temp = {key: dict()}
    for field in fields:
        res = input(f'{field}:')
        if type(res) == int:
            temp[key][field] = int(res)
        else:
            print('Введите возраст числом.')
    last = max(pets.keys())
    pets[last + 1] = temp

def read():
    print('Команда "Информация"')
    ID = int(input('Введите ID: '))
    pet = get_pet(ID)
    if not pet:
        print(f'Нет питомца с таким ID: {ID}')
        return
    key = [x for x in pet.keys()][0]
    result = f'Это {pet[key]["Вид питомца"]} по кличке "{key}".'\
             f'Возраст питомца: {pet[key]["Возраст питомца"]}{get_suffix(pet[key]["Возраст питомца"])}'\
             f'Имя владельца: {pet[key]['Имя владельца']}'
    print(result)

def update():
    print('Команда "Обновить данные"')
    ID = int(input('Введите ID:'))
    pet = get_pet(ID)
    if not pet:
        print(f'Нет питомца с таким ID:{ID}')
        return
    key1 = [x for x in pet.keys()[0]]
    print('Введите данные')
    temp = dict()
    for key in pet[key1].items():
        res = input(f'{key}')
        if res:
            temp[key] = int(res) if res.isnumeric() else res
            pet[key1].update(temp)

def delete():
    print('Команда "Удалить"')
    ID = int(input('Введите ID:'))
    pets.pop(ID, None)

def get_pet(ID):
    return pets.get(ID, None)

def pets_list():
    for key, val in pets.items():
        print(f'ID:{key}', val)
        commands = {
            'create': create,
            'read': read,
            'update': update,
            'delete': delete,
            'list': pets_list,
            'stop': 0
        }

        def print_commands():
            print('Доступные команды:')
            for key in commands:
                print('->', key)

        while True:
            print_commands()
            command = input('Введите команду:')
            if command not in commands.key():
                continue
            if command == 'stop':
                break
            commands[command]()
            input('Продолжить')