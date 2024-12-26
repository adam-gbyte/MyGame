import pygame
import sys
from entity import Player
from utils.utils import Utils2

# Inisialisasi Pygame
pygame.init()

# Font default untuk game
font = pygame.font.Font(None, 40)


def game_page(screen):
    """
    Fungsi untuk menampilkan halaman game utama.

    :param screen: Objek layar Pygame (pygame.Surface).
    :return: String yang menunjukkan pilihan pengguna ("menu" atau "option").
    """
    width = screen.get_width()
    height = screen.get_height()

    # Membuat objek player
    player_1 = Player("Hero", 100, 100)

    # Membuat tombol menu dan opsi
    button_menu = Utils2.Button("Menu", 20, 20, 100, 45, (255, 0, 255), font)
    button_option = Utils2.Button("Option", 150, 20, 100, 45, (0, 0, 255), font)

    # Membuat teks di halaman game
    text_game_page = Utils2.Text(font_name=None, font_size=36, color=(255, 255, 0))

    # Inisialisasi clock untuk membatasi FPS
    clock = pygame.time.Clock()

    while True:
        clicked = False
        screen.fill("white")  # Mengisi layar dengan warna putih

        # Menampilkan teks halaman game
        text_game_page.draw_text(screen, "Game Page", (width / 2, height / 2))

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
                    print("Menu button in game page clicked!")
                    return "menu"  # Kembali ke menu utama
                elif button_option.is_clicked(mx, my):
                    print("Option button in game page clicked!")
                    return "option"  # Pindah ke halaman opsi

                clicked = True  # Tombol sudah diklik

            # Reset status klik jika mouse ditekan
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = False

        # Menangani input keyboard untuk pergerakan player
        keys = pygame.key.get_pressed()
        player_1.move(keys)  # Memperbarui posisi player
        player_1.draw(screen)  # Menggambar player di layar

        # Menggambar tombol menu dan opsi
        button_menu.draw(screen)
        button_option.draw(screen)

        # Perbarui layar
        pygame.display.flip()

        # Batasi FPS ke 60
        clock.tick(60)
