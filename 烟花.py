import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# 定义烟花粒子类
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        size = random.randint(10, 20)
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.randint(5, 10)
        self.gravity = pygame.Vector2(0, 0.3)
        self.resistance = 0.02
        self.life = random.randint(40, 60)

    def update(self):
        self.life -= 1
        if self.life <= 0:
            self.kill()
        self.velocity *= (1 - self.resistance)
        self.velocity += self.gravity
        self.rect.move_ip(self.velocity)

# 创建一个粒子群组
particles = pygame.sprite.Group()

# 加载中文字体
font_path ="X:\python\XiaoDouDaoShanZhongYueJian-Shan-ChangGui(REEJI-Xiaodou-MoonGB-Flash-Regular)-2.ttf"  # 将 'your_font_path.ttf' 替换为你的字体文件路径
font = pygame.font.Font(font_path, 36)

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # 每帧创建一些新的粒子
    for _ in range(10):
        particle = Particle(width // 2, height // 2, random.choice(COLORS))
        particles.add(particle)

    # 更新和绘制粒子
    for particle in particles:
        particle.update()
        pygame.draw.rect(screen, particle.image.get_at((0, 0)), particle.rect)

    particles.update()
    particles.draw(screen)

    # 绘制文字
    text = font.render("庆祝上海解封一周年", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, 50)
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

# 退出程序
pygame.quit()
