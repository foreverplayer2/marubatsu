import random
import pandas as pd

field =  pd.DataFrame([['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']])


def my_action():
    my_turn = True
    while my_turn:
        print('丸を書きたいところを横(0~2), 縦(0~2)で選択してね!')
        maru_place = input().split(',')
        maru_yoko = int(maru_place[0])
        maru_tate = int(maru_place[1])
        if field[maru_yoko][maru_tate] != 'o' or field[maru_yoko][maru_tate] != 'x':
            field[maru_yoko][maru_tate] = 'o'
            my_turn = False   
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

result = 0
count = 0
def judge(field):
    global count
    global result
    for j in range(2):
        if field[0][j] == 'o' or field[0][j] == 'x':
            count += 1
        
        if field[1][j] == 'o' or field[1][j] == 'x':
            count += 1
        
        if field[2][j] == 'o' or field[2][j] == 'x':
            count += 1

    if count < 9:
        for i in range(2):
            if field[i][0] == field[i][1] and field[i][1] == field[i][2]:
                result = 1
                print(f'{field[i][0]}のプレイヤーの勝利です！')
                        
                    
            elif field[0][i] == field[1][i] and field[1][i] == field[2][i]:
                result = 1
                print(f'{field[0][i]}のプレイヤーの勝利です！')

        if field[0][0] == field[1][1] and field[1][1] == field[2][2]:
            result = 1
            print(f'{field[0][0]}のプレイヤーの勝利です!')
    
        elif field[2][0] == field[1][1] and field[1][1] == field[0][2]:
            result = 1
            print(f'{field[2][0]}のプレイヤーの勝利です!')
    

    elif count == 9:
        for i in range(2):
            if field[i][0] == field[i][1] and field[i][1] == field[i][2]:
                result = 1
                print(f'{field[i][0]}のプレイヤーの勝利です!')

            elif field[0][i] == field[1][i] and field[1][i] == field[2][i]:
                result = 1
                print(f'{field[0][i]}のプレイヤーの勝利です!')

        if field[0][0] == field[1][1] and field[1][1] == field[2][2]:
            result = 1
            print(f'{field[0][0]}のプレイヤーの勝利です!')
        
        elif field[2][0] == field[1][1] and field[1][1] == field[0][2]:
            result = 1
            print(f'{field[2][0]}のプレイヤーの勝利です!')            
        
        if result == 0:
            result = 1
            print('引き分けです')
        
def taisen():
    running = True
    while running:
       my_action()
       enemy_action()
       judge(field)
       
       if result == 1:
           running = False

taisen()