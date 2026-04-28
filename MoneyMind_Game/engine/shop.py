class ShopManager:
    def __init__(self):
        # Do'kondagi narsalar ro'yxati
        self.items = {
            "1": {"name": "Sifatli ovqat", "cost": 100, "health_gain": 10, "desc": "Sog'liqni tiklaydi, lekin qimmat."},
            "2": {"name": "Onlayn Kurs (Moliya)", "cost": 300, "income_boost": 50, "desc": "Oylik maoshingizni doimiy +50$ ga oshiradi."},
            "3": {"name": "Sport zaliga a'zolik", "cost": 50, "health_gain": 5, "desc": "Har oy sog'liqni barqaror ushlaydi."},
            "4": {"name": "Eski Velosiped", "cost": 150, "expense_reduction": 20, "desc": "Transport xarajatlarini kamaytiradi."}
        }

    def show_menu(self):
        print("\n--- DO'KON VA RIVOJLANISH ---")
        for key, item in self.items.items():
            print(f"{key}. {item['name']} - ${item['cost']} | {item['desc']}")
        print("0. Orqaga")

    def buy_item(self, player, choice):
        if choice in self.items:
            item = self.items[choice]
            if player.balance >= item['cost']:
                player.balance -= item['cost']
                
                # Sotib olingan narsaning ta'siri
                if "health_gain" in item:
                    player.health += item['health_gain']
                if "income_boost" in item:
                    player.monthly_income += item['income_boost']
                if "expense_reduction" in item:
                    player.monthly_expenses -= item['expense_reduction']
                
                return True, f"Muvaffaqiyatli sotib olindi: {item['name']}"
            else:
                return False, "Mablag' yetarli emas!"
        return False, "Noto'g'ri tanlov!"
