from pathlib import Path

def list_files (path: str) -> tuple[str]:
    """
    Функция, которая возвращает кортеж с именами файлов в каталоге по переданному пути.
    Осуществляется нерекурсивный поиск.
    """
    path = Path(path)
    
    if path.exists():
        content = tuple(
            el.name 
            for el in path.iterdir() 
            if not el.is_dir()
        )
        return content
    else:
        return         
    
    
# C:\Users\79526\Galeev\2024.12.14
#  20:50:35 > tree /f
# 
# C:.
# │   # HW 2024.12.14.txt
# │   1.py
# │
# └───data
#     │   7MD9i.chm
#     │   conf.py
#     │   E3ln1.txt
#     │   F1jws.jpg
#     │   le1UO.txt
#     │   q40Kv.docx
#     │   questions.quiz
#     │   r62Bf.txt
#     │   vars.py
#     │   xcD1a.zip
#     │
#     ├───c14KE
#     │       5vsIh.dat
#     │       P2a91.dat
#     │
#     ├───mXbd9
#     │       RoBjg.pt
#     │       z03EN.pt
#     │
#     └───names
#             женские_имена.txt
#             мужские_имена_отчества.txt
#             фамилии.txt

# >>> list_files(r'C:\Users\79526\Galeev\2024.12.14\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')    