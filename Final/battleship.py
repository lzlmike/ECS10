import random
import sys

def initialize_board(w,h):
    m=[['*' for x in range(w+1)] for y in range(h+1)]
    m[0][0]=" "
    for i in range(1,w+1):
        m[0][i]=i-1
    for j in range(1,h+1):
        m[j][0]=j-1
    return m

def init_board(m,x1,y1,x2,y2,symbol,data1):
    if x1>=len(m) or x2>=len(m) or y1>=len(m[0]) or y2>=len(m[0]) or x1<0 or x2<0 or y1<0 or y2<0:
        print("Error %s is placed outside of the board. Terminating game."%(symbol))
        sys.exit()
    elif (not x1==x2) and (not y1==y2):
        print("Ships cannot be placed diagonally. Terminating game.")
        sys.exit()
    elif symbol in data1:
        print("Error symbol %s is already in use. Terminating game"%(symbol))
        sys.exit()
    elif x1==x2:
        a=min(y1,y2)
        b=max(y1,y2)
        for i in range(a,b+1):
            if m[x1+1][i+1]!='*':
                print("There is already a ship at location %d, %d. Terminating game."%(x1,i))
                sys.exit()
            else:
                m[x1+1][i+1]=symbol
    elif y1==y2:
        a=min(x1,x2)
        b=max(x1,x2)
        for i in range(a,b+1):
            if m[i+1][y1+1]!='*':
                print("There is already a ship at location %d, %d. Terminating game."%(i,y2))
                sys.exit()
            else:
                m[i+1][y1+1]=symbol

def print_board(m):
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            print(m[i][j],end=" ")
        print()

def ai_init(m,ships):
    a=[]
    for s in sorted(ships):
        ship=s.split(" ")
        length=abs(int(ship[3])-int(ship[1]))+abs(int(ship[4])-int(ship[2]))+1
        symbol=ship[0]
        overlap=1
        while(overlap==1):
            overlap=0
            dirc=random.choice(['vert','horz'])
            if dirc=="vert":
                x_max=len(m)-length
                x=random.randint(1,x_max)
                y=random.randint(1,len(m[0])-1)
                #print(x,y,length)
                for i in range(x,x+length):
                    if m[i][y]!='*':
                        overlap=1
                        break
                if overlap==0:
                    for i in range(x,x+length):
                        m[i][y]=symbol
                    a.append("%s %d %d %d %d"%(symbol,x-1,y-1,x+length-2,y-1))
            else:
                y_max=len(m[0])-length
                x=random.randint(1,len(m)-1)
                y=random.randint(1,y_max)
                for i in range(y,y+length):
                    if m[x][i]!='*':
                        overlap=1
                        break
                if overlap==0:
                    for i in range(y,y+length):
                        m[x][i]=symbol
                    a.append("%s %d %d %d %d"%(symbol,x-1,y-1,x-1,y+length-2))

    return (m,a)

def create_list(m):
    A=[]
    for i in range(0,len(m)-1):
        for j in range(0,len(m[0])-1):
            A.append((i,j))
    return A
        
def check(m,ai_fire,data):
    symbol=m[ai_fire[0]+1][ai_fire[1]+1]
    if symbol!='*'and symbol!='X' and symbol!='O':
        data[symbol]-=1
        if data[symbol]==0:
            print("You sunk my %s"%(symbol))
            return 2
        else:
            return True
    else:
        return False

def update_board(board,hit,ai_fire):
    if(hit==True):
        board[ai_fire[0]+1][ai_fire[1]+1]='X'
        print("Hit!")
    elif hit==2:
        board[ai_fire[0]+1][ai_fire[1]+1]='X'
    else:
        board[ai_fire[0]+1][ai_fire[1]+1]='O'
        print("Miss!")

def display(temp,board):
    print("Scanning Board")
    print_board(temp)
    print("\nMy Board")
    print_board(board)
    print("\n")

