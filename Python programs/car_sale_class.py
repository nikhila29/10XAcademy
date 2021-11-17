class CarSell:
    def __init__(self,customer_proposals):
        self.customer_proposals=customer_proposals
    def getPromisingCustomers(self):
        res=[]
        for i in range(len(self.customer_proposals)):
            if (self.customer_proposals[i]>=900000):
                res.append(i)
        if (len(res)==0):
            return([-1])
        return(res)
if __name__ == "__main__":
    num_customers = int(input())
    customer_proposals = []
    for i in range(num_customers):
        customer_proposals.append(int(input()))

    car_sell = CarSell(customer_proposals)
    for j in car_sell.getPromisingCustomers():
        print(j)

        