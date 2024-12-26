import pygame

# Import halaman-halaman game
import menu_page
import option_page
import game_page

from settings import WIDTH, HEIGHT, TITLE

# Inisialisasi Pygame
pygame.init()


class Main:
    def __init__(self):
        """
        Inisialisasi game utama, termasuk layar dan judul.
        """
        self.screen_width = WIDTH
        self.screen_height = HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(TITLE)

    def game_loop(self):
        """
        Loop utama game, menangani navigasi antar halaman.
        """
        current_page = "menu"  # Halaman awal adalah menu utama

        while True:
            # Logika navigasi halaman
            if current_page == "menu":
                result = menu_page.main_menu(self.screen)  # Tampilkan menu utama
                if result == "play":
                    current_page = "game"  # Pindah ke halaman game
                elif result == "option":
                    current_page = "option"  # Pindah ke halaman opsi
                elif result == "menu":
                    current_page = "menu"  # Tetap di halaman menu

            elif current_page == "game":
                result = game_page.game_page(self.screen)  # Tampilkan halaman game
                if result == "menu":
                    current_page = "menu"  # Kembali ke menu utama
                elif result == "option":
                    current_page = "option"  # Pindah ke halaman opsi

            elif current_page == "option":
                result = option_page.option_page(self.screen)  # Tampilkan halaman opsi
                if result == "menu":
                    current_page = "menu"  # Kembali ke menu utama


# Menjalankan game
if __name__ == '__main__':
    game = Main()
    game.game_loop()
