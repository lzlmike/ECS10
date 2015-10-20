def main():
    year=eval(input("Please enter a year: "))
    leap=0
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=1
            else:
                leap=0
        else:
            leap=1
    else:
        leap=0

    if leap==1:
        print("%.d is a leap year."%(year))
    else:
        print("%.d is not a leap year."%(year))

main()
