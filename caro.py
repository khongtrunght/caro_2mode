from IPython.display import clear_output
from os import system, name
import random
from typing import List, Any


def display_board():
    #clear_output
    system('clear')
    print(' ' + boards[1] + ' | ' + boards[2] + ' | ' + boards[3])
    print('------------')
    print(' ' + boards[4] + ' | ' + boards[5] + ' | ' + boards[6])
    print('------------')
    print(' ' + boards[7] + ' | ' + boards[8] + ' | ' + boards[9])


def player_input():
    global choose
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
    kha_thi = []
    kha_thi = [x for x, lay_o in enumerate(boards) if lay_o == ' ' and x != 0]
    for xet in choose :
        for i in kha_thi:
            boards_copy = boards[:]
            boards_copy[i] = xet
            if check_win(xet,boards_copy) :
                return i

    if 5 in kha_thi:
        return 5

    goc_trong = []
    for i in kha_thi:
        if i in [1,3,7,9] :
            goc_trong.append(i)
    if len(goc_trong) > 0 :
        return random_pick(goc_trong)
    o_trong = []
    for i in kha_thi:
        if i in [2,4,6,8] :
            o_trong.append(i)
    if len(o_trong) > 0 :
        return random_pick(o_trong)



def random_pick(set):
    import random
    l = len(set)
    return set[random.randrange(0,l)]

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
    if check_win(bieu_tuong[ten.index(Luot)],boards):
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
        if check_win(bieu_tuong[ten.index(Luot)],boards):
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
        if check_win(bieu_tuong[ten.index(Luot)],boards):
            display_board()
            print("Chuc mung %s da chien thang!!" % (Luot))
            on_game = False
        else:
            if check_full():
                print("Khong ai thang ca :( ")
                on_game = False
            else:
                Luot = ten[ten.index(Luot) - 1]

def check_win(mark,boards):
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







