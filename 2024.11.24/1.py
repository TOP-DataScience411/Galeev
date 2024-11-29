def deck () -> object:
    """
    Функция, которая создаёт упорядоченную колоду карт.
    
    На каждой итерации генератор возвращает кортеж из двух элементов:
    - целое число, обозначающее номинал карты: 2, 3 ... 10, 11 — валет, 12 — дама, 13 — король, 14 — туз.
    - строка, обозначающая масть карты: 'черви', 'бубны', 'пики', 'трефы'.
    
    Колода упорядочивается следующим образом:
        сначала все номиналы червей, затем все номиналы бубен, затем все номиналы пик и в конце все номиналы треф.
    """
   card_suit = ['черви', 'бубны', 'пики', 'трефы']
   count = 2
   
   for elem in card_suit:
       while count < 15:
           yield (count, elem)
           count += 1
       count = 2

# Как в аннотации указать, что возвращается объект генератор?       

# list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]       
   