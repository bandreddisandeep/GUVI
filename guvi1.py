class check:
    def __init__(self,num):
        self.num=num
    def checki(self):
        if(self.num)<0:
            print('Negative')
        elif(self.num)>0:
            print('Positive')
        else:
            print('Zero')

i=int(input())
i1=check(i)
i1.checki()