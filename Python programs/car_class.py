class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model

if __name__ == '__main__':
    
    flag = int(input())
    if flag == 1:
        input_string = input().split()
        p1 = Car(input_string[0], input_string[1])
    else:
        p1 = Car("Audi","A4")

    print(p1.name)
    print(p1.model)