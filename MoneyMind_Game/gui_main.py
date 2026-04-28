import pygame
from engine.player import Player
from engine.finance import FinanceManager

# 1. Init
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MoneyMind: Moliyaviy Erkinlik")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
BLUE = (52, 152, 219)

# Shriftlar
font = pygame.font.SysFont("Arial", 24)
title_font = pygame.font.SysFont("Arial", 32, bold=True)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def main_gui():
    player = Player("Myster008", 100000) # Test uchun
    running = True
    
    while running:
        screen.fill((240, 240, 240)) # Och kulrang fon
        
        # Voqealarni ushlash
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # Space bosilsa keyingi oy
                    FinanceManager.process_monthly_cycle(player)

        # Vizual Panellar
        pygame.draw.rect(screen, WHITE, (20, 20, 350, 200), border_radius=10) # Status paneli
        draw_text("Moliyaviy Holat", title_font, BLACK, 40, 30)
        draw_text(f"Balans: ${player.balance:,.2f}", font, GREEN, 40, 80)
        draw_text(f"Bank: ${player.savings:,.2f}", font, BLUE, 40, 120)
        
        # Progress Bar (Maqsadga erishish)
        pygame.draw.rect(screen, BLACK, (400, 50, 350, 30), 2) # Ramka
        progress_width = min(350 * ((player.balance + player.savings) / player.target_money), 350)
        pygame.draw.rect(screen, GREEN, (400, 50, progress_width, 30))
        draw_text("Maqsad sari yo'l", font, BLACK, 400, 20)

        # Tugmalar bo'limi (Pastda)
        draw_text("Keyingi oyga o'tish uchun [SPACE] ni bosing", font, BLACK, 200, 500)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main_gui()
