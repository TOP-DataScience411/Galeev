from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
from utils import load_file

def ask_for_file ():
    """ 
    Функция, которая запрашивает у пользователя путь к потерянному файлу и копирует этот файл с помощью функции load_file.
    """
    file_path = Path(input(r'Путь:'))
    
    while not file_path.exists():
        print('! по указанному пути отсутствует необходимый файл !')
        file_path = Path(input(r'Путь:'))
        
    path = load_file(file_path)
    spec =  spec_from_file_location(path.stem, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return module

# >>> config_module = ask_for_file()
# Путь:d:\student\2023.05.28\conf.py
# ! по указанному пути отсутствует необходимый файл !
# Путь:C:\Users\79526\Galeev\2024.12.14\data\conf.py
# >>>
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}