import pygame
import sys
from entity import Player

from utils.utils import Utils2

pygame.init()

# Font game
font = pygame.font.Font(None, 40)

# Fungsi untuk halaman game
def game_page(screen):

    # Membuat player
    player_1 = Player("Hero", 100, 100)

    # Membuat tombol
    button_menu = Utils2().Button("Menu", 20, 20, 100, 45, (255, 0, 255), font)
    button_option = Utils2().Button("Option", 150, 20, 100, 45, (0, 0, 255), font)

    clock = pygame.time.Clock()

    while True:
        clicked = False
        screen.fill("white")

        # Menampilkan teks "Game Page"
        label = font.render("Welcome to the Game!", True, "black")
        screen.blit(label, (screen.get_width() // 2 - label.get_width() // 2, screen.get_height() // 2 - label.get_height() // 2))

        # Menangani event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Memeriksa klik mouse (tombol dilepaskan)
            if event.type == pygame.MOUSEBUTTONUP and not clicked:
                mx, my = pygame.mouse.get_pos()

                # Menangani klik pada tombol
                if button_menu.is_clicked(mx, my):  # Klik kiri mouse
                    print("Menu button in game page, clicked!")
                    return "menu"
                elif button_option.is_clicked(mx, my):  # Klik kiri mouse
                    print("Option button in game page, clicked!")
                    return "option"

                clicked = True  # Tombol sudah diklik, set status ke True

            # Jika mouse tidak diklik lagi, reset status
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = False

        # Menangani input keyboard
        keys = pygame.key.get_pressed()

        # Menggambar player
        player_1.move(keys) # Update pergerakkan
        # player_1.in_window(screen)
        player_1.draw(screen) # Menggambar Player

        # Gambar tombol
        button_menu.draw(screen)
        button_option.draw(screen)

        # Menguji tabrakan


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        clock.tick(60) / 1000
