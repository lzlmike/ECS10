def cipher(sen,number):
    new=[]
    for i in range(0,len(sen)):
        if(sen[i].isalpha()):
            if ord(sen[i])+number>122:
                a=chr(ord(sen[i])+number-26)
            elif ord(sen[i])>=97 and ord(sen[i])<=122:
                a=chr((ord(sen[i])+number-97)%26+97)

            elif ord(sen[i])>=65 and ord(sen[i])<=90:
                a=chr((ord(sen[i])+number-65)%26+65)
        else:
            a=sen[i]
            
        new.append(a)
        
    s=''.join(new)
    return s

def main():
    sentence=str(input("Please enter a string to be ciphered: "))
    num=str(input("Please enter a shift amount between 0 and 25: "))
    while (not num.isdigit()) or int(num)>25 or int(num)<0:
        num=str(input("Please enter a shift amount between 0 and 25: "))

    print(cipher(sentence,int(num)))
main()
