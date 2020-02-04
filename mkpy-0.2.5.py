#!/usr/bin/env python3


'''
@file    mkpy-0.2.5
@brief   Утилита создает шаблон питоновского файла с именем, заданным
         пользователем, в текущем директории.
@version 0.2.5
@date    2020.02.04
@author  Жевак Александр
@email   zhevak@mail.ru
'''


import os
import pwd
import sys
import argparse
from datetime import datetime

EMAIL = u'zhevak@mail.ru'

FILE_TEMPLATE = """#!/usr/bin/env python3


'''
@module  {module}
@version <укажите версию>
@date    {date}
@author  {author}
@email   {email}

@brief   <вставьте сюда краткое описание модуля>
'''


if __name__ == "__main__":

    pass
"""


HELP = '''Генератор шаблонов Python-овских модулей.
Создаёт файлы-шаблоны и делает их исполняемыми.

Используйте так: mkpy [-h] [module[ module [module] ...]]]

Аргумены:
  -h, --help                        Показать эту помощь
  [module[ module [module] ...]]]   Список имён модулей (без суффикса ".py")
'''


def get_user_info():
    login = os.getlogin()
    info = pwd.getpwnam(login)
    gecos = info.pw_gecos.split(',')

    username = os.environ.get('GIT_AUTHOR_NAME') or (login if len(gecos) == 1 else gecos[0])
    email = os.environ.get('GIT_AUTHOR_EMAIL') or EMAIL
    return username, email


def make_py(module):
    if not module.lower().endswith('.py'):
        filename = module + '.py'
    else:
        filename = module

    # Убедимся, что не перезапишем существующий с таким же именем файл
    if os.path.isfile(filename):
        print('ОШИБКА: файл {} уже существует'.format(filename))
        return

    username, email = get_user_info()
    params = {
        'module': module,
        'date': datetime.now().strftime('%Y.%m.%d'),
        'author': username,
        'email': email
    }

    # Создадим файл и запишем в него шаблон
    with open(filename, 'w') as f:
        f.write(FILE_TEMPLATE.format(**params))

    # Сделаем файл исполняемым
    os.chmod(filename, 0o755)


def show_help():
    print('Используйте: mkpy <имя модуля>')


if __name__ == '__main__':

    if (len(sys.argv) == 1) or ('-h' in sys.argv) or ('--help' in sys.argv):
        print(HELP)
    else:
        for arg in sys.argv[1:]:
            make_py(arg)

