class Movie:
    def __init__(self,length_in_minutes,num_characters,language):
        self.language=language
        self.num_characters=num_characters
        self.length_in_minutes=length_in_minutes
    
    def run(self):
        print ("This is a",self.language,"movie with",str(self.num_characters),"characters and is",str(length_in_minutes),"minutes long.")


language=input()
num_characters=int(input())
length_in_minutes=int(input())
obj=Movie(length_in_minutes,num_characters,language)
obj.run()

