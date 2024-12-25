import pygame

import menu_page
import option_page
import game_page

from settings import WIDTH, HEIGHT, TITLE

# Inisialisasi Pygame
pygame.init()

class Main(object):
    def __init__(self):
        # Set ukuran layar
        self.screen_width = WIDTH
        self.screen_height = HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(TITLE)

    # Main loop game
    def game_loop(self):
        current_page = "menu"  # Halaman yang sedang aktif

        while True:

            if current_page == "menu":
                result = menu_page.main_menu(self.screen) # Tampilkan menu utama
                if result == "play":
                    current_page = "game" # Pindah ke halaman play game
                if result == "option":
                    current_page = "option" # Pindah ke halaman option game
                if result == "menu":
                    current_page = "menu" # Pindah ke halaman menu

            elif current_page == "game":
                result = game_page.game_page(self.screen)  # Tampilkan halaman game
                if result == "menu":
                    current_page = "menu" # Pindah ke halaman menu
                if result == "option":
                    current_page = "option" # Pindah ke halaman menu

            elif current_page == "option":
                result = option_page.option_page(self.screen) # Tampilkan halaman option
                if result == "menu":
                    current_page = "menu" # Pindah ke halaman menu

# Menjalankan game
if __name__ == '__main__':
    run = Main()
    run.game_loop()
