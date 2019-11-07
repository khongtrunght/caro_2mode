#from IPython.display import clear_output
from os import system, name
import random


def display_board():
    # clear_output
    system('clear')
    print(' ' + boards[1] + ' | ' + boards[2] + ' | ' + boards[3])
    print('------------')
    print(' ' + boards[4] + ' | ' + boards[5] + ' | ' + boards[6])
    print('------------')
    print(' ' + boards[7] + ' | ' + boards[8] + ' | ' + boards[9])


def player_input():
    choose = ('X', 'O')
    inp = ' '
    while inp not in choose:
        inp = input('1st player, you want to play X or O, please choose X,O :')
    mark_1 = inp
    mark_2 = choose[choose.index(inp) - 1]
    print("you picked " + mark_1 + " 2nd player will be " + mark_2)
    return (mark_1, mark_2)


def lay_o_danh(player):
    vi_tri = '0'
    while int(vi_tri) not in range(1, 10) or not check_hop_le(int(vi_tri)):
        vi_tri = input("Ban %s chon o nao de danh : 1 - 9 :" % (player))
    return int(vi_tri)

def lay_o_danh_bot(player):
    vi_tri = random.randint(1, 9)
    while not check_hop_le(vi_tri):
        vi_tri = random.randint(1,9)
    return vi_tri

def check_hop_le(vi_tri):
    return boards[vi_tri] == ' '


def check_full():
    return ' ' not in boards


def danh_dau(vi_tri, bi_tu):
    boards[vi_tri] = bi_tu


def lay_ten():
    global mode
    mode = input("Ban muon choi voi nguoi hay voi bot? n/b ")
    if mode == 'n':
        a = input("Ten nguoi choi 1 : ")
        b = input("Ten nguoi choi 2 : ")
    else :
        a = input("Ten nguoi choi  : ")
        b = "Bot"
    return (a, b)

# choi voi nguoi 
def choi_vs_nguoi():
    global on_game
    global Luot
    display_board()
    vi_tri = lay_o_danh(Luot)
    danh_dau(vi_tri,bieu_tuong[ten.index(Luot)])
    if check_win(bieu_tuong[ten.index(Luot)]):
        print("Chuc mung %s da chien thang!!"%(Luot))
        on_game = False
    else :
        if check_full():
            print("Khong ai thang ca :( ")
            on_game = False
        else :
            Luot = ten[ten.index(Luot)-1]

#choi vs bot 
def choi_vs_may():
    global on_game
    global Luot
    if Luot == ten[0] :
        display_board()
        vi_tri = lay_o_danh(Luot)
        danh_dau(vi_tri, bieu_tuong[ten.index(Luot)])
        if check_win(bieu_tuong[ten.index(Luot)]):
            display_board()
            print("Chuc mung %s da chien thang!!" % (Luot))
            on_game = False
        else:
            if check_full():
                print("Khong ai thang ca :( ")
                on_game = False
            else:
                Luot = ten[ten.index(Luot) - 1]
    else :
        display_board()
        vi_tri = lay_o_danh_bot(Luot)
        danh_dau(vi_tri, bieu_tuong[ten.index(Luot)])
        if check_win(bieu_tuong[ten.index(Luot)]):
            display_board()
            print("Chuc mung %s da chien thang!!" % (Luot))
            on_game = False
        else:
            if check_full():
                print("Khong ai thang ca :( ")
                on_game = False
            else:
                Luot = ten[ten.index(Luot) - 1]

def check_win(mark):
    return ((boards[7] == mark and boards[8] == mark and boards[9] == mark) or  # across the top
            (boards[4] == mark and boards[5] == mark and boards[6] == mark) or  # across the middle
            (boards[1] == mark and boards[2] == mark and boards[3] == mark) or  # across the bottom
            (boards[7] == mark and boards[4] == mark and boards[1] == mark) or  # down the middle
            (boards[8] == mark and boards[5] == mark and boards[2] == mark) or  # down the middle
            (boards[9] == mark and boards[6] == mark and boards[3] == mark) or  # down the right side
            (boards[7] == mark and boards[5] == mark and boards[3] == mark) or  # diagonal
            (boards[9] == mark and boards[5] == mark and boards[1] == mark))  # diagonal


print("Chao mung den caro !!! ")
while True:
    boards = [" "] * 10
    boards[0] = "ok"
    ten = lay_ten()
    bieu_tuong = player_input()
    on_game = True
    Luot = ten[0]
    while on_game:
        if mode == 'n' :
            choi_vs_nguoi()
        else:
            choi_vs_may()
    choi_tiep = input(" Ban co muon choi tiep : Y / N : ")
    if choi_tiep == 'N':
        exit(0)







