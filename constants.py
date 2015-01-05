import pygame
from pygame import *

GREY_TILE = "img/greyTile.png"
ORANGE_TILE = "img/orangeTile.png"
CROSSHAIR = "img/crosshair.png"
BG = "img/bg.png"

BLACK = (0,0,0)

BLOCKSIZE = 16

BUTTONWIDTH = 26
BUTTONHEIGHT = 16

DOORWIDTH = 16
DOORHEIGHT = 16*4

LOCKSIZE = 32

KEYWIDTH = 32
KEYHEIGHT = 20

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 30

STARWIDTH = 16
STARHEIGHT = 16

class MouseButton:
	#def __init__(self):
	LEFT = 1
	MIDDLE = 2
	RIGHT = 3
	WHEEL_UP = 4
	WHEEL_DOWN = 5