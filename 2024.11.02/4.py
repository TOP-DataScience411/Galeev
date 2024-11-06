chess_square1 = input()
chess_square2 = input()

horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x1 = int(chess_square1[1])
x2 = int(chess_square2[1])
y1 = horizontal.index(chess_square1[0]) + 1
y2 = horizontal.index(chess_square2[0]) + 1

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print('да')
else:
    print('нет') 

# a1
# b2
# да    