def myturn(m):
    while True:
        xy = input("Enter row and column to fire on separated by a space: ").split(" ")
        if len(xy) < 2 or not xy[0].isdigit() or not xy[1].isdigit() or int(xy[0]) > len(m) - 2 or int(xy[1]) > len(
            m[0]) - 2:
            continue
        else:
            break

    a=(int(xy[0]),int(xy[1]))
    return a

def over(data):
    sum=0
    for i in data:
        sum+=data[i]
    if sum==0:
        return True
    else:
        return False

def cheat_list(m):
    A=[]
    for i in range(1,len(m)):
        for j in range(1,len(m[0])):
            if m[i][j]!='*':
                A.append((i-1,j-1))
    return A

    
def con_list(m,ai_fire,temp):
    x,y=ai_fire[0],ai_fire[1]
    if (not(x-1,y)in temp) and x-1>=0 and y>=0 and x<len(m) and y+1<len(m[0]) and m[x][y+1]!='X' and m[x][y+1]!='O':
        temp.append((x-1,y))
    if (not(x+1,y)in temp) and x+1>=0 and y>=0 and x+2<len(m) and y+1<len(m[0]) and m[x+2][y+1]!='X'and m[x+2][y+1]!='O':
        temp.append((x+1,y))
    if (not(x,y-1)in temp) and x>=0 and y-1>=0 and x+1<len(m) and y<len(m[0]) and m[x+1][y]!='X'and m[x+1][y]!='O':
        temp.append((x,y-1))
    if (not(x,y+1)in temp) and x>=0 and y+1>=0 and x+1<len(m) and y+2<len(m[0]) and m[x+1][y+2]!='X' and m[x+1][y+2]!='O':
        temp.append((x,y+1))
    return temp

def play(aiboard,board,turn,ai,temp,data1,data2):
    if ai==1:
        ai_target=create_list(board)
        gameover=0
        mewin=0
        aiwin=0
        if turn==1:
            ai_fire=random.choice(ai_target)
            print("The AI fires at location ",ai_fire)
            hit=check(board,ai_fire,data1)
            ai_target.remove(ai_fire)
            update_board(board,hit,ai_fire)
            if(over(data1)):
                    aiwin,gameover=1,1
        while(gameover==0):
            display(temp,board)
            my_fire=myturn(board)
            hit=check(aiboard,my_fire,data2)
            update_board(temp,hit,my_fire)
            if(over(data2)):
                mewin,gameover=1,1
                break
            
            ai_fire=random.choice(ai_target)
            print("The AI fires at location ",ai_fire)
            hit=check(board,ai_fire,data1)
            ai_target.remove(ai_fire)
            update_board(board,hit,ai_fire)
            if(over(data1)):
                aiwin,gameover=1,1

        display(temp,board)
        if mewin==1:
            print("You win!")
        else:
            print("The AI wins.")
    if ai==2:
        ai_target=create_list(board)
        gameover=0
        mewin=0
        aiwin=0
        mode=0
        aitemp=[]
        if turn ==1:
            ai_fire=random.choice(ai_target)
            print("The AI fires at location ",ai_fire)
            hit=check(board,ai_fire,data1)
            ai_target.remove(ai_fire)
            update_board(board,hit,ai_fire)
            if(over(data1)):
                    aiwin,gameover=1,1
            if hit:
                mode=1
                aitemp=con_list(board,ai_fire,aitemp)
                
        while(gameover==0):
            display(temp,board)
            my_fire=myturn(board)
            hit=check(aiboard,my_fire,data2)
            update_board(temp,hit,my_fire)
            if(over(data2)):
                mewin,gameover=1,1
                break
            if mode==0:
                ai_fire=random.choice(ai_target)
                print("The AI fires at location ",ai_fire)
                hit=check(board,ai_fire,data1)
                ai_target.remove(ai_fire)
                update_board(board,hit,ai_fire)
                if(over(data1)):
                    aiwin,gameover=1,1
                if hit:
                    mode=1
                    aitemp=con_list(board,ai_fire,aitemp)
            else:
                ai_fire=aitemp[0]
                print("The AI fires at location ",ai_fire)
                hit=check(board,ai_fire,data1)
                ai_target.remove(ai_fire)
                aitemp.remove(ai_fire)
                update_board(board,hit,ai_fire)
                if(over(data1)):
                    aiwin,gameover=1,1
                if hit:
                    mode=1
                    aitemp=con_list(board,ai_fire,aitemp)
                if len(aitemp)==0:
                    mode=0
                
        display(temp,board)
        if mewin==1:
            print("You win!")
        else:
            print("The AI wins.")
        

    if ai==3:
        gameover=0
        mewin=0
        aiwin=0
        ai_target=cheat_list(board)
        if turn==1:
            ai_fire=ai_target[0]
            print("The AI fires at location ",ai_fire)
            hit=check(board,ai_fire,data1)
            ai_target.remove(ai_fire)
            update_board(board,hit,ai_fire)
            if(over(data1)):
                    aiwin,gameover=1,1
        while(gameover==0):
            display(temp,board)
            my_fire=myturn(board)
            hit=check(aiboard,my_fire,data2)
            update_board(temp,hit,my_fire)
            if(over(data2)):
                mewin,gameover=1,1
                break
            
            ai_fire=ai_target[0]
            print("The AI fires at location ",ai_fire)
            hit=check(board,ai_fire,data1)
            ai_target.remove(ai_fire)
            update_board(board,hit,ai_fire)
            if(over(data1)):
                aiwin,gameover=1,1

        display(temp,board)
        if mewin==1:
            print("You win!")
        else:
            print("The AI wins.")
        
        
    
