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
