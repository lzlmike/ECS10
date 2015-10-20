def main():
    First=str(input("Please enter the student's first name: "))
    Last=str(input("\nPlease enter the student's last name:"))
    Date=str(input("\nPlease enter the student's enrollment date:"))
    First_name=""
    Last_name=""
    
    if(len(First)>=10):
        First_name=First[0:10]
    else:
        First_name=First+"-"*(10-len(First))

    if(len(Last)>=10):
        Last_name=Last[0:10]
    else:
        Last_name=Last+"-"*(10-len(Last))

    
    d=Date.split()
    Month={"January":"01","February":"02","March":"03","April":"04","May":"05",
           "June":"06","July":"07","August":"08","September":"09","October":"10",
           "November":"11","December":"12"}
    if len(d[1])==2:
        day='0'+d[1][0]
    else:
        day=d[1][0:2]
    date=Month[d[0]]+'/'+day+'/'+d[2][2:]
    print("\nStoring: "+Last_name+First_name+date)

main()
