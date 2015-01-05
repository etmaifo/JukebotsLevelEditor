import pygame, sys, os
from pygame import *
from block import *
from camera import *
from crosshair import *
from constants import *
from assets import *

class Editor:
	def __init__(self, width=800, height=384):
		pygame.init()
		os.environ["SDL_VIDEO_CENTERED"] = "1"

		self.width = width
		self.height = height
		self.screen_width = 640
		self.screen = pygame.display.set_mode((self.width, self.height))#, DOUBLEBUF | FULLSCREEN)
		self.right_panel = pygame.Surface((self.screen_width, height))
		self.right_panel_rect = self.right_panel.get_rect()
		self.sidebar = pygame.Surface((160, self.height))
		self.sidebar_rect = self.sidebar.get_rect()
		self.sidebar_rect.width-=2
		self.sidebar_rect.height-=2
		self.sidebar_rect.x+=1
		self.sidebar_rect.y+=1

		self.fpsClock = pygame.time.Clock()

		self.cursor = pygame.Rect(0, 0, 8, 8)
		self.crosshair = Crosshair(self.width/4, self.height/2)

		self.tile_group = pygame.sprite.OrderedUpdates()
		self.object_group = pygame.sprite.OrderedUpdates()
		self.entities = pygame.sprite.OrderedUpdates()

		#self.camera = Camera(self.complex_camera, 640, height)
		self.camera = Camera(self.complex_camera, self.screen_width*2+self.sidebar_rect.width+2, height)

		self.blocklist = []
		self.objectlist = []
		self.coords = []

		self.asset = Asset()
		self.display_asset = Asset()

		self.complete_asset = True


	def launch(self, fps=60):
		self.fps = fps
		while True:
			self.handleEvents()
			self.update()
			self.draw()

			pygame.display.update()
			pygame.display.set_caption("Humanoids - " + str(int(self.fpsClock.get_fps()))+" FPS")
			self.fpsClock.tick(self.fps)


	def handleEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

			if event.type == MOUSEMOTION: # Draw while dragging
				if event.buttons[0]:
					asset = Asset()
					asset.type = self.asset.type
					asset.update()					
					self.highlight_tile(asset, pygame.mouse.get_pos())

				elif event.buttons[2]:
					self.remove_asset(pygame.mouse.get_pos())

			if event.type == MOUSEBUTTONDOWN: # Single click drawing
				if event.button == MouseButton.RIGHT:
					self.remove_asset(pygame.mouse.get_pos())

				elif event.button == MouseButton.LEFT:
					asset = Asset()
					asset.type = self.asset.type
					asset.update()
					self.highlight_tile(asset, pygame.mouse.get_pos())

			if event.type == KEYDOWN:
				if self.complete_asset:
					if event.key == K_b:
						self.asset.type = "block"
						self.display_asset.type = "block"
					if event.key == K_m:
						self.asset.type = "box"
						self.display_asset.type = "box"
					if event.key == K_l:
						self.asset.type = "lock"
						self.display_asset.type = "lock"
					if event.key == K_k:
						self.asset.type = "key"
						self.display_asset.type = "key"						
					if event.key == K_p:
						self.asset.type = "player"
						self.display_asset.type = "player"
					if event.key == K_h:
						self.asset.type = "platform_h"
						self.display_asset.type = "platform_h"
					if event.key == K_v:
						self.asset.type = "platform_v"
						self.display_asset.type = "platform_v"
					if event.key == K_0:
						self.asset.type = "star"
						self.display_asset.type = "star"
					if event.key == K_1:
						self.asset.type = "button_blue"
						self.display_asset.type = "button_blue"
					if event.key == K_2:
						self.asset.type = "button_red"
						self.display_asset.type = "button_red"
					if event.key == K_3:
						self.asset.type = "button_green"
						self.display_asset.type = "button_green"
					if event.key == K_4:
						self.asset.type = "door_red"
						self.display_asset.type = "door_red"
					if event.key == K_5:
						self.asset.type = "door_green"
						self.display_asset.type = "door_green"
					if event.key == K_6:
						self.asset.type = "door_blue"
						self.display_asset.type = "door_blue"												
				if event.key == K_j:
					self.asset.type = "platform_block"
					self.display_asset.type = "platform_block"

				if event.key == K_i:
					print self.objectlist

				if event.key == K_o:
					print self.blocklist

				if event.key == K_q:
					self.prepare_files()	
					self.create_level_data()			

			if event.type == KEYUP:
				if event.key == K_DOWN:
					self.camera.width += 0

				self.crosshair.handleEvents(event)



	def convert(self, xy):
		''' Adjust grid coordinates
		to start from the right side of the 
		side bar'''
		x = xy[0]
		y = xy[1]
		x = x*BLOCKSIZE
		x -= 160
		x = x/16

		return [x,y]

	def highlight_tile(self, asset, mouseposition):
		pos = [mouseposition[0], mouseposition[1]]
		pos[0] -= self.camera.rect.x
		pos[1] -= self.camera.rect.y
		pos[0] -= 160
	
		xy = [pos[0]/BLOCKSIZE, pos[1]/BLOCKSIZE]
		#xy = self.convert(xy)

		if asset.type == "block":
			for tile in self.tile_group:
				if tile.rect.collidepoint(pos):
					tile.image = asset.image
					if xy not in self.blocklist:
						self.blocklist.append(xy)
						xy.insert(0, asset.type)
						self.blocklist.sort()

		elif asset.type == "player":
			for tile in self.object_group:
				if tile.rect.collidepoint(pos):
					tile.image = asset.image
					if xy not in self.objectlist:
						self.objectlist.append(xy)
						#self.blocklist.append(xy)
						xy.insert(0, asset.type)						
						self.objectlist.sort()

		elif asset.type == "platform_h":
			for tile in self.object_group:
				if tile.rect.collidepoint(pos):
					tile.image = asset.image
					if xy not in self.objectlist:
						self.objectlist.append(xy)
						#self.blocklist.append(xy)
						xy.insert(0, asset.type)						
						self.objectlist.sort()
						self.complete_asset = False

						self.asset.type = "platform_block"
						self.display_asset.type = "platform_block"

		elif asset.type == "platform_block":
			for tile in self.object_group:
				if tile.rect.collidepoint(pos):
					tile.image = asset.image
					for obj in self.objectlist:
						if obj[0] == "platform_h":
							#obj.append(xy[0]-obj[1])	# right block pos - left block pos = rail distance
							if len(obj) == 3:
								obj.append(xy[0])
								obj.append(xy[1])
							self.complete_asset = True

							self.asset.type = "platform_h"
							self.display_asset.type = "platform_h"						

		elif asset.type == "platform_v":
			for tile in self.object_group:
				if tile.rect.collidepoint(pos):
					tile.image = asset.image
					if xy not in self.objectlist:
						self.objectlist.append(xy)
						#self.blocklist.append(xy)
						xy.insert(0, asset.type)						
						self.objectlist.sort()
						self.complete_asset = False

						self.asset.type = "platformv_block"
						self.display_asset.type = "platformv_block"												

		elif asset.type == "platformv_block":
			for tile in self.object_group:
				if tile.rect.collidepoint(pos):
					tile.image = asset.image
					for obj in self.objectlist:
						if obj[0] == "platform_v":
							#obj.append(xy[0]-obj[1])	# right block pos - left block pos = rail distance
							if len(obj) == 3:
								obj.append(xy[0])
								obj.append(xy[1])
							self.complete_asset = True

							self.asset.type = "platform_v"
							self.display_asset.type = "platform_v"
						

		elif "button" in asset.type or "door" in asset.type or "box" in asset.type or "lock" in asset.type or "key" in asset.type or "star" in asset.type:
			for cell in self.object_group:
				if cell.rect.collidepoint(pos):
					cell.image = asset.image
					if xy not in self.objectlist:
						xy.insert(0, asset.type)
						self.objectlist.append(xy)
						#self.blocklist.append(xy)
						self.objectlist.sort()



	def remove_asset(self, mouseposition):
		pos = [mouseposition[0], mouseposition[1]]
		pos[0] -= self.camera.rect.x
		pos[1] -= self.camera.rect.y

		pos[0] -= 160

		xy = [pos[0]/BLOCKSIZE, pos[1]/BLOCKSIZE]
		asset_name = ""

		for tile in self.tile_group:
			if tile.rect.collidepoint(pos):
				#self.tile_group.remove(tile)
				tile.image = pygame.image.load(GREY_TILE)
				tile.image = pygame.transform.smoothscale(tile.image, (BLOCKSIZE, BLOCKSIZE))
				for block in self.blocklist:
					if block[1] == xy[0] and block[2] == xy[1]:
						self.blocklist.remove(block)


		for cell in self.object_group:
			if cell.rect.collidepoint(pos):
				cell.image = pygame.image.load(GREY_TILE)
				cell.image = pygame.transform.smoothscale(cell.image, (BLOCKSIZE, BLOCKSIZE))
				for obj in self.objectlist:
					if obj[1] == xy[0] and obj[2] == xy[1]:
						self.objectlist.remove(obj)


	def update(self):
		#pygame.display.set_caption("Map Editor")
		self.cursor.x = pygame.mouse.get_pos()[0] - 4
		self.cursor.y = pygame.mouse.get_pos()[1] - 4

		self.crosshair.update()

		self.camera.update(self.crosshair)

		self.asset.update()
		self.display_asset.update()
		self.display_asset.scale(2)

		for tile in self.tile_group:
			self.entities.add(tile)
		for asset in self.object_group:
			self.entities.add(asset)


	def draw(self):
		self.screen.fill((250, 250, 250))
		self.right_panel.fill((255, 255, 255))

		for entity in self.entities:
			self.right_panel.blit(entity.image, self.camera.apply(entity))
		
		self.screen.blit(self.sidebar, (0, 0))
		self.screen.blit(self.right_panel, (160, 0))
		self.sidebar.fill((250, 250, 250), self.sidebar_rect)
		self.sidebar.blit(self.display_asset.image, (50, 50))


	def complex_camera(self, cameraRect, target_rect):
		x, y, dummy, dummy = target_rect
		dummy, dummy, w, h = cameraRect
		x, y  = int(self.width/2)-x, int(self.height/2) - y

		x = min(0, x)
		x = max(-(cameraRect.width-self.width), x)
		y = max(-(cameraRect.height-self.height), y)
		y = min(0, y)

		return pygame.Rect(x, y, w, h)		


	def create_tile_group(self):
		self.tile_group.empty()
		self.object_group.empty()
		width = self.camera.width
		height = self.camera.height
		for y in range(width/BLOCKSIZE):
			for x in range(height/BLOCKSIZE):
				block = Block(y*BLOCKSIZE, x*BLOCKSIZE)
				self.tile_group.add(block)
				#self.object_group.add(block)
				self.coords.append([block.rect.x, block.rect.y])

		for y in range(width/BLOCKSIZE):
			for x in range(height/BLOCKSIZE):
				cell = Block(y*BLOCKSIZE, x*BLOCKSIZE)
				self.object_group.add(cell)
				#self.object_group.add(block)
		self.tile_group.add(self.crosshair)


	def get_image(self, x, y, width, height):
		sheet = pygame.image.load(BG)
		dummy, dummy, w, h = sheet.get_rect()
		image = pygame.Surface((w, h))#.convert()
		image.blit(sheet, (0, 0), (x, y, w, h))
		image.set_colorkey(BLACK)

		return image	


	def create_level(self, blocklist, width, height):
		width = width-self.sidebar.get_rect().width
		raw_str = ""
		level = []
		for i in range(height/BLOCKSIZE):
			for j in range(width/BLOCKSIZE):
				if ['block', j, i] in blocklist:					
					raw_str += "8"
				else:
					raw_str += "."
			level.append(raw_str)
			raw_str = ""
		return level


	def prepare_files(self):
		f = open("output/level.lv", "w")
		f.write("Hello world!")
		f.close()


	def create_level_data(self):
		f = open("output/level01.lv", "w")
		players = ["players"]
		buttons = ["buttons"]
		lifts = ["lifts"]
		doors = ["doors"]
		boxes = ["boxes"]
		locks = ["locks"]
		keys = ["keys"]
		stars = ["stars"]
		#assetlist = []
		level_blocks = self.create_level(self.blocklist, self.camera.width, self.camera.height)

		for assets in self.objectlist:
			if assets[0].startswith("player"):
				players.append(assets)
			elif assets[0].startswith("door"):
				doors.append(assets)
			elif assets[0].startswith("button"):
				buttons.append(assets)
			elif assets[0].startswith("platform"):
				lifts.append(assets)
			elif assets[0].startswith("box"):
				boxes.append(assets)
			elif assets[0].startswith("lock"):
				locks.append(assets)
			elif assets[0].startswith("key"):
				keys.append(assets)
			elif assets[0].startwith("star"):
				stars.append(assets)


		for player in players:
			if player =="players":
				f.write(player+"\n")
			else:
				p = ""
				for item in player:
					p += str(item)+" "

				f.write(p + "\n")

		f.write("\n")
		for door in doors:
			if door == "doors":
				f.write(door+'\n')
			else:
				d = ""
				for item in door:
					d += str(item)+" "

				f.write(d + "\n")

		f.write("\n")
		for button in buttons:
			if button == "buttons":
				f.write(button+'\n')
			else:
				b = ""
				for item in button:
					b += str(item)+" "

				f.write(b + "\n")

		f.write("\n")
		for lift in lifts:
			if lift == "lifts":
				f.write(lift+'\n')
			else:
				l = ""
				for item in lift:
					l += str(item)+" "

				f.write(l + "\n")

		f.write("\n")
		for box in boxes:
			if box == "boxes":
				f.write(box+"\n")
			else:
				l = ""
				for item in box:
					l += str(item)+" "

				f.write(l + "\n")

		f.write("\n")
		for lock in locks:
			if lock == "locks":
				f.write(lock+"\n")
			else:
				l = ""
				for item in lock:
					l += str(item)+" "

				f.write(l + "\n")	

		f.write("\n")
		for key in keys:
			if key == "keys":
				f.write(key+"\n")
			else:
				l = ""
				for item in key:
					l += str(item)+" "

				f.write(l + "\n")		

		f.write("\n")
		for star in stars:
			if star == "stars":
				f.write(key+"\n")
			else:
				l = ""
				for item in star:
					l += str(item)+" "

				f.write(l + "\n")					

		f.write("\n")
		f.write("blocks\n")
		for row in level_blocks:
			f.write(row+"\n")


		f.close()
		print "Done"



editor = Editor()
editor.create_tile_group()
editor.launch()