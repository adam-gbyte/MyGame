import pygame

class Utils2:
    class Button:
        def __init__(self, text, x, y, width, height, color, font):
            """Inisialisasi tombol dengan teks, posisi, ukuran, warna, dan font"""
            self.text = text
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            self.font = font

        def draw(self, screen):
            """Menggambar tombol pada layar"""
            # Menggambar persegi panjang untuk tombol
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

            # Menggambar teks di atas tombol
            label = self.font.render(self.text, True, "white")
            screen.blit(label, (self.x + (self.width - label.get_width()) // 2,
                                self.y + (self.height - label.get_height()) // 2))

        def is_clicked(self, mx, my):
            """Memeriksa apakah tombol diklik berdasarkan posisi mouse"""
            return self.x < mx < self.x + self.width and self.y < my < self.y + self.height

    @staticmethod
    def draw_text(surface, text, position, font_size, color, font_path=None):
        """Menggambar teks pada permukaan tertentu."""
        try:
            font = pygame.font.Font(font_path, font_size)
        except FileNotFoundError:
            font = pygame.font.SysFont(None, font_size)
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, position)

    @staticmethod
    def load_image(path, scale=None):
        """Memuat gambar dari path, dengan opsi skala."""
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
        """Membatasi frame rate menggunakan objek clock."""
        clock.tick(fps)

    @staticmethod
    def play_sound(path, volume=1.0):
        """Memutar suara dari path."""
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(volume)
            sound.play()
        except pygame.error as e:
            print(f"Error playing sound {path}: {e}")

    @staticmethod
    def check_collision(rect1, rect2):
        """Memeriksa tabrakan antara dua objek Rect."""
        return rect1.colliderect(rect2)