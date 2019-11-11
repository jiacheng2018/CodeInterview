import numpy as np
def NumToStr(x):
    if(x==0):
        return "EAST"
    elif(x==1):
        return "SOUTH"
    elif(x==2):
        return "WEST"
    elif(x==3):
        return "NORTH"

def StrToNum(x):
    if(x=="EAST"):
        return 0
    elif(x=="SOUTH"):
        return 1
    elif(x=="WEST"):
        return 2
    elif(x=="NORTH"):
        return 3

class State:#DESCRIBE THE STATE
    def __init__(self,x,y,F):
        self.pos=np.array([x,y])
        self.F=StrToNum(F)
        self.Go=np.array([[1,0],[0,-1],[-1,0],[0,1]])
    def makeSure(self):
        if(self.pos[0]<0):
            self.pos[0] += 1
        if(self.pos[0]>4):
            self.pos[0] -= 1
        if(self.pos[1]>4):
            self.pos[1] -= 1
        if(self.pos[1]<0):
            self.pos[1] += 1

def REPORT(curState):
    '''
    RETURN RESULT
    '''
    return 'Output: {},{},{}'.format(curState.pos[0],curState.pos[1],NumToStr(curState.F))

def leftAndRight(curState,Change):
    '''
    LISTEN TO CHANGE 
    '''
    if(Change=="LEFT"):
        curState.F=(curState.F+3)%4;
    elif(Change=="RIGHT"):
        curState.F=(curState.F+5)%4;

def testLeftAndRight():
    '''
    TESTING 
    '''
    print('----------------------*testLeftAndRight*----------------------')
    curState = State(0,0,'WEST')
    print('Now curState is ',REPORT(curState))
    leftAndRight(curState,'LEFT')
    print('Turn LEFT')
    print('Now curState is ',REPORT(curState))
    curState = State(0,0,'WEST')
    print('Return back ')
    print('Now curState is ',REPORT(curState))
    print('Turn RIGHT')
    leftAndRight(curState,'RIGHT')
    print('Now curState is ',REPORT(curState))
    curState = State(0,0,'EAST')
    print('Now curState is ',REPORT(curState))
    leftAndRight(curState,'LEFT')
    print('Turn LEFT')
    print('Now curState is ',REPORT(curState))
    curState = State(0,0,'EAST')
    print('Return back ')
    print('Now curState is ',REPORT(curState))
    print('Turn RIGHT')
    leftAndRight(curState,'RIGHT')
    print('Now curState is ',REPORT(curState))
    curState = State(0,0,'NORTH')
    print('Now curState is ',REPORT(curState))
    leftAndRight(curState,'LEFT')
    print('Turn LEFT')
    print('Now curState is ',REPORT(curState))
    curState = State(0,0,'NORTH')
    print('Return back ')
    print('Now curState is ',REPORT(curState))
    print('Turn RIGHT')
    leftAndRight(curState,'RIGHT')
    print('Now curState is ',REPORT(curState))
    curState = State(0,0,'SOUTH')
    print('Now curState is ',REPORT(curState))
    leftAndRight(curState,'LEFT')
    print('Turn LEFT')
    print('Now curState is ',REPORT(curState))
    curState = State(0,0,'SOUTH')
    print('Return back ')
    print('Now curState is ',REPORT(curState))
    print('Turn RIGHT')
    leftAndRight(curState,'RIGHT')
    print('Now curState is ',REPORT(curState))
    return 

def changeF(curState,InPut):
    
    curState.F = StrToNum(InPut)

def testChangeF():
    '''
    TESTING 
    '''
    print('----------------------*testChangeF*----------------------')
    curState = State(0,0,'WEST')
    print('Now curState is ',REPORT(curState))
    print('changeF(curState,EAST)')
    changeF(curState,'EAST')
    print('Now curState is ',REPORT(curState))
    print('changeF(curState,SOUTH)')
    changeF(curState,'SOUTH')
    print('Now curState is ',REPORT(curState))
    print('changeF(curState,NORTH)')
    changeF(curState,'NORTH')
    print('Now curState is ',REPORT(curState))
    print('changeF(curState,EAST)')
    changeF(curState,'EAST')
    print('Now curState is ',REPORT(curState))
def MOVE(curState):
    '''
    MOVE OBJECT 
    '''
    curState.pos+=curState.Go[curState.F]

def testMOVE():
    print('----------------------*testMOVE*----------------------')
    curState = State(0,0,'EAST')
    print('Now curState is ',REPORT(curState))
    print('MOVE(curState)')
    MOVE(curState)
    print('Now curState is ',REPORT(curState))
    print('changeF(curState,WEST)')
    changeF(curState,'WEST')
    print('MOVE(curState)')
    MOVE(curState)
    print('Now curState is ',REPORT(curState))
    print('changeF(curState,NORTH)')
    changeF(curState,'NORTH')
    print('MOVE(curState)')
    MOVE(curState)
    print('Now curState is ',REPORT(curState))
    print('changeF(curState,SOUTH)')
    changeF(curState,'SOUTH')
    print('MOVE(curState)')
    MOVE(curState)
    print('Now curState is ',REPORT(curState))
    return

def UnitTest():
    testChangeF()
    testLeftAndRight()
    testMOVE() 
    print('******************************************************')
def ReadAndDo(curState):
    '''
    READ INPUT 
    '''
    InPut = input().split(' ')
    if(len(InPut)==0):
        return 1
    if(InPut[0] == 'PLACE'):
        ST = InPut[1].split(',')
        curState.pos[0] = int(ST[0])
        curState.pos[1] = int(ST[1])
        curState.F = StrToNum(ST[2])
        
    if(InPut[0] == 'MOVE'):
        MOVE(curState)
    elif(InPut[0] == 'EAST' or InPut[0] == 'WEST' or InPut[0] == 'NORTH' or InPut[0] == 'SOUTH'):
        changeF(curState,InPut[0])
    elif(InPut[0] == 'LEFT' or InPut[0] == 'RIGHT'):            
        leftAndRight(curState,InPut[0])
    elif(InPut[0] == 'REPORT'):
        print(REPORT(curState))
    return 1
UnitTest()

state = State(0,0,'NORTH')#state.x = 1 state.y = 2 state.F = EAST

while(ReadAndDo(state)):
    state.makeSure()
    
'''
TestDatas:
PLACE 1,2,EAST

MOVE

MOVE

REPORT

LEFT


MOVE

REPORT

RIGHT

MOVE

REPORT

WEST

MOVE

REPORT

EAST

MOVE

REPORT

NORTH

MOVE

REPORT

WEST

MOVE

REPORT

'''