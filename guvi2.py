class check:
    def __init__(self,num):
        self.num=num
    def checki(self):
        if self.num>-1:
            x=self.num%2
            if x==0:
                print('Even')
            elif x==1:
                print('Odd')
        else:
            print('invalid')

i=int(input())
i1=check(i)
i1.checki()