import pygame
from constants import *
from block import *


class Icons:
    def __init__(self):
        self.icons_group = pygame.sprite.OrderedUpdates()
        self.load_icons()
        self.selected = "block"

    def get_image(self, x, y, width, height, spritesheet):
        image = pygame.Surface((width, height))
        image.blit(spritesheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)

        return image

    def load_icons(self):
        player = Block(0, 0)
        player.image = self.get_image(150, 0, 50, 61, PLAYER.spritesheet)
        player.image = pygame.transform.smoothscale(player.image, (BLOCK.size))
        player.rect = player.image.get_rect()
        player.type = ASSET.player
        self.icons_group.add(player)

        block = Block(0, 0)
        block.image = pygame.image.load("img/block_blue.png")
        block.image = pygame.transform.smoothscale(block.image, (BLOCK.size))
        block.rect = block.image.get_rect()
        block.type = ASSET.block
        self.icons_group.add(block)

        box = Block(0, 0)
        box.image = pygame.image.load("img/box.png")
        box.image = pygame.transform.smoothscale(box.image, (BLOCK.size))
        box.rect = box.image.get_rect()
        box.type = ASSET.box
        self.icons_group.add(box)

        blue_button = Block(0, 0)
        blue_button.image = pygame.image.load("img/button_blue.png")
        blue_button.image = pygame.transform.smoothscale(blue_button.image, (BLOCK.size))
        blue_button.rect = blue_button.image.get_rect()
        blue_button.type = ASSET.button_blue
        self.icons_group.add(blue_button)


        green_button = Block(0, 0)
        green_button.image = pygame.image.load("img/button_green.png")
        green_button.image = pygame.transform.smoothscale(green_button.image, (BLOCK.size))
        green_button.rect = green_button.image.get_rect()
        green_button.type = ASSET.button_green
        self.icons_group.add(green_button)

        red_button = Block(0, 0)
        red_button.image = pygame.image.load("img/button_red.png")
        red_button.image = pygame.transform.smoothscale(red_button.image, (BLOCK.size))
        red_button.rect = red_button.image.get_rect()
        red_button.type = ASSET.button_red
        self.icons_group.add(red_button)

        blue_door = Block(0, 0)
        blue_door.image = pygame.image.load("img/door_blue.png")
        blue_door.image = pygame.transform.smoothscale(blue_door.image, (BLOCK.size))
        blue_door.rect = blue_door.image.get_rect()
        blue_door.type = ASSET.door_blue
        self.icons_group.add(blue_door)


        green_door = Block(0, 64)
        green_door.image = pygame.image.load("img/door_green.png")
        green_door.image = pygame.transform.smoothscale(green_door.image, (BLOCK.size))
        green_door.rect = green_door.image.get_rect()
        green_door.type = ASSET.door_green
        self.icons_group.add(green_door)

        red_door = Block(0, 0)
        red_door.image = pygame.image.load("img/door_red.png")
        red_door.image = pygame.transform.smoothscale(red_door.image, (BLOCK.size))
        red_door.rect = red_door.image.get_rect()
        red_door.type = ASSET.door_red
        self.icons_group.add(red_door)


        platform_h = Block(0, 0)
        platform_h.image = pygame.image.load("img/platformh.png")
        platform_h.image = pygame.transform.smoothscale(platform_h.image, (BLOCK.size))
        platform_h.rect = platform_h.image.get_rect()
        platform_h.type = ASSET.platform_h
        self.icons_group.add(platform_h)

        platform_v = Block(0, 0)
        platform_v.image = pygame.image.load("img/platformv.png")
        platform_v.image = pygame.transform.smoothscale(platform_v.image, (BLOCK.size))
        platform_v.rect = platform_v.image.get_rect()
        platform_v.type = ASSET.platform_v
        self.icons_group.add(platform_v)

        platform_block = Block(0, 0)
        platform_block.image = pygame.image.load("img/platform_block.png")
        platform_block.image = pygame.transform.smoothscale(platform_block.image, (BLOCK.size))
        platform_block.rect = platform_block.image.get_rect()
        platform_block.type = ASSET.platform_block
        self.icons_group.add(platform_block)

        platformv_block = Block(0, 0)
        platformv_block.image = pygame.image.load("img/platformv_block.png")
        platformv_block.image = pygame.transform.smoothscale(platformv_block.image, (BLOCK.size))
        platformv_block.rect = platformv_block.image.get_rect()
        platformv_block.type = ASSET.platformv_block
        self.icons_group.add(platformv_block)

        star = Block(0, 128)
        star = pygame.sprite.Sprite()
        star.image = pygame.image.load("img/star.png")
        star.image = pygame.transform.smoothscale(star.image, (BLOCK.size))
        star.rect = star.image.get_rect()
        star.type = ASSET.star
        self.icons_group.add(star)

        lock = Block(0, 0)
        lock.image = pygame.image.load("img/lock.png")
        lock.image = pygame.transform.smoothscale(lock.image, (BLOCK.size))
        lock.rect = lock.image.get_rect()
        lock.type = ASSET.lock
        self.icons_group.add(lock)

        key = Block(0, 0)
        key.image = pygame.image.load("img/key.png")
        key.image = pygame.transform.smoothscale(key.image, (BLOCK.size))
        key.rect = key.image.get_rect()
        key.type = ASSET.key
        self.icons_group.add(key)


        x = 0
        y = 4
        for icon in self.icons_group:
            icon.rect.x = x * 32
            icon.rect.y = y * 32
            x += 1
            if x >= 5:
                x = 0
                y += 1

    def update(self):
        self.icons_group.update()

    def selectIcon(self):
        pos = pygame.mouse.get_pos()
        for icon in self.icons_group:
            if icon.rect.collidepoint(pos):
                self.selected_type = icon.type
                return

    def draw(self, surface):
        for icon in self.icons_group:
            surface.blit(icon.image, icon.rect)