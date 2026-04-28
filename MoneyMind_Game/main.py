from engine.player import Player
from engine.finance import FinanceManager
from engine.shop import ShopManager
import time

def start_game():
    # ... boshqa initlar
    invest_manager = InvestmentManager()

    while player.is_alive:
        print("\n" + "="*40)
        print(f" FOYDALANUVCHI: {player.name.upper()}")
        print(f" OY: {month_count} | YOSH: {player.age + (month_count // 12)}")
        print("="*40)
        
        # Vizual ko'rsatkichlar
        health_bar = draw_progress_bar(player.health, 100)
        target_bar = draw_progress_bar((player.balance + player.savings), player.target_money)
        
        print(f"SOG'LIQ: {health_bar}")
        print(f"MAQSAD:  {target_bar}")
        print("-"*40)
        print(f"HAMYON:  {format_currency(player.balance)}")
        print(f"BANK:    {format_currency(player.savings)}")
        print(f"OYLIK DAROMAD: {format_currency(player.monthly_income + player.passive_income)}")
        print("-"*40)
        
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
