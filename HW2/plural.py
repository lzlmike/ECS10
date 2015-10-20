def vowel(x):
    v='aeiou'
    return x in v

def main():
    old_world=str(input("Please enter a word: "))
    word=old_world
    if word[-2:]=='ch' or word[-2:]=='sh' or word[-1]=='s' or word[-1]=='x' or word[-1]=='z':
        word=word+'es'
    elif vowel(word[-2:-1]) and word[-1]=='y':
        word=word+'s'
    elif (not vowel(word[-2:-1])) and word[-1]=='y':
        word=word[0:-1]+'ies'
    elif word[-1]=='f':
        word=word[0:-1]+'ves'
    elif word[-2:]=='fe':
        word=word[0:-2]+'ves'
    else:
        word=word+'s'

    print("The plural form of %s is %s."%(old_world,word))

main()
