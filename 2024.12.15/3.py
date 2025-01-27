class ChessKing:
    """
    Класс, который описывает шахматную фигуру короля.
    """
    files: dict[str, int] = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8} 
    ranks: dict[str, int] = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
    
    def __init__(self, color: str = 'white', square: str = None):
        self.color = color
        self.square = square or ('e8' if color == 'black' else 'e1')          
            
    
    def __repr__(self):
        if self.color == 'white':
            return f"'WK: {self.square}'"
        else:
            return f"'BK: {self.square}'"
            
    def __str__(self):
        if self.color == 'white':
            return f"WK: {self.square}"
        else:
            return f"BK: {self.square}"

    def _is_move_within_one_square(self, new_square: str) -> bool:
        """
        Вспомогательная функция, которая принимает на вход строку нового поля и проверяет, возможен ли для данной фигуры ход с текущего поля на новое. 
        """
        files_diff = abs(self.files[self.square[0]] - self.files[new_square[0]])
        ranks_diff = abs(self.ranks[self.square[1]] - self.ranks[new_square[1]])
        return files_diff <= 1 and ranks_diff <= 1            

    def is_turn_valid(self, new_square: str) -> bool:
        """
        Функция, которая проверяет возможность хода на новую клетку. 
        """
        return self._is_move_within_one_square(new_square)
    
    def turn(self, new_square: str) -> None:
        """
        Функция, которая принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход.
        """
        if self._is_move_within_one_square(new_square):
            self.square = new_square
        else:
            raise ValueError


# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>> wk.turn('e2')
# >>> wk
# 'WK: e2'
# >>> wk.turn('d4')
# 
# ValueError
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8            
             