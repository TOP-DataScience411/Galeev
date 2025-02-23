from re import compile, VERBOSE, MULTILINE
from sys import path
from pathlib import Path


months = (
    'январ[ья]',
    'феврал[ья]',
    'марта*',
    'апрел[ья]',
    'ма[йя]',
    'июн[ья]',
    'июл[ья]',
    'августа*',
    'сентябр[ья]',
    'октябр[ья]',
    'ноябр[ья]',
    'декабр[ья]',
)

with open(Path(path[0])/'history_dates_ed.txt', encoding='utf-8') as filein:
    data = filein.read()
    

pattern1 = compile(r'''^(?P<date>
  (?:
    # Вариант 1. Дата с названием месяца (и опционально с днём, а также с диапазоном месяцев)
    (?:(?P<day>\d{1,2})\s+)?(?P<month>f'{'|'.join(months)}')
    (?:\s*[–-]\s*(?:(?P<day2>\d{1,2})\s+)?(?P<month2>f'{'|'.join(months)}'))?
    \s+(?P<year>\d{4})
    (?:\s*гг?\.?)?
  |
    # Вариант 2. Годовой диапазон без указания месяцев
    (?P<year1>\d{4})\s*[–-]\s*(?P<year2>\d{4})(?:\s*гг?\.?)?
  |
    # Вариант 3. Только год
    (?P<year_only>\d{4})(?:\s*гг?\.?)?
  )
)''',
     VERBOSE | MULTILINE)

res = pattern1.findall(data)

# >>> res[0][0]
# '1801–1825 гг.'
# >>> res[10][0]
# '1824 г.'
# >>> res[25][0]
# '1866 г.'