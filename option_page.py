import pygame
import sys

from utils.utils import Utils2

pygame.init()

font = pygame.font.Font(None, 40)

# Fungsi untuk halaman option
def option_page(screen):

    # Membuat tombol
    button_menu = Utils2().Button("Menu", 20, 20, 100, 45, (255, 0, 255), font)

    while True:
        clicked = False
        screen.fill("white")

        # Menampilkan teks "Game Page"
        Utils2.draw_text(screen, "Welcome to the Option Game", (20, 550), 45, (0, 0, 0))

        # Menangani event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Memeriksa klik mouse (tombol dilepaskan)
            if event.type == pygame.MOUSEBUTTONUP and not clicked:
                mx, my = pygame.mouse.get_pos()

                # Menangani klik pada tombol
                if button_menu.is_clicked(mx, my):
                    print("Back button in option page, clicked!")
                    return "menu"  # Kembali ke game

                clicked = True  # Tombol sudah diklik, set status ke True

            # Jika mouse tidak diklik lagi, reset status
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = False

        # Gambar tombol menu
        button_menu.draw(screen)

        pygame.display.update()
