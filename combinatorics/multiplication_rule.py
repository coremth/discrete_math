"""
Правило произведения
Если первое действие можно выполнить m способами,
а второе — n способами, то вместе их можно выполнить m * n  способами.

Задача
Сколько уникальных паролей можно составить из 5 символов,
где каждый символ — это заглавная буква английского алфавита (26 букв),
и повторения разрешены?
"""


def calc_pwd_options(space_of_options_length: int, alphabet_size: int) -> int:
    pwd_options = alphabet_size**space_of_options_length
    return pwd_options


space_of_options_length = 5
alphabet_size = 26

print(calc_pwd_options(space_of_options_length, alphabet_size))


"""
Задача
Напиши программу, которая перебирает и выводит все возможные комбинации пароля
из 2 цифр (от 0 до 9). В конце выведи их количество.
"""


def print_pwd_options(alphabet_size: int) -> None:
    counter = 0
    for i in range(0, alphabet_size):
        for j in range(0, alphabet_size):
            counter += 1
            print(f"{i} - {j}")

    print(counter)


alphabet_size = 10

print_pwd_options(alphabet_size)


"""
Вариант выше является сильно захардкоженым и подходит только в том случае,
если символов в пароле всего два. Если мы не знаем количество вложенных циклов изначально
(а для каждого нового символа в пароле потребуется новый вложенный цикл), можно
использовать рекурсию. Рекурсия — это когда функция вызывает саму себя.
В каждой рекурсии должен быть предусмотрен базовый случай (на котором она останавливается).
"""


def calc_pwd_options_rec(current: str, length: int, alphabet_size: int) -> int:
    if len(current) == length:
        return 1
    count = 0
    for i in range(alphabet_size):
        count += calc_pwd_options_rec(current + str(i), length, alphabet_size)
    return count


current = ""
length = 3
alphabet_size = 10
print(calc_pwd_options_rec(current, length, alphabet_size))
