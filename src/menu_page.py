import pygame
import sys
from utils.utils import Utils2

# Inisialisasi Pygame
pygame.init()

# Font default
font = pygame.font.Font(None, 40)


def main_menu(screen):
    """
    Fungsi untuk menampilkan halaman menu utama.

    :param screen: Objek layar Pygame (pygame.Surface).
    :return: String yang menunjukkan pilihan pengguna ("play", "option", atau keluar).
    """
    clicked = False  # Status apakah tombol sudah diklik

    # Membuat tombol menu utama
    button_play = Utils2.Button("Play", 20, 20, 100, 45, (255, 0, 255), font)
    button_option = Utils2.Button("Option", 20, 70, 100, 45, (255, 0, 255), font)
    button_quit = Utils2.Button("Quit", 20, 120, 100, 45, (255, 0, 255), font)

    while True:
        screen.fill("white")  # Mengisi layar dengan warna putih

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
                    return "option"  # Pindah ke halaman opsi

                elif button_quit.is_clicked(mx, my):
                    print("Quit button clicked!")
                    pygame.quit()
                    sys.exit()  # Keluar dari game

                clicked = True  # Tombol sudah diklik

            # Reset status klik jika tombol mouse ditekan
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = False

        # Gambar tombol menu di layar
        button_play.draw(screen)
        button_option.draw(screen)
        button_quit.draw(screen)

        # Perbarui layar
        pygame.display.update()
