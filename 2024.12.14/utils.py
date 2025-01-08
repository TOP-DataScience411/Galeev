from shutil import copy2, get_terminal_size
from pathlib import Path

def load_file (file_path: Path) -> Path:
    """
    Функция, которая осуществляет копирование файла по переданному пути в основной каталог
    """
    path = Path(r'C:\Users\79526\Galeev\2024.12.14')
    copy2(file_path, path)
    
    return path / file_path.name
    
def edit_text ():
    """
    Функция, которая читает из файлов данные и упорядочивает их. 
    """
    question = ''
    
    with open(r'C:\Users\79526\Galeev\2024.12.14\data\questions.quiz', encoding='utf-8') as file:
        for line in file:
            if not line[0].isdecimal() and line != '\n':
                question = line.strip()                
                data[question] = {}
            elif line != '\n':
                answer = line.strip('1234.')
                data[question].setdefault(answer.rstrip('\n+'), answer.endswith('+\n'))    
 

def important_message(text: str) -> str:
    """
    Задача этой функции — сгенерировать строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'. 
        Ширина рамки определяется текущей шириной окна терминала. 
        Пустое пространство внутри рамки заполняется пробелами. 
        Между верхней границей рамки и первой строчкой текста должен быть отступ одна строчка. 
        Между последней строчкой текста и нижней границей рамки должен быть отступ одна строчка. 
        Текст внутри рамки выравнивается по центру.
        Между боковыми границами рамки и текстом должен быть минимальный отступ два пробела.
    """
    columns = get_terminal_size().columns - 2
    
    border = '#' + '=' * columns + '#\n'
    space_line = '#' + ' ' * columns + '#\n'
    
    result = border + space_line

    words = text.split()
    
    current_line = ''
    
    for word in words:
        if len(current_line) + len(word) + 1 <= columns:
            current_line += (' ' if current_line else '') + word
        else:
            result += '#' + current_line.center(columns) + '#\n'
            current_line = word

    if current_line:
        result += '#' + current_line.center(columns) + '#\n'

    result += space_line + border
    
    return result    