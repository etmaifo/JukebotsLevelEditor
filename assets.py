import pygame
from constants import *
from block import *

class Asset(pygame.sprite.Sprite):
	def __init__(self, x=0, y=0):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("img/block_blue.png")
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

		self.type = "player"
		self.color_code = "blue"
		self.pos = [0, 0]

		self.group = pygame.sprite.Group()


	def get_image(self, x, y, width, height, spritesheet):
		image = pygame.Surface((width, height))#.convert()
		image.blit(spritesheet, (0, 0), (x, y, width, height))
		image.set_colorkey(BLACK)

		return image


	def update(self):
		self.group.update()

		x = self.rect.x
		y = self.rect.y
		spritesheet = ""
		if self.type == "player":
			#spritesheet = pygame.image.load("img/player.png")
			self.image = self.get_image(150, 0, 50, 61, PLAYER.spritesheet)
			self.image = pygame.transform.smoothscale(self.image, (PLAYER.width, PLAYER.height))
			self.rect = self.image.get_rect()

		elif self.type == "block":
			#self.image = pygame.image.load("img/block_%s.png" %self.color_code)
			self.image = pygame.image.load("img/block_blue.png")
			self.image = pygame.transform.smoothscale(self.image, (BLOCK.width, BLOCK.height))
			self.rect = self.image.get_rect()

		elif self.type == "box":
			self.image = pygame.image.load("img/box.png")
			self.rect = self.image.get_rect()

		elif self.type =="platform_h":
			self.image = pygame.image.load("img/platformh.png")
			self.rect = self.image.get_rect()
			self.image = pygame.transform.smoothscale(self.image, (self.rect.width*2, BLOCK.height))
			self.rect = self.image.get_rect()

		elif self.type == "platform_v":
			self.image = pygame.image.load("img/platformv.png")
			self.rect = self.image.get_rect()
			self.image = pygame.transform.smoothscale(self.image, (self.rect.width*2, self.rect.height*2))
			self.rect = self.image.get_rect()

		elif self.type == "platform_block":
			self.image = pygame.image.load("img/platform_block.png")
			self.image = pygame.transform.smoothscale(self.image, (BLOCK.width, BLOCK.height))
			self.rect = self.image.get_rect()

		elif self.type == "platformv_block":
			self.image = pygame.image.load("img/platformv_block.png")
			#self.image = pygame.transform.smoothscale(self.image, (BLOCKSIZE, BLOCKSIZE))
			self.rect = self.image.get_rect()			

		elif self.type == "button_blue":
			self.image = pygame.image.load("img/button_blue.png")
			self.image = pygame.transform.smoothscale(self.image, (BUTTON.width, BUTTON.height))
			self.rect = self.image.get_rect()
	
		elif self.type == "button_red":
			self.image = pygame.image.load("img/button_red.png")
			self.image = pygame.transform.smoothscale(self.image, (BUTTON.width, BUTTON.height))
			self.rect = self.image.get_rect()
			self.color_code = "red"

		elif self.type == "button_green":
			self.image = pygame.image.load("img/button_green.png")
			self.image = pygame.transform.smoothscale(self.image, (BUTTON.width, BUTTON.height))
			self.rect = self.image.get_rect()
			self.color_code = "green"	

		elif self.type == "door_blue":
			self.image = pygame.image.load("img/door_blue.png")
			self.image = pygame.transform.smoothscale(self.image, (DOOR.width, DOOR.height))
			self.rect = self.image.get_rect()
			self.color_code = "blue"							

		elif self.type == "door_red":
			self.image = pygame.image.load("img/door_red.png")
			self.image = pygame.transform.smoothscale(self.image, (DOOR.width, DOOR.height))
			self.rect = self.image.get_rect()
			self.color_code = "red"


		elif self.type == "door_green":
			self.image = pygame.image.load("img/door_green.png")
			self.image = pygame.transform.smoothscale(self.image, (DOOR.width, DOOR.height))
			self.rect = self.image.get_rect()
			self.color_code = "green"

		elif self.type == "lock":
			self.image = pygame.image.load("img/lock.png")
			self.image = pygame.transform.smoothscale(self.image, (LOCK.width, LOCK.height))
			self.rect = self.image.get_rect()

		elif self.type == "key":
			self.image = pygame.image.load("img/key.png")
			self.image = pygame.transform.smoothscale(self.image, (KEY.width, KEY.height))
			self.rect = self.image.get_rect()

		elif self.type == "star":
			self.image = pygame.image.load("img/star.png")
			self.image = pygame.transform.smoothscale(self.image, (STAR.width, STAR.height))
			self.rect = self.image.get_rect()
			
		self.rect.x = x
		self.rect.y = y



	def scale(self, factor):
		width = self.image.get_rect().width
		height = self.image.get_rect().height

		self.image = pygame.transform.smoothscale(self.image, (width*factor, height*factor))
		self.rect = self.image.get_rect()