def prime(k):
    if k%2==0:
        return False
    for i in range(3,k//2+2):
        if k%i==0:
            return False
    return True

def main():
    num=str(input("Please enter an integer >= 2: "))
    while(not num.isdigit()) or int(num)<2:
        num=str(input("Please enter an integer >= 2: ")) 
    for i in range(2,int(num)+1):
        if i==2:
            print(2)
        elif prime(i):
            print(i)
        
main()
