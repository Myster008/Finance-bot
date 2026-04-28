import pygame
from engine.player import Player
from engine.finance import FinanceManager
from utils.ui_elements import Button

# Init va Oyna sozlamalari
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("MoneyMind Simulyatori")
clock = pygame.time.Clock()

def main_gui():
    player = Player("Myster008", 50000)
    running = True
    
    # Tugmalarni yaratish
    next_month_btn = Button(550, 500, 200, 50, "KEYINGI OY", (46, 204, 113), (39, 174, 96))
    shop_btn = Button(50, 500, 200, 50, "DO'KON", (52, 152, 219), (41, 128, 185))
    bank_btn = Button(300, 500, 200, 50, "BANK", (155, 89, 182), (142, 68, 173))

    while running:
        screen.fill((236, 240, 241)) # Yumshoq oq fon
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Tugma bosilishini tekshirish
            if next_month_btn.is_clicked(event):
                FinanceManager.process_monthly_cycle(player)
            
            if shop_btn.is_clicked(event):
                print("Do'kon oynasi ochildi (Mantiq ulangan)")
                # Bu yerda alohida Shop UI chiqarish mumkin

        # UI Chizish
        # 1. Tepada Header (O'yinchi statusi)
        pygame.draw.rect(screen, (44, 62, 80), (0, 0, 800, 80))
        # (Shu yerda draw_text orqali balans va sog'liqni chizamiz)

        # 2. O'yinchi personaji (Hozircha oddiy doira, keyinchalik rasm)
        pygame.draw.circle(screen, (52, 152, 219), (400, 300), 50)
        # Personaj holati sog'liqqa qarab o'zgarishi mumkin (yashil/qizil)

        # 3. Tugmalarni chiqarish
        next_month_btn.draw(screen)
        shop_btn.draw(screen)
        bank_btn.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main_gui()
