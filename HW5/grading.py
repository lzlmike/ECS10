import os

def read_homework(name,dic):
    file_cont=name.readlines();
    percent_total=int(file_cont[0].split(",")[1])
    max_point=int(file_cont[1].split(",")[1])
    for student in file_cont[4:]:
        s_name=student.split(",")[0]+" "+student.split(",")[1]
        if s_name in dic:
            dic[s_name]=dic[s_name]+int(student.split(",")[2])*percent_total/max_point
        else:
            dic[s_name]=int(student.split(",")[2])*percent_total/max_point
    return dic

def mean(dic):
    count=0
    total=0
    for i in dic:
        count+=1
        total+=dic[i]
    return total/count
        
def median(dic):
    a=[]
    count=0
    for i in dic:
        count+=1
        a.append(dic[i])
    return sorted(a)[count//2]
        
def mode(dic):
    a=[]
    for i in dic:
        a.append(dic[i])
    return max(set(a),key=a.count)
    
def std_dev(dic,mean):
    count=0
    s=0
    for i in dic:
        s+=(dic[i]-mean)**2
        count+=1
    return (s/count)**0.5

def percent2Letter(per):
    if per>=90:
        return 'A'
    elif per>=80 and per<90:
        return 'B'
    elif per>=70 and per<80:
        return 'C'
    elif per>=60 and per<70:
        return 'D'
    else:
        return 'F'
    
def display_statistics(Mean,Median,Mode,sd):
    print("Mean | Median | Mode | Standard Deviation")
    print("%.2f | %.2f | %.2f | %.2f"%(Mean,Median,Mode,sd))

def display_grades(dic):
    print("Last Name | First Name | Percent | Letter")
    for i in sorted(dic):
        last=i.split(" ")[0]
        first=i.split(" ")[1]
        print("%s | %s | %.2f | %s"%(last,first,dic[i],percent2Letter(dic[i])))
    
def grading():
    filedir=input("Please enter the name of the directory containing the homeworks: ")
    files=os.listdir(filedir)
    dic={}
    for file in files:
        with open(os.path.join(filedir,file)) as csv_file:
            dic=read_homework(csv_file,dic)
    Mean=mean(dic)
    Median=median(dic)
    Mode=mode(dic)
    sd=std_dev(dic,Mean)
    display_statistics(Mean,Median,Mode,sd)
    display_grades(dic)

grading()
