from random import randrange

def tree_generator() -> list:
    """ 
    Рекурсивная функция, которая генерирует дерево с произвольным количеством веток и листьев.
    Правила генерирования дерева:
    - Вложенность веток должна быть произвольной.
    - Возвращаемый список не может быть пустым.
    - Вложенные списки (ветки) могут быть пустыми.
    """
    tree = []
    num_leaves = randrange(5)

    branch = ['leaf' for _ in range(num_leaves)]

    if randrange(10):
        branch.append(tree_generator())

    tree.append(branch)
    return tree

# >>> tree_generator()
# [['leaf', [['leaf', 'leaf', 'leaf', 'leaf', [['leaf', 'leaf', 'leaf', 'leaf', [['leaf', 'leaf', [['leaf', 'leaf', 'leaf']]]]]]]]]]
# >>> tree_generator()
# [['leaf', 'leaf']]
# >>> tree_generator()
# [['leaf', [['leaf', [['leaf', 'leaf', [[[['leaf', 'leaf', 'leaf', 'leaf']]]]]]]]]]
# >>> tree_generator()
# [['leaf', 'leaf', [['leaf', 'leaf', 'leaf', 'leaf']]]]
# >>> tree_generator()
# [['leaf', 'leaf', [['leaf', [['leaf', [[[['leaf', 'leaf', 'leaf', [[]]]]]]]]]]]]
# >>> tree_generator()
# [['leaf', [[[['leaf', 'leaf', 'leaf', 'leaf', [['leaf', 'leaf', 'leaf', 'leaf', [[[['leaf', 'leaf', 'leaf', 'leaf', [['leaf', 'leaf', 'leaf', 'leaf', [['leaf']]]]]]]]]]]]]]]]
# >>> tree_generator()
# [[]]
# >>> tree_generator()
# [['leaf', 'leaf', 'leaf', 'leaf', [['leaf', 'leaf', 'leaf', 'leaf', [['leaf', 'leaf', [['leaf', 'leaf', 'leaf', 'leaf', [[[['leaf', 'leaf', 'leaf', 'leaf', [['leaf', 'leaf', 'leaf', [[[['leaf', 'leaf', 'leaf']]]]]]]]]]]]]]]]]]

   
    
   
        
        
    
        
        
    
   

          