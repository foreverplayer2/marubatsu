import random
import time
import pandas as pd


import pandas as pd

field =  pd.DataFrame([['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']])

running = True

def my_action():
    print('丸を書きたいところを横(0~2), 縦(0~2)で選択してね!')
    maru_place = input().split(',')
    maru_yoko = int(maru_place[0])
    maru_tate = int(maru_place[1])
    field[maru_yoko][maru_tate] = 'o'
    print(field)
    
def enemy_action():
    batsu_yoko = 0
    batsu_tate = 0
    enemy_turn = True
    while enemy_turn:
        batsu_yoko = random.randint(0, 2)
        batsu_tate = random.randint(0, 2)
        if field[batsu_yoko][batsu_tate] != 'o' and field[batsu_yoko][batsu_tate] != 'x':
            field[batsu_yoko][batsu_tate] = 'x'
            enemy_turn = False
    print(field)

def judge(field):
    for i in range(2):
        if field[i][0] == field[i][1] and field[i][1] == field[i][2]:
            return(field[i][0])
            running = False
            
        elif field[0][i] == field[1][i] and field[1][i] == field[2][i]:
            return(field[0][i])
            running = False

        elif field[0][0] == field[1][1] and field[1][1] == field[2][2]:
            return(field[0][0])
            running = False
        
        else:
            pass
        

        

       