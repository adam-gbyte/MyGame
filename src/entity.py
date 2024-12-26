import pygame

pygame.init()

# Konstanta untuk kecepatan gerakan pemain dan musuh
PLAYER_SPEED = 5
ENEMY_SPEED = 5


class Entity:
    """
    Kelas dasar untuk entitas di dalam game, seperti pemain atau musuh.
    """

    def __init__(self, name, window_x, window_y, width=16, height=16, color=(255, 0, 0)):
        """
        Inisialisasi entitas.

        :param name: Nama entitas (string).
        :param window_x: Posisi awal x (int).
        :param window_y: Posisi awal y (int).
        :param width: Lebar entitas (int).
        :param height: Tinggi entitas (int).
        :param color: Warna entitas dalam format RGB (tuple).
        """
        self.x = window_x
        self.y = window_y
        self.width = width
        self.height = height
        self.color = color

        self.name = name
        self.health = 0
        self.damage = 0

    def draw(self, surface):
        """
        Menggambar entitas pada permukaan layar.
        
        :param surface: Objek permukaan layar (pygame.Surface).
        """
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def collides_with(self, other):
        """
        Memeriksa apakah entitas ini bertabrakan dengan entitas lain.

        :param other: Entitas lain (Entity).
        :return: True jika bertabrakan, False jika tidak.
        """
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )

    def __str__(self):
        """
        Mengembalikan representasi string dari entitas.
        """
        return f"{self.name} (Health: {self.health}, Damage: {self.damage})"


class Player(Entity):
    """
    Kelas untuk pemain, mewarisi dari Entity.
    """

    def __init__(
        self, name, window_x, window_y, width=16, height=16, color=(255, 0, 0), speed=PLAYER_SPEED
    ):
        """
        Inisialisasi pemain.

        :param name: Nama pemain (string).
        :param window_x: Posisi awal x (int).
        :param window_y: Posisi awal y (int).
        :param width: Lebar pemain (int).
        :param height: Tinggi pemain (int).
        :param color: Warna pemain dalam format RGB (tuple).
        :param speed: Kecepatan pemain (int).
        """
        super().__init__(name, window_x, window_y, width, height, color)
        self.speed = speed

    def move(self, keys):
        """
        Memperbarui posisi pemain berdasarkan input keyboard.

        :param keys: Input keyboard (pygame.key.get_pressed()).
        """
        if keys[pygame.K_UP] or keys[pygame.K_w]:  # Bergerak ke atas
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Bergerak ke bawah
            self.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Bergerak ke kiri
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Bergerak ke kanan
            self.x += self.speed

    def in_window(self, screen):
        """
        Menjaga agar pemain tetap berada di dalam layar.

        :param screen: Objek layar (pygame.Surface).
        """
        self.x = max(0, min(self.x, screen.get_width() - self.width))
        self.y = max(0, min(self.y, screen.get_height() - self.height))
