class Bank_Account:
    def __init__(self,initial):
        self.balance=initial
    def debit(self,amount):
        self.balance-=amount
    def credit(self,amount):
        self.balance+=amount
obj=Bank_Account(0)
n=int(input())
while n>0:
    amount=int(input())
    if (amount>0):
        obj.credit(amount)
    else:
        obj.debit(-amount)
    n-=1
print(obj.balance)
        