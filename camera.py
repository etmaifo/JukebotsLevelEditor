import pygame

class Camera:
	def __init__(self, camera_rect, width, height):
		self.camera_func = camera_rect
		self.width = width
		self.height = height
		self.rect = pygame.Rect(0, 0, self.width, self.height)

	def apply(self, target):
		return target.rect.move(self.rect.topleft)

	def update(self, target):
		self.rect = self.camera_func(self.rect, target.rect)
