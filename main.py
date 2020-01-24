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
        self.__getch = getInput._getChUnix()
        super().__init__()
        self._play=Scenary()
        self.__boostcount=0
        self.__boostpress=False
        self.__green='\u001b[32;1m'
        self.__reset= '\u001b[0m'
        self.__yellow  = '\u001b[33;1m'
        self.__timecounter=0

    def run(self):
        def alarmhandler(signum, frame):
            raise AlarmException
        def getinp(timeout=0.09):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                ch = self.__getch()
                signal.alarm(0)
                return ch
            except AlarmException:
                pass
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return ''
        self._play.prior()
        while True:
            self._play.timing=time.time()
            os.system("tput reset")
            print(self.__green)
            print("score",self._play.score,"           ","Boost Value"," ",end=" ")
            speed(self.__boostcount)
            print("         ",end='  ')
            print("Time Remaining",self._play.time,"               ",end=" ")

            print(self.__reset,end=' ')
            self._play.check()
            self._play.checkCollisions()
            self._play.background()
            self._play.shh=False
            if self.__boostcount==600:
                self.__boostcount=0
                self.__boostpress=False
            key=getinp()
            if key=='d':
                self._play.Right=True
            elif key=='w':
                self._play.Up=True
            elif key=='b':
                self._play.fired=True
                self._play.bullets=True
            elif key=='a':
                self._play.left=True
            elif key=='s':
                self._play.speedBoost=True
            elif key==' ':
                if self.__boostcount==0:
                    self._play.shh=True
                self.__boostpress=True
            elif key=='q' or key=='Q':
                os.system('clear')
                print(self.__green)
                print("                          Game Exited                             ")
                print(self.__reset)
                sys.exit()
            if self.__boostpress:
                self.__boostcount+=1
            self.__timecounter+=1
            if self.__timecounter%4==0:
                self._play.time-=time.time()-self._play.timing
                self._play.time=int(self._play.time)
            if self._play.time==0:
                os.system("clear")
                print(self.__yellow)
                print("                             TIME UP                               ")
                print(self.__reset)
                sys.exit()

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
