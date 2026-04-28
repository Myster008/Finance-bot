from engine.player import Player
from engine.finance import FinanceManager
from engine.shop import ShopManager
import time

def start_game():
    # ... (oldingi kod: ism va maqsad kiritish)
    shop = ShopManager()
    
    while player.is_alive:
        print(f"\n--- {month_count}-oy | Balans: ${player.balance:.2f} | Sog'liq: {player.health} ---")
        print("1. Keyingi oyga o'tish (Oylik va Xarajatlar)")
        print("2. Do'kon va Ta'lim (Investitsiya o'ziga)")
        print("3. O'yinni tugatish")
        
        choice = input("Tanlov: ")
        
        if choice == "1":
            success, message = FinanceManager.process_monthly_cycle(player)
            print(message)
            # ... (victory va bankrot tekshiruvi)
            
        elif choice == "2":
            shop.show_menu()
            item_choice = input("Nima sotib olasiz? (0-bekor qilish): ")
            if item_choice != "0":
                bought, msg = shop.buy_item(player, item_choice)
                print(msg)
