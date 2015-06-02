import pygame
from pygame import *

GREY_TILE = "img/greyTile.png"
ORANGE_TILE = "img/orangeTile.png"
CROSSHAIR = "img/crosshair.png"
BG = "img/bg.png"

BLACK = (0,0,0)

class ASSET:
    player = "player"
    block = "block"
    box = "box"
    lock = "lock"
    key = "key"
    platform_h = "platform_h"
    platform_v = "platform_v"
    star = "star"
    button_blue = "button_blue"
    button_red = "button_red"
    button_green = "button_green"
    door_blue = "door_blue"
    door_red = "door_red"
    door_green = "door_green"
    platform_block = "platform_block"
    platformv_block = "platformv_block"



class BLOCK:
    width = 32
    height = 32
    size = (32, 32)

class BUTTON:
    width = 52
    height = 32


class DOOR:
    width = 32
    height = 32*4

class LOCK:
    width = 64
    height = 64

class KEY:
    width = 64
    height = 64

class PLAYER:
    width = 50
    height = 60
    spritesheet = pygame.image.load("img/player.png")

class STAR:
    width = 32
    height = 32

class MouseButton:
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3
    WHEEL_UP = 4
    WHEEL_DOWN = 5