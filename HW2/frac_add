def isnot_int(s):
    try:
        int(s)
        return False
    except ValueError:
        return True


def main():
    First=str(input("Please enter a fraction: "))
    Second=str(input("Pleaes enter another fraction: "))

    if not(isnot_int(First)):
        First=First+'/1'
    if not(isnot_int(Second)):
        Second=Second+'/1'

    if '/' not in First:
        print("%s is not a valid fraction. Ending program."%First)
        exit(0)
    if '/' not in Second:
        print("%s is not a valid fraction. Ending program."%Second)
        exit(0)
        
    first=First.split("/")
    first=first[0].split()+['/']+first[1].split()
    second=Second.split("/")
    second=second[0].split()+['/']+second[1].split()

    if len(first)!=3 or first[1]!='/' or not(first[2].isdigit()) or isnot_int(first[0]):
        print("%s is not a valid fraction. Ending program."%First)
        exit(0)
    elif len(second)!=3 or second[1]!='/' or not(second[2].isdigit())or isnot_int(second[0]):
        print("%s is not a valid fraction. Ending program."%Second)
        exit(0)

    result=''
    if int(first[2])==int(second[2]):
        top=int(first[0])+int(second[0])
        result=str(top)+'/'+first[2]
    else:
        top=int(first[0])*int(second[2])+int(second[0])*int(first[2])
        bot=int(first[2])*int(second[2])
        result=str(top)+'/'+str(bot)

    num1=''.join(first)
    num2=''.join(second)

    print(num1+' + '+num2+' = '+result)
main()
