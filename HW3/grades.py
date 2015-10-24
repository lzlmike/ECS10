def get_input():
    print("1. Add/modify student grade")
    print("2. Delete student grade")
    print("3. Print student grades")
    print("4. Display the course statistics")
    print("5. Quit")
    cho=str(input("Your choice: "))
    while(not cho.isdigit() or int(cho)>5 or int(cho)<1 ):
        print("Unrecognized command.")
        print("1. Add/modify student grade")
        print("2. Delete student grade")
        print("3. Print student grades")
        print("4. Display the course statistics")
        print("5. Quit")
        cho=str(input("Your choice: "))
    return int(cho)

def add_grade(dic):
    n=str(input("Enter name and points (Ex. 'Bob 95'): "))
    n_list=n.split()
    dic[n_list[0]]=n_list[1]
    
def remove(dic):
    n=str(input("Enter a name to be removed (Ex. Bob): "))
    if n in dic:
        dic.pop(n)

def display(dic):
    print("-----Displaying Grades-----\n")
    for i in sorted(dic):
        print(i+'    : '+str(dic[i]))
    print("-----Done Displaying Grades-----")
        
def statistics(dic):
    grade=[]
    dic_mode={}
    for i in dic:
        grade.append(int(dic[i]))
        
    grade.sort()
    mode=grade[0]
    max_grade=0
    
    for i in grade:
        if i in dic_mode:
            dic_mode[i]+=1
            if dic_mode[i]>max_grade:
                mode=i
                max_grade=dic_mode[i]
        else:
            dic_mode[i]=1
        
        
    median=grade[(len(grade))//2]
    mean=sum(grade)/len(grade)
    
    print("-----Displaying Statistics-----\n")
    print("Mean : %.2f"%mean+'\n')
    print("Median : "+str(median)+'\n')
    print("Mode : "+str(mode)+'\n')
    print("-----Done Displaying Statistics-----\n")
    
    
    
def main():
    choice=get_input()
    student_grade={}
    while(choice!=5):
        if choice==1:
            add_grade(student_grade)
            choice=get_input()
        elif choice==2:
            remove(student_grade)
            choice=get_input()
        elif choice==3:
            display(student_grade)
            choice=get_input()
        elif choice==4:
            statistics(student_grade)
            choice=get_input()
    
main()
