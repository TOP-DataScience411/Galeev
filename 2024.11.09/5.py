scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
points = 0
word = input()

for i in word:
    for key, value in scores_letters.items():
        if i in value.lower():
            points += key

print(points)

# Второй вариант:
 
# scores_letters = {
#     letter: score 
#     for score, letters in scores_letters.items() 
#     for letter in letters
# }
# 
# points = (
#     sum(scores_letters.get(char, 0) 
#     for char in input().upper())
# )
# 
# print(points)

# Какой варинт более оптимизированный? 

# синхрофазотрон
# 29            