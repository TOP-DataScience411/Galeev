from urllib.request import urlopen
from re import findall, S
from pathlib import Path
from charset_normalizer import from_bytes
from json import dump
from gzip import decompress

def json_from_html (url: str, re_pattern: str, default_encoding = 'utf-8') -> Path:
    """
    Функция, которая по заданному шаблону извлекает из HTML документа структурируемые данные и помещает их в JSON файл.
    Функция возвращает путь к созданному JSON файлу в виде объекта Path.
    """
    with urlopen(url) as response:
        html = response.read()

        if response.headers.get('Content-Encoding') == 'gzip':
            html = decompress(html)
            
    result = from_bytes(html).best()
    encoding = result.encoding or default_encoding
    html = html.decode(encoding)    
    
    data = findall(re_pattern, html, S)
    if not all(len(el) == 2 for el in data):
        raise ValueError("Регулярное выражение должно возвращать пары (ключ, значение)")
        
    json_dict = {el[0]: el[1] for el in data}
    
    if url.endswith('.html'):
        path_json = Path(
            Path(url).name.replace('html', 'json')
            )
    else:
       path_json = Path(
           Path(__loader__.path).name.replace('py', 'json')
           )
       
    with path_json.open('w', encoding='utf-8') as file:
        dump(json_dict, file, indent = 2, ensure_ascii = False)
        
    return path_json 
    
# >>> url = 'https://docs.python.org/3/py-modindex.html'
# >>> modules_pattern = r'<tr>.+?>(\w+?)<.+?</td><td>.*?<em>(.*?)</em>'
# >>> file_path = json_from_html(url, modules_pattern)
# >>> file_path.name
# 'py-modindex.json'
# >>> print(file_path.read_text(encoding='utf-8')[:110])
# {
  # "__future__": "Future statement definitions",
  # "__main__": "The environment where top-level code is run.
# >>>
# >>>
# >>> url = 'http://www.world-art.ru/cinema/rating_top.php'
# >>> films_pattern = (r'<tr .*?>'
# ... r'<td .*?<a.*?>(?P<name>.*?)</a>.*?</td>'
# ...  r'<td .*?>(?P<rating>.*?)</td>')
# >>> file_path = json_from_html(url, films_pattern)
# >>> file_path.name
# 'json_from_html.json'
# >>> Path(__loader__.path).name
# 'json_from_html.py'
# >>> print(file_path.read_text(encoding='utf-8')[:110])
# {
  # "Побег из Шоушенка": "8.9755",
  # "Зелёная миля": "8.9540",
  # "Форрест Гамп": "8.9035",
  # "Леон": "8.8920",


  