import random
def game(comp,you):
    if comp==you:
        print("the match is tie") 
    elif comp=='s':
        if you=='r':
            return True
        else:
            return False
    elif comp=='r':
        if you=='p':
            return True
        else:
            return False 
    elif comp=='p':
        if you=='s':
            return True
        else:
            return False
a=random.randint(1,3)
if a==1:
    comp='r'
elif a==2:
    comp='p'
else:
    comp='s'
you=input('Enter rock(r),paper(p) or scissor(s)') 
b=game(comp,you)    
print(f'Computer entered: {comp}')
print(f'You entered: {you}')
if b==True:
    print('You have won')
elif b==False:
    print('You have lost')
else:
    print('The match is tie')     

