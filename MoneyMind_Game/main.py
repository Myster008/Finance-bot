from engine.player import Player
from engine.finance import FinanceManager
import time

def start_game():
    print("--- MOLIYAVIY ERKINLIK O'YINIGA XUSH KELIBSIZ ---")
    name = input("Ismingizni kiriting: ")
    try:
        target = float(input("Maqsadingiz (necha pul yig'moqchisiz?): "))
    except ValueError:
        target = 100000.0 # Default maqsad

    player = Player(name, target)
    month_count = 0

    while player.is_alive:
        month_count += 1
        print(f"\n--- {month_count}-oy ---")
        print(player.get_status())
        
        print("\n1. Keyingi oyga o'tish")
        print("2. Investitsiya qilish (tez kunda)")
        print("3. O'yinni tugatish")
        
        choice = input("Tanlang: ")
        
        if choice == "1":
            success, message = FinanceManager.process_monthly_cycle(player)
            print(message)
            
            if player.check_victory():
                print(f"\nTABRIKLAYMIZ! Siz {month_count} oyda maqsadga erishdingiz!")
                break
            if not success:
                print("\nO'YIN TUGADI. Siz kambag'allikdan chiqa olmadingiz.")
                break
        elif choice == "3":
            break
        else:
            print("Hozircha faqat 1-tugma ishlaydi!")

if __name__ == "__main__":
    start_game()
