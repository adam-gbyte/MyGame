import pygame
import sys

from utils import Utils2

pygame.init()

font = pygame.font.Font(None, 40)

# Fungsi untuk halaman menu utama
def main_menu(screen):
    clicked = False  # Menyimpan status apakah tombol sudah diklik

    button_play = Utils2().Button("Play", 20, 20, 100, 45, (255, 0, 255), font)
    button_option = Utils2().Button("Option", 20, 70, 100, 45, (255, 0, 255), font)
    button_quit = Utils2().Button("Quit", 20, 120, 100, 45, (255, 0, 255), font)

    while True:
        screen.fill("white")

        # Menangani event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("X Quit")
                pygame.quit()
                sys.exit()

            # Memeriksa klik mouse (tombol dilepaskan)
            if event.type == pygame.MOUSEBUTTONUP and not clicked:
                mx, my = pygame.mouse.get_pos()

                # Menangani klik pada tombol
                if button_play.is_clicked(mx, my):
                    print("Play button clicked!")
                    return "play"  # Kembali ke game

                elif button_option.is_clicked(mx, my):
                    print("Options button clicked!")
                    return "option"

                elif button_quit.is_clicked(mx, my):
                    print("Quit button clicked!")
                    pygame.quit()
                    sys.exit()

                clicked = True  # Tombol sudah diklik, set status ke True

            # Jika mouse tidak diklik lagi, reset status
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = False

        # Gambar tombol menu
        button_play.draw(screen)
        button_option.draw(screen)
        button_quit.draw(screen)

        pygame.display.update()