from random import sample
from data.vars import * 
from time import perf_counter
from utils import important_message
from utils import edit_text

data = {}

edit_text()
                               
def main ():
    """
    Функция, которая создаёт игру викторину.
    На каждой игровой сессии в терминал по очереди будут выведены вопросы с вариантами ответа, из которых необходимо выбрать правильный. Номер правильного ответа игрок необходимо вводить в терминал. При этом нужно уложиться в заданное время.
    Для каждой игровой сессии ведётся счёт. За правильный ответ в отведённое время начисляется максимум баллов. За правильный, но просроченный ответ начисляется меньшее количество баллов. За неправильный ответ начисляется ноль баллов.    
    """
    keys = []
    result = 0
    
    print(important_message('ИСТОРИЧЕСКАЯ БЛИЦ-ВИКТОРИНА'))
    print('''Приветствуем в викторине по истории!
Проверьте своё знание истории России с помощью интересных вопросов.
        
Все вопросы имеют варианты ответов, среди них только один верный. За отведённое время (20 с) вам необходимо ввести номер варианта после приглашения для ввода и нажать клавишу Enter.
    ''')
        
    for key, value in data.items():
        keys.append(key)        
    
    for q in sample(keys, N):
        answers = []

        for a in data[q].keys():
            answers.append(a)            
        
        answers = sample(answers, len(answers))

        print('\n' + q)
        print('\n'.join(f'  {i}. ' + a for i, a in enumerate(answers, 1)))
        
        while True:
            try:
                start = perf_counter()
                response = int(input(PROMPT))
                end = perf_counter()
                if 1 <= response <= len(answers):
                    break
                else:
                    raise ValueError   
            except ValueError:
                print(ERR_PREFIX + 'введите цифру номера ответа' + ERR_PREFIX[::-1])    
            
        time = end - start
        
        
        if not data[q][answers[response-1]]:
            print('Неверно...')    
        elif data[q][answers[response-1]] and TIMER < time:
            result += CORRECT_TIMEOUT
            print(f'Верно, но недостаточно быстро. ({round(time)} c)')
        else:
            print(f'Верно! ({round(time)} c)')
            result += CORRECT_TIME
        
    print(f'Ваш счёт: {result}') 

# >>> main()
# #======================================================================================================================#
# #                                                                                                                      #
# #                                             ИСТОРИЧЕСКАЯ БЛИЦ-ВИКТОРИНА                                              #
# #                                                                                                                      #
# #======================================================================================================================#
# 
# Приветствуем в викторине по истории!
# Проверьте своё знание истории России с помощью интересных вопросов.
# 
# Все вопросы имеют варианты ответов, среди них только один верный. За отведённое время (20 с) вам необходимо ввести номер варианта после приглашения для ввода и нажать клавишу Enter.
# 
# 
# Для игр с футболистами какой страны была в 1923 году впервые создана сборная РСФСР по футболу?
#   1.  Великобритания
#   2.  Швеция
#   3.  Германия
#   4.  Финляндия
#  > 4
# Верно! (13 c)
# 
# Как назвали первый в СССР металлокерамический твёрдый сплав?
#   1.  Опередит
#   2.  Сразит
#   3.  Осилит
#   4.  Победит
#  > d
# ! введите цифру номера ответа !
#  > d
# ! введите цифру номера ответа !
#  > d
# ! введите цифру номера ответа !
#  > 4
# Верно! (1 c)
# 
# При Иване Грозном была основана первая в России:
#   1.  Корабельная верфь
#   2.  Типография
#   3.  Гимназия
#   4.  Университет
#  > df
# ! введите цифру номера ответа !
#  > 545
# ! введите цифру номера ответа !
#  > df5
# ! введите цифру номера ответа !
#  > 4
# Неверно...
# 
# Какой из этих пассажирских самолётов был первым в СССР реактивным авиалайнером?
#   1.  Ан-24
#   2.  Ил-62
#   3.  Як-40
#   4.  Ту-104
#  > 4
# Верно, но недостаточно быстро. (28 c)
# 
# Изображение какого евангелиста украшало первую печатную русскую книгу?
#   1.  Марк
#   2.  Лука
#   3.  Иоанн
#   4.  Матфей
#  > 2
# Верно! (9 c)
# Ваш счёт: 70    
            