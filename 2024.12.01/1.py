from datetime import date, timedelta

vacations = [(date(2023, 5, 1), timedelta(weeks=1)), (date(2023, 7, 17), timedelta(weeks=1))]

def non_working_days(date: date) -> bool:
    """  
    Функция, которая работает с глобальной переменной "vacations" и определяет является ли аргумент функции выходным днём.
    """
    vacation_ranges = [(start, start + delta) for start, delta in vacations]

    return any(start <= date <= end for start, end in vacation_ranges)    
    
def schedule(start_date: date, weekday: int, /, *weekdays: int, total_days: int, form='%d/%m/%Y') -> list[str]:
    """
    Функция генерирует график проведения мероприятий по заданным условиям.
    Функция принимает дату первого мероприятия в графике, обязательным аргументом один и более номеров дней недели, далее обязательным аргументом общее количество занятий, и необязательным аргументом формат строкового представления генерируемых дат. 
    Функция возвращает список строковых представлений дат в заданном формате.
    """
    timetable = []
    next_date = start_date

    if not weekdays:
        while len(timetable) < total_days:
            if next_date.isoweekday()  == weekday and not non_working_days(next_date):
                timetable.append(next_date.strftime(form))
            next_date += timedelta(days=1)
    else:
        while len(timetable) < total_days:
            if next_date.isoweekday() in (weekday, *weekdays) and not non_working_days(next_date):
                timetable.append(next_date.strftime(form))
            next_date += timedelta(days=1)

    return timetable
    
# >>> vacations = [(date(2023, 5, 1), timedelta(weeks=1)), (date(2023, 7, 17), timedelta(weeks=1))]
# >>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
# >>> len(py321)
# 70
# >>> py321[28:32]
# ['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']    
               