
### Define the required class here...
class Flight:
    def __init__(self, upTime, downTime):
        self.upTime = upTime
        self.downTime = downTime

    def calculateFlight(self):
        # Your Code goes here
        ut=int(self.upTime[:2])*60+int(self.upTime[3:])
        dt=int(self.downTime[:2])*60+int(self.downTime[3:])
        flying_time=abs(dt-ut)
        return flying_time

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    t1 = input()
    t2 = input()

    f1 = Flight(t1, t2)
    print(f1.calculateFlight())