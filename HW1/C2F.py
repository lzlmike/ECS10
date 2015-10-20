def main():
    Temp_In_Cel=eval(input("Please enter the temperature in Celsius: "))
    Temp_In_Fahrenheit=9/5 * Temp_In_Cel + 32
    print("%.2f Celsius is %.2f Fahrenheit."%(Temp_In_Cel,Temp_In_Fahrenheit))

main()
