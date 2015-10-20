def main():
    Money_To_Withdraw=eval(input("Please enter the amount of money you wish to withdraw: "))
    Hundreds= Money_To_Withdraw // 100
    Fifties= (Money_To_Withdraw % 100) //50
    Twenties= (Money_To_Withdraw-Hundreds*100-Fifties*50)//20
    Tens= (Money_To_Withdraw-Hundreds*100-Fifties*50-Twenties*20)//10
    Fives= (Money_To_Withdraw-Hundreds*100-Fifties*50-Twenties*20-Tens*10)//5
    Ones= Money_To_Withdraw-Hundreds*100-Fifties*50-Twenties*20-Tens*10-Fives*5

    print("%d hundreds. \n%d fifties.\n%d twenties.\n%d tens.\n%d fives.\n%d ones."%
          (Hundreds,Fifties,Twenties,Tens,Fives,Ones))

main()
