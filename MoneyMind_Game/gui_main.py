import pygame
import os # Fayl yo'llarini to'g'ri ko'rsatish uchun
from engine.player import Player
from engine.finance import FinanceManager
from utils.ui_elements import Button

# Init va Oyna sozlamalari
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MoneyMind Simulyatori")
clock = pygame.time.Clock()

# --- ASSETLARNI YUKLASH FUNKSIYASI ---
def load_assets():
    assets = {}
    # Rasmlar joylashgan yo'lni aniqlash
    base_path = os.path.join("assets", "images")
    
    try:
        # Rasmlarni yuklash va o'lchamini moslash (alpha kanali bilan - shaffoflik)
        assets["player_happy"] = pygame.image.load(os.path.join(base_path, "player_happy.png")).convert_alpha()
        assets["player_sad"] = pygame.image.load(os.path.join(base_path, "player_sad.png")).convert_alpha()
        assets["icon_money"] = pygame.image.load(os.path.join(base_path, "icon_money.png")).convert_alpha()
        assets["icon_health"] = pygame.image.load(os.path.join(base_path, "icon_health.png")).convert_alpha()
        
        # O'yinchi rasmini kattaroq qilish
        assets["player_happy"] = pygame.transform.scale(assets["player_happy"], (120, 120))
        assets["player_sad"] = pygame.transform.scale(assets["player_sad"], (120, 120))
        # Ikonkalarni kichraytirish
        assets["icon_money"] = pygame.transform.scale(assets["icon_money"], (32, 32))
        assets["icon_health"] = pygame.transform.scale(assets["icon_health"], (32, 32))
        
    except pygame.error as e:
        print(f"Rasmlarni yuklashda xatolik: {e}")
        print("Iltimos, assets/images/ papkasida kerakli rasmlar borligini tekshiring.")
        # Agar rasm bo'lmasa, o'yin to'xtab qolmasligi uchun bo'sh sirt yaratish
        fallback_surf = pygame.Surface((32, 32))
        fallback_surf.fill((255, 0, 255)) # Fuksiy rang (xatolik belgisi)
        assets = {"player_happy": fallback_surf, "player_sad": fallback_surf, 
                  "icon_money": fallback_surf, "icon_health": fallback_surf}
        
    return assets

# Shriftlar
font = pygame.font.SysFont("Arial", 22)
bold_font = pygame.font.SysFont("Arial", 26, bold=True)

def draw_text(text, current_font, color, x, y):
    img = current_font.render(text, True, color)
    screen.blit(img, (x, y))

def main_gui():
    player = Player("Myster008", 75000)
    images = load_assets() # Rasmlarni yuklash
    running = True
    
    # Tugmalar
    next_month_btn = Button(580, 520, 200, 50, "KEYINGI OY", (46, 204, 113), (39, 174, 96))
    shop_btn = Button(20, 520, 180, 50, "DO'KON", (52, 152, 219), (41, 128, 185))
    bank_btn = Button(220, 520, 180, 50, "BANK", (155, 89, 182), (142, 68, 173))

    while running:
        screen.fill((236, 240, 241)) # Fon
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if next_month_btn.is_clicked(event):
                FinanceManager.process_monthly_cycle(player)
                # Oylik sikl ichida random event mantiqini ham gui_main.py ga ulash kerak bo'ladi

        # --- VIZUALIZATSIYA ---
        
        # 1. Header (Status paneli)
        pygame.draw.rect(screen, (44, 62, 80), (0, 0, 800, 100))
        draw_text(f"OY: {player.age * 12 + 1} (Yosh: {player.age})", bold_font, (255, 255, 255), 20, 20)
        
        # Pul va Sog'liqni ikonkalar bilan chiqarish
        screen.blit(images["icon_money"], (20, 60))
        draw_text(f"Balans: ${player.balance:,.2f}", font, (46, 204, 113), 60, 62)
        
        screen.blit(images["icon_health"], (300, 60))
        draw_text(f"Sog'liq: {player.health}%", font, (231, 76, 60), 340, 62)

        # 2. O'yinchi personaji (Sog'liqqa qarab rasm o'zgaradi)
        player_image = images["player_happy"] if player.health > 50 else images["player_sad"]
        # Rasmni markazga joylashtirish
        img_rect = player_image.get_rect(center=(400, 300))
        screen.blit(player_image, img_rect)
        
        # 3. Maqsad Progress Bar (Tepada)
        pygame.draw.rect(screen, (127, 140, 141), (550, 30, 230, 20), border_radius=10) # Fon
        current_wealth = player.balance + player.savings
        progress_width = min(230 * (current_wealth / player.target_money), 230)
        pygame.draw.rect(screen, (46, 204, 113), (550, 30, progress_width, 20), border_radius=10) # To'lish
        draw_text("Maqsad", font, (255, 255, 255), 630, 5)

        # 4. Tugmalar
        next_month_btn.draw(screen)
        shop_btn.draw(screen)
        bank_btn.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main_gui()
