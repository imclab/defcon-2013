'''
racinggame.py

u - player
~ - snake/crash
T - tree/crash
P - person/crash
Z - zebra/crash
r - rock/crash
c - car/crash
X - road block/ crash
| - wall/crash - restrict movement to the 5 positions between the walls

At any give time it needs to be able to predict 5 steps ahead.
Needs to be moving forward at every step.
Avoid all objects in front of you between the walls.

Starting screen:

|-----|
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|  u  |
|-----|

'''

import random
import math
import socket

def moveForward(s):
    s.send("\n")

def moveLeft(s):
    s.send("l\n")

def moveRight(s):
    s.send("r\n")

def startGame(s):

def eval()


def parseTrack(s):
	trackList = []
	num = 0
	lines = s.recv(1024).split('\n')
	print lines
	i = 0

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("grandprix.shallweplayaga.me", 2038))
    s.send("\n")

if __name__ == "__main__":
    main()