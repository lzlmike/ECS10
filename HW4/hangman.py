
def guess(guessed,word_display):
    print(word_display)
    print("So far you have guessed: ",end='')
    temp=sorted(guessed)
    if len(temp)==0:
        print(end='')
    elif len(guessed)==1:
        print(guessed[0],end='')
    else:
        for i in range(0,len(temp)-1):
            print(temp[i]+', ',end='')
        print(temp[-1],end='')

    print()
    char=str(input("Please enter your next guess: "))
    char=char.lower().replace(" ",'')
    
    while(len(char)!=1 or char in guessed or char==''):
        if char=='':
            print("You must enter a guess.")
            char=str(input("Please enter your next guess: "))
        elif len(char)>1:
            print("You can only guess a single character.")
            char=str(input("Please enter your next guess: "))
        elif char in guessed:
            print("You already guessed the character: ",char)
            char=str(input("Please enter your next guess: "))
        char=char.lower().replace(" ",'')
        
    return char

def check(char,word,guessed,correct,real_word,word_display):
    new=word_display
    guessed.append(char)
    if char in word:
        correct.append(char)
        if sorted(correct)==real_word:
            print("You correctly guessed the secret word: ",word)
            exit()
        new=construct(word,correct)

    return new

def construct(word,correct):
    temp=[]
    for i in word:
        if i in correct:
            temp.append(i)
        else:
            temp.append('?')
    return ''.join(temp)
    
        
def draw(count):
    print
    if count==1 :
        print(" |")
    elif count==2:
        print(" |\n 0")
    elif count==3 :
        print(" |\n 0\n |")
    elif count==4:
        print(" |\n 0\n/|")
    elif count==5:
        print(" |\n 0\n/|\ ")
    elif count==6:
        print(" |\n 0\n/|\ \n/ ")
    elif count==7 :
        print(" |\n 0 \n/|\ \n/ \ ")
    else:
        print("\n")


def main():
    word=str(input("Please enter a word to be guessed \nthat does not contain ? or white space: "))
    while('?'in word or ' 'in word):
        word=str(input("Please enter a word to be guessed \nthat does not contain ? or white space: "))
    print('\n'*30)

    word=word.lower()
    count=0
    l=len(word)
    word_display='?'*l
    guessed=[]
    correct=[]
    real_word=sorted(list(set(word)))
    while(count-len(correct)<7):
        char=guess(guessed,word_display)
        word_display=check(char,word,guessed,correct,real_word,word_display)
        count+=1
        print()
        draw(count-len(correct))
        print()

    print("You failed to guess the secret word: ",word)
        
main()
