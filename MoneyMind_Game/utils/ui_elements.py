import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("Arial", 20, bold=True)

    def draw(self, screen):
        # Sichqoncha tugma ustida ekanini tekshirish
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        
        # Tugma soyasi va o'zi
        pygame.draw.rect(screen, (50, 50, 50), (self.rect.x + 3, self.rect.y + 3, self.rect.width, self.rect.height), border_radius=8)
        pygame.draw.rect(screen, current_color, self.rect, border_radius=8)
        
        # Matnni markazga qo'yish
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class ShopWindow:
    def __init__(self, x, y, width, height, shop_manager):
        self.rect = pygame.Rect(x, y, width, height)
        self.shop_manager = shop_manager
        self.is_visible = False
        self.font = pygame.font.SysFont("Arial", 18)
        self.title_font = pygame.font.SysFont("Arial", 24, bold=True)
        
        # Sotib olish tugmalari
        self.buy_buttons = {}
        self.update_buttons()

    def update_buttons(self):
        # Har bir mahsulot uchun alohida tugma yaratamiz
        y_offset = 80
        for key, item in self.shop_manager.items.items():
            btn = pygame.Rect(self.rect.x + self.rect.width - 100, self.rect.y + y_offset, 80, 30)
            self.buy_buttons[key] = btn
            y_offset += 60

    def draw(self, screen):
        if not self.is_visible:
            return

        # Oyna foni (shaffofroq qora fon ustidan oq oyna)
        overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=15)
        pygame.draw.rect(screen, (44, 62, 80), self.rect, 3, border_radius=15) # Ramka

        # Sarlavha
        title = self.title_font.render("DO'KON: O'zingizga investitsiya qiling", True, (44, 62, 80))
        screen.blit(title, (self.rect.x + 20, self.rect.y + 20))

        # Mahsulotlar ro'yxati
        y_offset = 80
        for key, item in self.shop_manager.items.items():
            name_txt = self.font.render(f"{item['name']} - ${item['cost']}", True, (0, 0, 0))
            desc_txt = self.font.render(item['desc'], True, (127, 140, 141))
            
            screen.blit(name_txt, (self.rect.x + 20, self.rect.y + y_offset))
            screen.blit(desc_txt, (self.rect.x + 20, self.rect.y + y_offset + 25))

            # Sotib olish tugmasi
            btn_rect = self.buy_buttons[key]
            pygame.draw.rect(screen, (46, 204, 113), btn_rect, border_radius=5)
            buy_txt = self.font.render("OLISH", True, (255, 255, 255))
            screen.blit(buy_txt, (btn_rect.x + 15, btn_rect.y + 5))
            
            y_offset += 60

        # Yopish ko'rsatmasi
        close_txt = self.font.render("Yopish uchun [ESC] bosing", True, (231, 76, 60))
        screen.blit(close_txt, (self.rect.x + self.rect.width // 2 - 80, self.rect.y + self.rect.height - 30))

    def handle_click(self, pos, player):
        if not self.is_visible:
            return False
            
        for key, btn_rect in self.buy_buttons.items():
            if btn_rect.collidepoint(pos):
                success, msg = self.shop_manager.buy_item(player, key)
                print(msg) # Bu yerda keyinchalik ekranda xabar chiqarishimiz mumkin
                return True
        return False
