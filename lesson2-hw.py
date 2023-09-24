# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи


# 2) протипізувати перше завдання
# from typing import Callable
# def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:

def notebook():
    todo_list: list[str] = []

    def add_todo(todo:str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all

add, all_todo = notebook()

add('do homework')
add('donate')


print(all_todo())

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    row = str(num)
    length = len(row) - 1
    res = []
    for i, ch in enumerate(row):
        if ch != '0':
            res.append(ch + '0' * (length - i))

    return ' + '.join(res) + f' = {row}'
#   return ' + '.join(ch + '0' * (len(str(num)) - 1 - i) for i, ch in enumerate(str(num)) if ch != '0') + f' = {num}'


print(expanded_form(5346))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'{count=}')
        func(*args, **kwargs)
        print('-' * 20)

    return inner

@decor
def func1():
    print('funct1')

@decor
def func2():
    print('funct2')

func1()
func2()
func1()