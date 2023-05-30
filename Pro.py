import math
def sum(a,b,c):
   return a+b+c

#def board 
def printBoard( xState, zState):
    zero='X' if xState[0] else ('O' if zState[0] else 0 )
    one='X' if xState[1] else ('O' if zState[1] else 1 )
    two='X' if xState[2] else ('O' if zState[2] else 2 )
    three='X' if xState[3] else ('O' if zState[3] else 3 )
    four='X' if xState[4] else ('O' if zState[4] else 4 )
    five='X' if xState[5] else ('O' if zState[5] else 5 )
    six='X' if xState[6] else ('O' if zState[6] else 6 )
    seven='X' if xState[7] else ('O' if zState[7] else 7 )
    eight='X' if xState[8] else ('O' if zState[8] else 8 )

    print(f"{zero} | {one} | {two}" )
    print(f'--|---|--')
    print(f'{three} | {four} | {five}' )
    print(f'--|---|--')
    print(f'{six} | {seven} | {eight}' )

def check_win(xState,zState):
   wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  
   for win in wins:
    
    if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
      return 1
    if(sum(zState[win[0]],zState[win[1]],zState[win[2]])==3):
      return 0
   return -1
#if board is full
def boardIsFull(xState,zState):
    for i in range(9):
      if ( xState[i]==0 and zState[i]==0): 
            return False 
    return True
#if position free or not

def returnInput(xState,zState,value):
   for i in range(9):
      if (value==i and xState[i]==0 and zState[i]==0): 
          return True
         
   return False  
#to insert
def insert(state,value):
   if(returnInput(xState,zState,value)):
       state[value]=1
   else:
      value= int(input('please enter anther value for free position !')) 
      insert(state,value)  


#best move
def bestMove(xState,zState):
    best_score = -math.inf
    best_move = -1  #position it return to best move 
    for i in range(9):
     if xState[i]==0 and zState[i]==0:
      xState[i]=1
      score= minimax(xState,zState,0,False)
      xState[i]=0
          
      if score>best_score:
             best_score=score
             best_move=i
    return best_move          

scores={1:1 , 0:-1 } # i is mean x  0 is mean o
def minimax(xState,zState,depth,isMaximizing):
   
   result=check_win(xState,zState)
   if result != -1:
      return scores[result]
      
   if(boardIsFull(xState,zState)):
      return 0
   
   if isMaximizing:
     best_score = -math.inf
     for i in range(9):
        if xState[i]==0 and zState[i]==0:
            xState[i] = 1
            score = minimax(xState, zState, depth + 1, False)
            xState[i] = 0
            best_score = max(score, best_score)
     return best_score
   else:
     best_score = math.inf
     for i in range(9):
        if xState[i]==0 and zState[i]==0:
            zState[i] = 1
            score = minimax(xState, zState, depth + 1, True)
            zState[i] = 0
            best_score = min(score, best_score)
     return best_score
          


#start of program
if __name__== "__main__":
    xState=[0,0,0, 0,0,0, 0,0,0]
    zState=[0,0,0, 0,0,0, 0,0,0]
    turn=1  ##### 1->X ,0->O
    print('Tic Tac Toe Game')
   
    while(True):
    
      printBoard(xState, zState)
      if(turn==0):
         
          value=bestMove(xState,zState)
          xState[value]=1
      else:
         print('O Chances')
         value= int(input('please enter the value of position'))
         insert(zState,value)

      check=check_win(xState,zState)
      if(check != -1):
            if(check==1):
                printBoard(xState, zState)
                print('========================')
                print('X is win' )
                print('========================')
            else:
                printBoard(xState, zState)
                print('========================')
                print('X is win' )
                print('========================') 

            print('game end')
            print('========================')
            break
      if(boardIsFull(xState,zState)):
         print('========================')
         print('NO one is win ' )
         print('========================')
         break
      else:  
       turn=1-turn
    