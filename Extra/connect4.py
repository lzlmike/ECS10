def construct_board():
    m=[['*' for x in range(8)] for y in range(7)]
    m[6][0]=" "
    for i in range(0,6):
        m[i][0]=5-i
    for i in range(1,8):
        m[6][i]=i-1
    return m

def print_board(m):
    for i in range(7):
        for j in range(8):
            print(m[i][j],end=" ")
        print()
    print()

def get_xinput(dic):
    a=input("X please enter a move: ")
    while(not a.isdigit() or int(a)>6 or int(a)<0 or dic[a]>=6):
        a=input("X please enter a move: ")
    print()
    return int(a)
    
def get_oinput(dic):
    a=input("O please enter a move: ")
    while(not a.isdigit() or int(a)>6 or int(a)<0 or dic[a]>=6):
        a=input("X please enter a move: ")
    print()
    return int(a)

def update_board(m,pos,dic,symbol):
    height=dic[str(pos)]
    m[5-height][pos+1]=symbol
    dic[str(pos)]+=1
    print_board(m)

def check_row(m):
    count=1
    for i in range(0,6):
        for j in range(1,8):
            if m[i][j-1]==m[i][j] and m[i][j]!='*':
                count+=1
                if count==4:
                    return True
            else:
                count=1
    return False

def check_col(m):
    count=1
    for j in range(1,8):
        for i in range(0,6):
            if m[i][j]==m[i+1][j] and m[i+1][j]!='*':
                count+=1
                if count==4:
                    return True
            else:
                count=1
    return False

def check_updia(m):
    count=1
    for i in range(0,3):
        for j in range(4,8):
            a,b=i,j
            count=1
            while(a<6 and b>=0):
                if m[a][b]==m[a+1][b-1] and m[a][b]!='*':
                    a,b=a+1,b-1
                    count+=1
                    if count==4:
                        return True
                else:
                    count=1
                    a,b=a+1,b-1
    return False

def check_downdia(m):
    count=1
    for i in range(0,3):
        for j in range(0,5):
            a,b=i,j
            count=1
            while(a<5 and b<7):
                if m[a][b]==m[a+1][b+1] and m[a][b]!='*':
                    a,b=a+1,b+1
                    count+=1
                    if count==4:
                        return True
                else:
                    count=1
                    a,b=a+1,b+1
    return False


def check(m):
    if check_row(m) or check_col(m) or check_updia(m) or check_downdia(m):
        return True
    return False

def tie_check(dic):
    s=0
    for i in dic:
        s+=dic[i]
    if s==42:
        return True
    return False

def main():
    board=construct_board()
    print_board(board)
    dic={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
    
    gameover=0
    xwin=0
    owin=0
    tie=0
    while(not gameover):
        x=get_xinput(dic)
        symbol='X'
        update_board(board,x,dic,symbol)
        if check(board):
            gameover=1
            xwin=1
            break

        o=get_oinput(dic)
        symbol='O'
        update_board(board,o,dic,symbol)
        if check(board):
            gameover=1
            owin=1
            break

        if tie_check(dic):
            gameover=1
            tie=1
            break
        
    if xwin==1:
        print("X won the game.")
    elif owin==1:
        print("O won the game.")
    else:
        print("The game ended in a tie.")
main()
