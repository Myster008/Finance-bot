import random

class InvestmentManager:
    def __init__(self):
        self.bank_interest_rate = 0.02  # Bank omonati uchun oyiga 2%
        self.stock_market_trend = 1.0   # Bozor holati

    def deposit_to_bank(self, player, amount):
        if player.balance >= amount:
            player.balance -= amount
            player.savings += amount
            return True, f"${amount} bankka omonat sifatida qo'yildi."
        return False, "Mablag' yetarli emas!"

    def withdraw_from_bank(self, player, amount):
        if player.savings >= amount:
            player.savings -= amount
            player.balance += amount
            return True, f"Bankdan ${amount} pul yechib olindi."
        return False, "Bankda buncha pulingiz yo'q!"

    def update_market(self):
        """Aksiya bozoridagi o'zgarish (tasodifiy)"""
        # Bozor -5% dan +10% gacha o'zgarishi mumkin
        change = random.uniform(-0.05, 0.10)
        self.stock_market_trend = 1 + change
        return change

    def process_monthly_interest(self, player):
        """Oylik foizlarni hisoblash"""
        interest = player.savings * self.bank_interest_rate
        player.savings += interest
        return interest
