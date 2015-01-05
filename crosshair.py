import pygame
from pygame.locals import *
from constants import *

class Crosshair(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(CROSSHAIR)
		self.rect = self.image.get_rect()

		self.rect.x = x
		self.rect.y = y

		self.hspeed = 0
		self.vspeed = 0

	def update(self):
		key = pygame.key.get_pressed()
		if key[K_w]:
			self.vspeed = -20
		if key[K_a]:
			self.hspeed = -20
		if key[K_s]:
			self.vspeed = 20
		if key[K_d]:
			self.hspeed = 20
		
		self.rect.x += self.hspeed
		self.rect.y += self.vspeed

	def handleEvents(self, event):
		if event.key == K_w or event.key == K_s:
			self.vspeed = 0
		if event.key == K_a or event.key == K_d:
			self.hspeed = 0
