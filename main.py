import commands
from controllers.participant_controller import route as participants_route
from controllers.raflle_controller import route as raffle_route

run = True

while run:
    command = input('$>> ')
    if command in commands.EXIT:
        run = False
    elif command.split(' ')[0] in commands.PARTICIPANTS:
        participants_route(command.split(' ')[1])
    elif command in commands.RANDOM or command in commands.CLEAR:
        raffle_route(command)
    else:
        print('Comando não reconhecido!')
