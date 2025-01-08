from pathlib import Path
from random import randrange, choice 
from typing import Literal
from datetime import date, timedelta
from pprint import pprint

names = {}

def load_data () -> None:
    """
    Функция, которая читает из файлов данные и упорядочивает их.
    """
    names['имя'] = []
    names['имя_м'] = []
    names['отчество_м'] = []
    names['отчество'] = []
    names['фамилия_м'] = []
    names['фамилия'] = [] 
    
    names_dir = Path(r'C:\Users\79526\Galeev\2024.12.14\data\names')
    female_names = Path(names_dir / 'женские_имена.txt')
    male_names_patronymics = Path(names_dir / 'мужские_имена_отчества.txt') 
    surnames = Path(names_dir / 'фамилии.txt')
    
    with open(female_names, encoding='utf-8') as filein:
        female_names = filein.readlines()
    
    for el in female_names:
        names['имя'].append(el.strip('\n'))
        
    with open(male_names_patronymics, encoding='utf-8') as filein:
       male_names_patronymics = filein.readlines()
    
    for el in male_names_patronymics:
        l = el.split()
        if len(l) == 3:        
            names['имя_м'].append(l[0]) 
            names['отчество_м'].append(l[1].strip('(,'))
            names['отчество'].append(l[2].strip(')\n')) 
        else:
            names['имя_м'].append(l[0].strip(','))
            names['имя_м'].append(l[1].strip())
            names['отчество_м'].append(l[2].strip('(,'))
            names['отчество'].append(l[3].strip(')\n'))
            
    with open(surnames, encoding='utf-8') as filein:
       surnames = filein.readlines()
    
    for el in surnames:
        l = el.split(', ')
        if len(l) == 2:
            names['фамилия_м'].append(l[0])
            names['фамилия'].append(l[1].strip('\n'))
        else:
            l = l[0].strip('\n')
            names['фамилия_м'].append(l) 
            names['фамилия'] .append(l)
            
            
def generate_person () -> dict[
    'имя': str,
    'отчество': str,
    'фамилия': str,
    'пол': Literal['мужской', 'женский'],
    'дата рождения': date,
    'мобильный': str
    ]:
    """
    Функция, которая генерирует анкету человека со случайными данными.
    
    Условия генерации случайных данных:
    
        Имя, отчество и фамилия должны быть согласованы по полу человека.
    
        При генерации случайной даты рождения необходимо учитывать количество дней в каждом месяце с учётом високосного года.
    
        Для генерации года рождения используйте в качестве диапазона одно столетие.
    
        Формат мобильного номера +79xxxxxxxxx.
    """    
    gender = choice(['мужской', 'женский'])    
    form = {} 
    birthday = date(1900, 1, 1) + timedelta(days=randrange(36524))
    if gender == 'мужской':
        form['имя'] = choice(names['имя_м'])
        form['отчество'] = choice(names['отчество_м'])
        form['фамилия'] = choice(names['фамилия_м'])
        form['пол'] = gender
        form['дата рождения'] = birthday
        form['мобильный'] = '+7' + str(randrange(9000000000, 10000000000))
    else:
        form['имя'] = choice(names['имя'])
        form['отчество'] = choice(names['отчество'])
        form['фамилия'] = choice(names['фамилия'])
        form['пол'] = gender
        form['дата рождения'] = birthday
        form['мобильный'] = '+7' + str(randrange(9000000000, 10000000000))
    


# >>> load_data()
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Савватий',
#  'отчество': 'Парамонович',
#  'фамилия': 'Доронин',
#  'пол': 'мужской',
#  'дата рождения': datetime.date(1911, 12, 31),
#  'мобильный': '+79340517833'}
# >>>
# >>> pprint(generate_person(), sort_dicts=False)
# {'имя': 'Лаура',
#  'отчество': 'Ксенофонтовна',
#  'фамилия': 'Доманская',
#  'пол': 'женский',
#  'дата рождения': datetime.date(1931, 6, 10),
#  'мобильный': '+79080776976'}