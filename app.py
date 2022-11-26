import pygame
import pygame_menu
from ui import *


class Application:
    def main(self):
        surface = pygame.display.set_mode((1000, 800))
        ui = EnterPage()
        while True:
            ui.draw()
            ui.menu.mainloop(surface)

    def _build(self):
        pass


app = Application()
app.main()