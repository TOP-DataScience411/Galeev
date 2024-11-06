chess_square1 = input()
chess_square2 = input()

horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x1 = int(chess_square1[1])
x2 = int(chess_square2[1])
y1 = horizontal.index(chess_square1[0]) + 1
y2 = horizontal.index(chess_square2[0]) + 1

if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('да')
else:
    print('нет')

# g3
# f2
# да

# c6
# d4
# нет