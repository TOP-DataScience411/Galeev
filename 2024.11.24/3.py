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
    
def tree_leaves (tree: list) -> int:
    """
    Функиция, которая считает количество листьев на дереве.
    """    
    num_leaves = 0
    
    for elem in tree:
        if type(elem) is list:
            num_leaves += tree_leaves(elem)
        else:
            num_leaves += 1
        
    return num_leaves 
    
# >>> tree = tree_generator()
# >>> tree
# [['leaf', 'leaf', [['leaf', 'leaf']]]]
# >>> tree_leaves(tree)
# 4    

# >>> tree_leaves([[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']])
# 38    