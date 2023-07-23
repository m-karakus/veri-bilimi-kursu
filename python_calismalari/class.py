class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == 'actor':
            print(self.name,"shoots a film")
        elif self.occupation == 'tennis player':
            print(self.name,"play tennis")
    
    def speaks(self):
        print(self.name,"says: how are you?")

tom = Human("com truise", "actor")
tom.do_work()
tom.speaks()
