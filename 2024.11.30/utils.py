from shutil import get_terminal_size

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
    
# >>> text = 'Обратите внимание на очень важное сообщение от команды разработчиков этой великолепной программы'
# >>> msg = important_message(text)
# >>> print(msg)
#==================================================================#
#                                                                  #
#      Обратите внимание на очень важное сообщение от команды      #
#            разработчиков этой великолепной программы             #
#                                                                  #
#==================================================================#    

  
      