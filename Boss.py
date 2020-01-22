
class Boss:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.__Boss=[
                ' <>=======()                           ',
                '(/\___   /|\\          ()==========<>_ ',
                '      \_/ | \\        //|\   ______/ \)',
                '        \_|  \\      // | \_/          ',
                '          \|\/|\_   //  /\/            ',
                '           (oo)\ \_//  /               ',
                '          //_/\_\/ /  |                ',
                '         @@/  |=\  \  |                ',
                '              \_=\_ \ |                ',
                '                \==\ \|\_              ',
                '             __(\===\(  )\             ',
                '            (((~) __(_/   |            ',
                '                 (((~) \  /            ',
                '                 ______/ /             ',
                '                (-------/              '
        ]
    def create(self,tmp_grid):
        for i in range(0+self.y,15+self.y):
            for j in range(self.x,38+self.x):
                tmp_grid[i][j]=self.__Boss[i-self.y][j-self.x]
        return tmp_grid

    def updatePosition(self,position):
        if position<=31:
            self.y=position

class DragonBullets:
        def __init__(self,x,y):
            self.bullposx=x-8
            self.bullposy=y+3
            self.__BallBullets=[
                        '    oooo    ',
                        ' o        o ',
                        'o          o',
                        'o          o',
                        ' o        o ',
                        '    oooo    '
                        ]
            self.red= '\u001b[31;1m'
            self.reset='\u001b[0m'

        def create(self,tmp_grid):
            for i in range(self.bullposy,self.bullposy+6):
                for j in range(self.bullposx,self.bullposx+12):
                    tmp_grid[i][j]=self.red+ self.__BallBullets[i-self.bullposy][j-self.bullposx]+self.reset
            return tmp_grid

        def updateBullets(self):
            self.bullposx-=4
