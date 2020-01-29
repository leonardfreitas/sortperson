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
    if command in commands.LIST:
        list_all()


def create():
    name = input('Nome do participante $>> ')
    index = str(get_next_index())
    with open(path_file, 'a') as file:
        name_linebreak = '{index} {name}\n'.format(index=index, name=name)
        file.write(name_linebreak)
    print('Participante adicionado com sucesso!')


def list_all():
    with open(path_file, 'r') as file:
        for participant in file.readlines():
            p = participant.split(' ')
            print('{index} => {name}'.format(index=p[0], name=p[1][:-1]))


def get_next_index():
    with open(path_file, 'r') as file:
        lines = file.readlines()
        if lines:
            return int(lines[-1].split(' ')[0]) + 1
        return 1