def main():
    seed=str(input("Enter the seed: "))
    while not seed.isdigit() and not seed.lstrip('-').isdigit():
        seed=str(input("Enter the seed: "))

    width=str(input("Enter the width of the board: "))
    while not width.isdigit() or not width.lstrip('-').isdigit():
        width=str(input("Enter the width of the board: "))

    height=str(input("Enter the height of the board: "))
    while not height.isdigit() or not height.lstrip('-').isdigit():
        height=str(input("Enter the height of the board: "))

    seed=random.seed(int(seed))
    height=int(height)
    width=int(width)

    board=initialize_board(width,height)
    aiboard=initialize_board(width,height)
    temp=initialize_board(width,height)
    
    filename=input("Enter the name of the file containing your ship placements: ")
    
    print("Choose your AI.\n1. Random\n2. Smart\n3. Cheater")
    ai=input(" Your choice: ")
    while ai not in ['1','2','3']:
        ai=input("Choose your AI.\n1. Random\n2. Smart\n3. Cheater\n Your choice: ")
    ai=int(ai)

    all_ship=[]
    data1={}
    data2={}
    with open(filename) as ships:
        for ship in ships:
            ship_list=ship.split(" ")
            symbol=ship_list[0]
            x1,y1=int(ship_list[1]),int(ship_list[2])
            x2,y2=int(ship_list[3]),int(ship_list[4])
            init_board(board,x1,y1,x2,y2,symbol,data1)
            all_ship.append(ship)
            data1[symbol]=abs(x2-x1)+abs(y2-y1)+1
            data2[symbol]=abs(x2-x1)+abs(y2-y1)+1

 
    temp2=ai_init(aiboard,all_ship)
    aiboard=temp2[0]
    
    for s in temp2[1]:
        line=s.split(" ")
        x1,y1=int(line[1]),int(line[2])
        x2,y2=int(line[3]),int(line[4])
        print("Placing ship from %d,%d to %d,%d."%(x1,y1,x2,y2))
    turn=random.randint(0,1)
    play(aiboard,board,turn,ai,temp,data1,data2)
    
main()
