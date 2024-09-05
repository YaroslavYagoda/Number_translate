"""
Напишите программу, которая принимает на ввод целое число в диапазоне
от 1 до 5, и выводит соответствующее ему слово на английском языке.
"""
dict_sootvetstviya = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
}

answer_user = input('Введите число от 1 до 5: ')
answer_system = dict_sootvetstviya.setdefault(answer_user, 'не найдено!')

print(f'Соответствующее слово: {answer_system}')
