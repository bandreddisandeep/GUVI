class check:
    def __init__(self,st):
        self.st=st
    def checki(self):
        if self.st in ['a','e','i','o','u']:
            print('Vowel')
        elif self.st in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            print('Consonant')
        else:
            print('invalid')
x=input() 
x=x.lower()
i=check(x)
i.checki()