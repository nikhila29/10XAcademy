class Input_reader:
    def __init__(self):
        self.data=[]
    @staticmethod
    def printer(index, val):
        print(str(index) + " " + str(val))
        return
    def read_strings(self,n):
        while n>0:
            self.data.append(input())
            n-=1
    def read_integer(self,n):
        while n>0:
            self.data.append(int(input()))
            n-=1
    def read_float(self,n):
        while n>0:
            self.print('%d %.2f' % (i, float(self.inputList[i])))
            n-=1
temp=Input_reader()
n=int(input())
ins=input()
if ins=="string":
    temp.read_strings(n)
elif ins=="integer":
    temp.read_integer(n)
elif ins=="float":
    temp.read_float(n)
for i in range(len(temp.data)):
    temp.printer(i,temp.data[i])