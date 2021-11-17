class Movie:
    def __init__(self,lang,char,length):
        self.lang=lang
        self.char=char
        self.length=length
    @staticmethod
    def certify(length,char):
        if length<=240 and char>=2:
            return True
        return False
    def run(self,status):
        print("This is a "+self.lang+" movie with "+str(self.char)+ " characters, is "+str(self.length)+" minutes long, and is "+status+".")
movie=Movie(input(),int(input()),int(input()))
cert=None
if (movie.certify(movie.length,movie.char)):
    cert="certified"
else:
    cert="not certified"
movie.run(cert)
