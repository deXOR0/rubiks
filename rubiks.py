import random
import keyboard
import time

ao5 = 0
total = 0
last_five_solves = []
moves = ['F', 'F2', 'F\'', 'B', 'B2', 'B\'', 'R', 'R2', 'R\'',
         'L', 'L2', 'L\'', 'U', 'U2', 'U\'', 'D', 'D2', 'D\'']
file_name = 'rubiks.txt'

n = 21


def format_time(solve_time):
    minutes = int(solve_time // 60)
    seconds = solve_time % 60
    return '{:02d}:{:05.2f}'.format(minutes, seconds)


def init():
    print('██████╗░██╗░░░██╗██████╗░██╗██╗░░██╗░██████╗')
    print('██╔══██╗██║░░░██║██╔══██╗██║██║░██╔╝██╔════╝')
    print('██████╔╝██║░░░██║██████╦╝██║█████═╝░╚█████╗░')
    print('██╔══██╗██║░░░██║██╔══██╗██║██╔═██╗░░╚═══██╗')
    print('██║░░██║╚██████╔╝██████╦╝██║██║░╚██╗██████╔╝')
    print('╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═════╝░')
    print('              Created by XOR0\n')


def stat():
    global ao5, last_five_solves

    if len(last_five_solves) == 5:
        ao5 = sum(last_five_solves) / len(last_five_solves)
        last_five_solves.clear()
        print(last_five_solves)

    print('Statistics')
    print('ao5:', format_time(ao5))


def write_to_file(scramble, solve_time, f_time):
    file = open(file_name, 'a')
    file.write('Scramble: {}\n'.format(scramble))
    file.write('Solve Time: {}\n'.format(solve_time))
    file.write('Formatted Time: {}\n\n'.format(f_time))
    file.close()


init()

while True:

    sequence = []

    ban = ''
    for i in range(n):
        while True:
            next_move = moves[random.randint(0, len(moves)-1)]
            if next_move[0] == ban:
                continue
            else:
                ban = next_move[0]
                sequence.append(next_move)
                break

    stat()
    print('')
    scramble = ' '.join(sequence)

    print(scramble)

    start = 0

    while True:
        if keyboard.is_pressed(' '):
            if not keyboard.is_pressed(' '):
                start = time.time()
                break

    print('GO')

    while not keyboard.is_pressed(' '):
        continue

    end = time.time()

    solve_time = end - start

    f_time = format_time(solve_time)

    print(f_time)

    write_to_file(scramble, solve_time, f_time)

    last_five_solves.append(solve_time)

    input('Press Enter to continue\n')
