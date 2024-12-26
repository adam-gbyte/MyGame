import pygame
import sys
from utils.utils import Utils2

# Inisialisasi Pygame
pygame.init()

# Font default
font = pygame.font.Font(None, 40)


def option_page(screen):
    """
    Fungsi untuk menampilkan halaman opsi.

    :param screen: Objek layar Pygame (pygame.Surface).
    :return: String yang menunjukkan pilihan pengguna ("menu" untuk kembali ke menu utama).
    """
    # Membuat tombol kembali ke menu utama
    button_menu = Utils2.Button("Menu", 20, 20, 100, 45, (255, 0, 255), font)

    while True:
        clicked = False  # Status klik mouse
        screen.fill("white")  # Mengisi layar dengan warna putih

        # Menampilkan teks judul
        Utils2.draw_text(screen, "Welcome to the Option Page", (20, 550), 45, (0, 0, 0))

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
                    print("Back button in option page clicked!")
                    return "menu"  # Kembali ke menu utama

                clicked = True  # Tombol sudah diklik

            # Reset status klik jika tombol mouse ditekan
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = False

        # Gambar tombol menu di layar
        button_menu.draw(screen)

        # Perbarui layar
        pygame.display.update()
