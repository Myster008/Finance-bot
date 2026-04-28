class FinanceManager:
    @staticmethod
    def process_monthly_cycle(player):
        """Bir oylik moliyaviy jarayonni amalga oshirish"""
        
        # 1. Daromadlarni qo'shish
        total_income = player.monthly_income + player.passive_income
        player.balance += total_income
        
        # 2. Xarajatlarni ayirish
        player.balance -= player.monthly_expenses
        
        # 3. Yoshni oshirish (Har 12 oyda 1 yosh)
        # Bu mantiqni keyinchalik yosh tizimi qo'shganda kengaytiramiz
        
        # 4. Holatni tekshirish
        if player.balance < 0:
            player.is_alive = False
            return False, f"Bankrot! Balansingiz: {player.balance}$"
        
        return True, f"Oy yakunlandi. Daromad: +{total_income}$, Xarajat: -{player.monthly_expenses}$"
