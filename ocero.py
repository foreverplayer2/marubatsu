import random
import pandas as pd

board = pd.DataFrame([[1, 2, 3, 4, 5, 6, 7, 8],
                      [9, 10, 11, 12, 13, 14, 15, 16],
                      [17, 18, 19, 20, 21, 22, 23, 24],
                      [25, 26, 27, 'o', 'x', 30, 31, 31],
                      [33, 34, 35, 'x', 'o', 38, 39, 40],
                      [41, 42, 43, 44, 45, 46, 47, 48],
                      [49, 50, 51, 52, 53, 54, 55, 56],
                      [57, 58, 59, 60, 61, 62, 63, 64]])

my_turn = True

def my_action():
    global my_turn
    print('白丸を置きたい場所を横(0~7), 縦(0~7)で決めてね!')
    put_shiromaru = input().split(',')
    shiromaru_yoko = int(put_shiromaru[0])
    shiromaru_tate = int(put_shiromaru[1])
    
    while my_turn:
        if board[shiromaru_yoko][shiromaru_tate] != 'o' and board[shiromaru_yoko][shiromaru_tate] != 'x':
            board[shiromaru_yoko][shiromaru_tate] = 'o'
            my_turn = False
            
    print(board)
    
    for i in range(6):
        if i < shiromaru_yoko and board[i][shiromaru_tate] == 'o':
            if 'o' not in board.iloc[i+1:shiromaru_yoko, shiromaru_tate:shiromaru_tate+1]:
                for j in range(i+1, shiromaru_yoko):
                    if board[j][shiromaru_tate] == 'x':
                        board[j][shiromaru_tate] = 'o'
        
        elif i > shiromaru_yoko and board[i][shiromaru_tate] == 'o':
            if 'o' not in board.iloc[shiromaru_yoko+1:i, shiromaru_tate:shiromaru_tate+1]:  
                for k in range(shiromaru_yoko+1, i):
                   if board[k][shiromaru_tate] == 'x':
                       board[k][shiromaru_tate] = 'o'
                
    print(board)
                
    
my_action()