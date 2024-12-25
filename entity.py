import pygame

pygame.init()

# Konstanta untuk kecepatan gerakan pemain
PLAYER_SPEED = 5
ENEMY_SPEED = 5

class Entity:
    def __init__(self, name, window_x, window_y, width=16, height=16, color=(255, 0, 0)):
        self.x = window_x
        self.y = window_y
        self.width = width
        self.height = height
        self.color = color

        self.name = name
        self.health = 0
        self.damage = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def collides_with(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Damage: {self.damage})"

class Player(Entity):
    def __init__(self,
                 name,
                 window_x,
                 window_y,
                 width=16,
                 height=16,
                 color=(255, 0, 0),
                 speed=5
        ):
        super().__init__(name, window_x, window_y, width, height, color)
        self.speed = speed

    def move(self, keys):
        """Update posisi pemain berdasarkan input."""
        if keys[pygame.K_UP] | keys[pygame.K_w]:  # Bergerak ke atas
            self.y -= self.speed
        if keys[pygame.K_DOWN] | keys[pygame.K_s]:  # Bergerak ke bawah
            self.y += self.speed
        if keys[pygame.K_LEFT] | keys[pygame.K_a]:  # Bergerak ke kiri
            self.x -= self.speed
        if keys[pygame.K_RIGHT] | keys[pygame.K_d]:  # Bergerak ke kanan
            self.x += self.speed

    def in_window(self, screen):
        # Menjaga agar pemain tetap berada di dalam layar
        self.x = max(0, min(self.x, screen.get_width() - self.width))
        self.y = max(0, min(self.y, screen.get_height() - self.height))

    # def draw(self, screen):
    #     """Gambar pemain di layar."""
        # pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # screen.blit(self.image, self.rect)
