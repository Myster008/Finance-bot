from engine.player import Player
from engine.finance import FinanceManager
from engine.shop import ShopManager
import time

def start_game():
    # ... boshqa initlar
    invest_manager = InvestmentManager()

    while player.is_alive:
        # Menyu qismiga qo'shamiz:
        print(f"Jamg'arma (Bank): ${player.savings:.2f}")
        print("3. Bank amallari (Omonat/Yechib olish)")
        
        choice = input("Tanlov: ")

        if choice == "1":
            # Oylik sikl ichida foizlarni ham hisoblaymiz
            interest = invest_manager.process_monthly_interest(player)
            success, msg = FinanceManager.process_monthly_cycle(player)
            print(f"{msg} | Bank foizi: +${interest:.2f}")
            # ...
            
        elif choice == "3":
            print("\n1. Pul qo'yish (Deposit)\n2. Pul yechish (Withdraw)")
            sub_choice = input("Tanlang: ")
            amount = float(input("Summani kiriting: "))
            if sub_choice == "1":
                s, m = invest_manager.deposit_to_bank(player, amount)
                print(m)
            elif sub_choice == "2":
                s, m = invest_manager.withdraw_from_bank(player, amount)
                print(m)
