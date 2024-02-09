import random
import time
import pandas as pd

field =  pd.DataFrame([['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']])

running = True

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
        

       