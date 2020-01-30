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
    elif command in commands.LIST:
        list_all()
    elif command in commands.UPDATE:
        update()
    elif command in commands.DELETE:
        delete()
    else:
        print("Comando '%s' não reconhecido." %command)


def create():
    name = input('Nome do participante $>> ')
    index = str(get_next_index())
    with open(path_file, 'a') as file:
        name_linebreak = '{index} {name}\n'.format(index=index, name=name)
        file.write(name_linebreak)
    print('Participante adicionado com sucesso!')


def update():
    print('- Digite o índice do participante que deseja editar')
    list_all()
    participant_update = input('[ Índice ] $>> ')
    participants_updated = []
    with open(path_file, 'r') as file:
        for participant in file.readlines():
            p = participant.split(' ')
            if participant_update != p[0]:
                participants_updated.append(participant)
            else:
                new_name = input('Novo nome $>> ')
                new_value = '{index} {name}\n'.format(index=p[0], name=new_name)
                participants_updated.append(new_value)
    with open(path_file, 'w') as f:
        f.writelines(participants_updated)
    print('Participante atualizado com sucesso')


def list_all():
    with open(path_file, 'r') as file:
        for participant in file.readlines():
            p = participant.split(' ')
            print('{index} => {name}'.format(index=p[0], name=p[1][:-1]))


def delete():
    print('- Digite o índice do participante que deseja excluir')
    list_all()
    participant_del = input('[ Índice ] $>> ')
    new_list = []
    with open(path_file, 'r') as file:
        for participant in file.readlines():
            p = participant.split(' ')
            if participant_del != p[0]:
                new_list.append(participant)
    with open(path_file, 'w') as f:
        f.writelines(new_list)
    print('Participante Excluído')


def get_next_index():
    with open(path_file, 'r') as file:
        lines = file.readlines()
        if lines:
            return int(lines[-1].split(' ')[0]) + 1
        return 1
