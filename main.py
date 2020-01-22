import time
import os
import sys
from alarmexception import AlarmException
import signal
import getInput
from scenary import Scenary
from player import Player

class Engine(Scenary,Player):
    def __init__(self):
        self.getch = getInput._getChUnix()
        super().__init__()
        self.play=Scenary()
        self.__boostcount=0
        self.boostpress=False
        self.green='\u001b[32;1m'
        self.reset= '\u001b[0m'
        self.yellow     = '\u001b[33;1m'


    def run(self):
        def alarmhandler(signum, frame):
            raise AlarmException
        def getinp(timeout=0.09):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                ch = self.getch()
                signal.alarm(0)
                return ch
            except AlarmException:
                pass
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return ''
        self.play.prior()
        while True:
            os.system("tput reset")
            print(self.green)
            print("score",self.play.score,"       ","Boost Value"," ",end=" ")
            print(self.reset,end=' ')
            speed(self.__boostcount)
            print("")
            print("")
            self.play.check()
            self.play.checkCollisions()
            self.play.background()
            self.play.shh=False
            if self.__boostcount==600:
                self.__boostcount=0
                self.boostpress=False
            key=getinp()
            if key=='d':
                self.play.Right=True
            elif key=='w':
                self.play.Up=True
            elif key=='b':
                self.play.fired=True
                self.play.bullets=True
            elif key=='a':
                self.play.left=True
            elif key=='s':
                self.play.speedBoost=True
            elif key==' ':
                if self.__boostcount==0:
                    self.play.shh=True
                self.boostpress=True
            elif key=='q':
                os.system('clear')
                print("Game Exited")
                sys.exit()
            if self.boostpress:
                self.__boostcount+=1

def speed(boostcount):
    if boostcount>=100 and boostcount<200:
        for x in range(0,1):
            print(  "|",end='')
    elif boostcount>=200 and boostcount<300:
        for x in range(0,2):
            print("|",end='')
    elif boostcount>=300 and boostcount<400:
        for x in range(0,3):
            print("|",end='')
    elif boostcount>=400 and boostcount<500:
        for x in range(0,4):
            print("|",end='')
    elif (boostcount>=500 and boostcount<=600) or boostcount==0:
        for x in range(0,5):
            print("|",end='')
