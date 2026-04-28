from engine.player import Player
from engine.finance import FinanceManager
from engine.shop import ShopManager
import time

def start_game():
    # ... (oldingi kodlar)
    shop = ShopManager()
    event_manager = EventManager() # Yangi obyekt
    
    while player.is_alive:
        # ... (menyu ko'rsatish)
        
        if choice == "1":
            # 1. Avval oylik moliya hisoblanadi
            success, message = FinanceManager.process_monthly_cycle(player)
            print(message)
            
            # 2. Keyin tasodifiy hodisa sodir bo'lishini tekshiramiz
            happened, event_msg = event_manager.trigger_random_event(player)
            if happened:
                print(event_msg)
            
            # 3. O'yin yakunini tekshirish
            if player.health <= 0:
                print("\nSog'lig'ingiz yomonlashdi. O'yin tugadi!")
                player.is_alive = False
            # ... (bankrot va g'alaba tekshiruvi)
