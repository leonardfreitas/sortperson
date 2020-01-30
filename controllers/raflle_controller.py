import os
import commands
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_connection = os.path.join(
    BASE_DIR
)
path_file_raffles = path_connection + '/files/raffles.txt'
path_file_participants = path_connection + '/files/participants.txt'


def route(command):
    if command in commands.RANDOM:
        raffle()
    elif command in commands.CLEAR:
        clear()
    else:
        print("Comando '%s' não reconhecido." %command)


def raffle():
    print(random_participant())


def random_participant():
    with open(path_file_participants, 'r') as file:
        participants = file.readlines()
    with open(path_file_raffles, 'r') as file:
        raffles = file.readlines()
    p = random.choice(participants)
    if not all(elem in raffles for elem in participants):
        if p in raffles:
            random_participant()
        else:
            with open(path_file_raffles, 'a') as file:
                file.write(p)
            return 'SORTEADO: {participant}'.format(participant=p[1:-1].upper())
    return "Não há participantes a serem sorteado. tente zerar a lista de sorteados"


def clear():
    open(path_file_raffles, 'w').close()