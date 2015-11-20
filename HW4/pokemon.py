import random

def status(m1,m2,hp1,hp2):
    print(m1,"has",hp1, "hit points remaining.")
    print(m2,"has",hp2, "hit points remaining.")

def move(name):
    print("Choose a move for %s."%(name))
    print("1. Tackle\n2. High Jump Kick\n3. Desperate Blow\n4. Slack Off")
    move=input("Enter your move: ")
    while move not in ['1','2','3','4']:
        print("Choose a move for %s."%(name))
        print("1. Tackle\n2. High Jump Kick\n3. Desperate Blow\n4. Slack Off")
        move=input("Enter your move: ")
    return int(move)

def check(Min,Max,Accu,crit,name,name2,skillname,hp):   
    if random.random()>Accu:
        print(name,"dodged the attack.")
        return 0
    else:
        strength=random.randint(Min,Max)
        if random.random()>crit:
            s=strength
        else:
            s=2*strength
            crit=1
        if hp-s<=0:
            s=hp
        print(name2,"hit",name,"with a",skillname,"dealing",s,"points of damage.")
        if crit==1:
            print('Critical Hit!')
        return s
    
def attack(skill,hp,name,name2):
    if skill==1:
        skillname="Tackle"
        Accu=0.9
        Min,Max=10,20
        crit=0.05
        
    elif skill==2:
        skillname="High Jump Kick"
        Accu=0.75
        Min,Max=25,30
        crit=0.05
    else:
        skillname="Desperate Blow"
        Accu=0.1
        Min,Max=50,60
        crit=0.05

    damage=check(Min,Max,Accu,crit,name,name2,skillname,hp)
    hp=hp-damage
    return hp
    
def heal(hp,name):   
    Accu=0.95
    crit=0.05
    if random.random()>Accu:
        print(name,"failed to heal itself.")
        return hp
    else:
        heal=random.randint(15,20)
        if random.random()>crit:
            s=heal 
        else:
            s=2*heal
            crit=1
        if hp==100:
            print(name,"failed to heal itself.")
        else:
            if hp+heal>=100:
                s=100-hp
                hp=100
            else:
                hp=hp+heal
            print(name,"Slacked Off, healing",s,"points of damage.")
            if crit==1:
                print('Critical Hit!')
        return hp

def main():
    monster_1=str(input("Enter the name for your monster: "))
    monster_2=str(input("Enter the name for your monster: "))
    seed=str(input("Enter a seed value: "))
    while not seed.isdigit() and not seed.lstrip('-').isdigit():
        seed=str(input("Enter a seed value: "))

    seed=random.seed(int(seed))
    start=random.randint(0,1)
    hp1=100
    hp2=100
    
    while hp1>0 and hp2>0:
        status(monster_1,monster_2,hp1,hp2,)
        if start==0:
            skill=move(monster_1)
            if skill<4:
                hp2=attack(skill,hp2,monster_2,monster_1)
            else:
                hp1=heal(hp1,monster_1)
        else:
            skill=move(monster_2)
            if skill<4:
                hp1=attack(skill,hp1,monster_1,monster_2)
            else:
                hp2=heal(hp2,monster_2)
        start=start^1
        
    if hp1==0:
        print(monster_2,"won the fight.")
    else:
        print(monster_1,"won the fight.")
main()
