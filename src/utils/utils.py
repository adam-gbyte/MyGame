import pygame


class Utils2:
    class Button:
        def __init__(self, text, x, y, width, height, color, font):
            """
            Inisialisasi tombol dengan teks, posisi, ukuran, warna, dan font.

            :param text: Teks pada tombol (string).
            :param x: Posisi x tombol (int).
            :param y: Posisi y tombol (int).
            :param width: Lebar tombol (int).
            :param height: Tinggi tombol (int).
            :param color: Warna tombol (tuple atau string).
            :param font: Objek font Pygame (pygame.font.Font).
            """
            self.text = text
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            self.font = font

        def draw(self, screen):
            """
            Menggambar tombol pada layar.

            :param screen: Objek layar Pygame (pygame.Surface).
            """
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            label = self.font.render(self.text, True, "white")
            screen.blit(
                label,
                (self.x + (self.width - label.get_width()) // 2,
                 self.y + (self.height - label.get_height()) // 2)
            )

        def is_clicked(self, mx, my):
            """
            Memeriksa apakah tombol diklik berdasarkan posisi mouse.

            :param mx: Posisi x mouse (int).
            :param my: Posisi y mouse (int).
            :return: True jika tombol diklik, False jika tidak.
            """
            return self.x < mx < self.x + self.width and self.y < my < self.y + self.height

    class Text:
        def __init__(self, font_name=None, font_size=24, color=(255, 255, 255)):
            """
            Utilitas untuk menggambar teks di Pygame.

            :param font_name: Nama font (string) atau None untuk default.
            :param font_size: Ukuran font (int).
            :param color: Warna teks dalam format RGB (tuple).
            """
            self.font_name = font_name
            self.font_size = font_size
            self.color = color
            self.font = pygame.font.Font(font_name, font_size)

        def render_text(self, text, antialias=True, color=None):
            """
            Membuat permukaan teks.

            :param text: Teks yang akan ditampilkan (string).
            :param antialias: Apakah menggunakan antialiasing (bool).
            :param color: Warna teks (tuple) atau None untuk warna default.
            :return: Permukaan teks (pygame.Surface).
            """
            color = color or self.color
            return self.font.render(text, antialias, color)

        def draw_text(self, screen, text, position, antialias=True, color=None):
            """
            Menggambar teks di layar.

            :param screen: Objek layar Pygame (pygame.Surface).
            :param text: Teks yang akan ditampilkan (string).
            :param position: Posisi teks dalam format (x, y).
            :param antialias: Apakah menggunakan antialiasing (bool).
            :param color: Warna teks (tuple) atau None untuk warna default.
            """
            text_surface = self.render_text(text, antialias, color)
            screen.blit(text_surface, position)

    @staticmethod
    def draw_text(surface, text, position, font_size, color, font_path=None):
        """
        Menggambar teks pada permukaan tertentu.

        :param surface: Permukaan Pygame (pygame.Surface).
        :param text: Teks yang akan ditampilkan (string).
        :param position: Posisi teks dalam format (x, y).
        :param font_size: Ukuran font (int).
        :param color: Warna teks (tuple).
        :param font_path: Path ke file font (string) atau None untuk default.
        """
        try:
            font = pygame.font.Font(font_path, font_size)
        except FileNotFoundError:
            font = pygame.font.SysFont(None, font_size)
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, position)

    @staticmethod
    def load_image(path, scale=None):
        """
        Memuat gambar dari path, dengan opsi skala.

        :param path: Path ke file gambar (string).
        :param scale: Ukuran baru gambar dalam format (width, height) atau None.
        :return: Objek gambar Pygame (pygame.Surface) atau None jika gagal.
        """
        try:
            image = pygame.image.load(path).convert_alpha()
            if scale:
                image = pygame.transform.scale(image, scale)
            return image
        except pygame.error as e:
            print(f"Error loading image {path}: {e}")
            return None

    @staticmethod
    def limit_frame_rate(clock, fps):
        """
        Membatasi frame rate menggunakan objek clock.

        :param clock: Objek clock Pygame (pygame.time.Clock).
        :param fps: Frame per detik yang diinginkan (int).
        """
        clock.tick(fps)

    @staticmethod
    def play_sound(path, volume=1.0):
        """
        Memutar suara dari path.

        :param path: Path ke file suara (string).
        :param volume: Volume suara (float, 0.0 hingga 1.0).
        """
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(volume)
            sound.play()
        except pygame.error as e:
            print(f"Error playing sound {path}: {e}")

    @staticmethod
    def check_collision(rect1, rect2):
        """
        Memeriksa tabrakan antara dua objek Rect.

        :param rect1: Objek Rect pertama (pygame.Rect).
        :param rect2: Objek Rect kedua (pygame.Rect).
        :return: True jika ada tabrakan, False jika tidak.
        """
        return rect1.colliderect(rect2)
