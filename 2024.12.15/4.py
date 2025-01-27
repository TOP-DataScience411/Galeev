from pathlib import Path
from csv import reader, writer

class CountableNouns:
    """
    Класс, который предоставляет интерфейс для работы с файловой базой существительных.
    """
    db_path: Path = Path(r'C:\Users\79526\Galeev\2024.12.15\words.csv')
    words: dict[str, tuple[str, str]] = {} # соответствие между существительным в единственном числе и кортежем из двух словоформ/слов во множественном числе, согласующихся с числительными "два" и "пять"
    with open(db_path, newline='') as csvfile:
        nouns = reader(csvfile, lineterminator='\n')
        for row in nouns:
            words[row[0]] = (row[1], row[2])
            
    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """
        Функция, которая принимает в качестве аргументов число и существительное для согласования в единственном числе, возвращает согласованное с переданным числом существительное.
        """
        cnt_nouns = cls.words.get(word)
        if not cnt_nouns:
            cls.save_words(word)
        else:
            last_two_digits = number % 100 
            last_digit = number % 10  
            if (
                   11 <= last_two_digits <= 19 
                or last_digit == 0 
                or 5 <= last_digit <= 9
            ):
                return cnt_nouns[1]  
            elif 2 <= last_digit <= 4:
                return cnt_nouns[0]  
            elif last_digit == 1:
                return word
            
    @classmethod        
    def save_words(cls, word1: str = None) -> None:
        """
        Функция, которая запрашивает в stdin у пользователя два или три слова согласующихся с числительными, добавляет полученные значения в поле класса words и дописывает их в файл с базой существительных.
        """
        if word1:
            print(f'существительное "{word1}" отсутствует в базе')
            word2 = input('  введите слово, согласующееся с числительным "два":')
            word3 = input('  введите слово, согласующееся с числительным "пять":')
        else:
            word1 = input('  введите слово, согласующееся с числительным "один":')
            word2 = input('  введите слово, согласующееся с числительным "два":')
            word3 = input('  введите слово, согласующееся с числительным "пять":')
        cls.words.setdefault(word1, (word2, word3))    
        
            
        with open(cls.db_path, 'a', newline='') as csvfile:
            nouns = writer(csvfile) 
            nouns.writerow([word1, word2, word3]) 

# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(22, 'год')
# 'года'
# >>> CountableNouns.pick(365, 'день')
# 'дней'
# >>> CountableNouns.pick(21, 'попугай')
#   введите слово, согласующееся с числительным "два":попугая
#   введите слово, согласующееся с числительным "пять":попугаев
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
# >>> CountableNouns.save_words()
#   введите слово, согласующееся с числительным "один":капля
#   введите слово, согласующееся с числительным "два":капли
#   введите слово, согласующееся с числительным "пять":капель
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# попугай,попугая,попугаев
# капля,капли,капель            