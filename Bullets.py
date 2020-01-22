class Bullets:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def checking(self):
        if self.x >= 1492:
            return True
