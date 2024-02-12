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

print(board)

my_turn = True

def my_action():
    global my_turn
    print('白丸を置きたい場所を横(0~7), 縦(0~7)で決めてね!')
    put_shiromaru = input().split(',')
    shiromaru_yoko = int(put_shiromaru[0])
    shiromaru_tate = int(put_shiromaru[1])
    
    while my_turn:
        if board[shiromaru_yoko][shiromaru_tate] != 'o' and board[shiromaru_yoko][shiromaru_tate] != 'x':
            if board[shiromaru_yoko+1][shiromaru_tate] == 'x':
                if shiromaru_yoko < 6: 
                    board_part1 = board.iloc[shiromaru_yoko+2:8, shiromaru_tate:shiromaru_tate+1]
                    if 'o' in board_part1:
                        board[shiromaru_yoko][shiromaru_tate] = 'o'
                        my_turn = False
                        
            if board[shiromaru_yoko-1][shiromaru_tate] == 'x': 
                if shiromaru_yoko > 1:
                    board_part2 = board.iloc[0:shiromaru_yoko-1, shiromaru_tate:shiromaru_tate+1] 
                    if 'o' in board_part2:
                        board[shiromaru_yoko][shiromaru_tate] = 'o'
                        my_turn = False
            
            if board[shiromaru_yoko][shiromaru_tate+1] == 'x': 
                if shiromaru_tate < 6:
                    board_part3 = board.iloc[shiromaru_yoko:shiromaru_yoko+1, shiromaru_tate+2:8]
                    if 'o' in board_part3:
                        board[shiromaru_yoko][shiromaru_tate] = 'o'
                        my_turn = False

            if board[shiromaru_yoko][shiromaru_tate-1] == 'x':
                if shiromaru_tate > 1:
                    board_part4 = board.iloc[shiromaru_yoko:shiromaru_yoko+1, 0:shiromaru_tate-1]
                    if 'o' in board_part4:
                        board[shiromaru_yoko][shiromaru_tate] = 'o'
                        my_turn = False
            
            if board[shiromaru_yoko-1][shiromaru_tate-1] == 'x':
                if shiromaru_yoko > 1 and shiromaru_tate > 1:
                    for i in range(2, min(shiromaru_yoko, shiromaru_tate)+1):
                        if 'o' == board[shiromaru_yoko-i][shiromaru_tate-i]:
                            board[shiromaru_yoko][shiromaru_tate] = 'o'
                            my_turn = False
            
            if board[shiromaru_yoko+1][shiromaru_tate-1] == 'x':
                if shiromaru_yoko < 6 and shiromaru_tate > 1: 
                    for i in range(2, min(7-shiromaru_yoko,shiromaru_tate)+1):
                        if 'o' == board[shiromaru_yoko+i][shiromaru_tate-i]:
                            board[shiromaru_yoko][shiromaru_tate] = 'o'
                            my_turn = False
            
            if board[shiromaru_yoko-1][shiromaru_tate+1] == 'x': 
                if shiromaru_yoko > 1 and shiromaru_tate < 6:
                    for i in range(2, min(shiromaru_yoko, 7-shiromaru_tate)+1):
                        if 'o' == board[shiromaru_yoko-i][shiromaru_tate+i]:
                            board[shiromaru_yoko][shiromaru_tate] = 'o'
                            my_turn = False
                        
            if board[shiromaru_yoko+1][shiromaru_tate+1] == 'x':
                if shiromaru_yoko < 6 and shiromaru_tate < 6:
                    for i in range(2, min(8-shiromaru_yoko, 8-shiromaru_tate)):
                        if 'o' == board[shiromaru_yoko+i][shiromaru_tate+i]:
                            board[shiromaru_yoko][shiromaru_tate] = 'o'
                            my_turn = False                       
    print(board)
    
    for i in range(7):
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
        
        if i < shiromaru_tate and board[shiromaru_yoko][i] == 'o':
            if 'o' not in board.iloc[shiromaru_yoko:shiromaru_yoko+1, i+1:shiromaru_tate]:
                for l in range(i+1, shiromaru_tate):
                    if board[shiromaru_yoko][l] == 'x':
                        board[shiromaru_yoko][l] = 'o'
                        
        elif i > shiromaru_tate and board[shiromaru_yoko][i] == 'o':
            if 'o' not in board.iloc[shiromaru_yoko:shiromaru_yoko+1, shiromaru_tate+1:i]:
                for m in range(shiromaru_tate+1, i):
                    if board[shiromaru_yoko][m] == 'x':
                        board[shiromaru_yoko][m] = 'o'
                        
        if i < shiromaru_tate and board[shiromaru_yoko-i][shiromaru_tate-i] == 'o':
            if 'o' not in board.iloc[shiromaru_yoko:shiromaru_yoko+1, shiromaru_tate+1:i]:
                for n in range(i+1, shiromaru_tate):
                    if board[shiromaru_yoko][n] == 'x':
                        board[shiromaru_yoko][n] = 'o'
                        
        elif i > shiromaru_tate and board[shiromaru_yoko][i] == 'o':
            if 'o' not in board.iloc[shiromaru_yoko:shiromaru_yoko+1, shiromaru_tate+1:i]:
                for p in range(shiromaru_tate+1, i):
                    if board[shiromaru_yoko][p] == 'x':
                        board[shiromaru_yoko][p] = 'o'                   
    print(board)
                
    
my_action()