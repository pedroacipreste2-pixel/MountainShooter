#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_ORANGE, MEMU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/Menu.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        pygame.mixer_music.load('./asset/guitar-vibe.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.memu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.memu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MEMU_OPTION)):
                self.memu_text(20, MEMU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def memu_text(self, text_size: int, text: str, text_color: tuple, text_certer_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_certer_pos)
        self.window.blit(source=text_surf,dest=text_rect)