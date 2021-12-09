import json
import re

BOOKS_FILE = "books.md"
# BOOK_REGEX = (r'####\s+(?P<position>(\d+))'
# BOOK_REGEX = r'#### (?P<position>\d+)\. \[(?P<book>.+?)]\((?P<book_url>.+?)\) by (?P<author>.+?) \((?P<recommended>.+?)\%.*(?P<cover_url>https.+?) \(?P<description>.+?)'
POSITION = r'####\s+(?P<position>\d+)'
BOOK = r'\[(?P<book>.+?)\]'
BOOK_URL = r'\((?P<book_url>.+?)\)'
AUTHOR = r'(?P<author>.+?)\s'
RECOMMENDED = r'\((?P<recommended>\d{1,3}\.\d+%) recommended\)'
COVER_URL = r'\((?P<cover_url>.+?)\)'
DESCRIPTION = r'\"(?P<description>.+?)\"'


BOOK_REGEX = f"{POSITION}\.\s+{BOOK}{BOOK_URL}\s+by\s+{AUTHOR}{RECOMMENDED}\s+!\[.*?\]{COVER_URL}\s+{DESCRIPTION}"

def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)     # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки
    result = list()
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            result.append(book.groupdict())
            # print(json.dumps(book.groupdict(), indent=4))
    result.sort(key=lambda dict_element: int(dict_element["position"]))

    with open ('result.json', 'w') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    for elem in result:
        print(elem)
if __name__ == '__main__':
    task()

