import os
import commands

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_connection = os.path.join(
    BASE_DIR
)
path_file = path_connection + '/files/participants.txt'


def route(command):
    if command in commands.CREATE:
        create()


def create():
    name = input('Nome do participante $>> ')
    with open(path_file, 'a') as file:
        name_linebreak = '{name}\n'.format(name=name)
        file.write(name_linebreak)
    print('Participante adicionado com sucesso!')
