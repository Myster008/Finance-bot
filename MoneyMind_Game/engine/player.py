class Player:
    def __init__(self, name, target_money):
        self.name = name
        self.target_money = target_money  # Foydalanuvchi orzusidagi summa
        
        # Moliyaviy holat
        self.balance = 1000               # Naqd pul
        self.savings = 0                  # Jamg'arma (bankda)
        self.passive_income = 0           # Biznes yoki investitsiyadan
        self.stocks_value = 0
        # Hayotiy ko'rsatkichlar
        self.monthly_income = 500         # Boshlang'ich oylik
        self.monthly_expenses = 300       # Majburiy (oziq-ovqat, ijara)
        self.health = 100                 # Sog'liq (0 bo'lsa - o'yin tugaydi)
        self.age = 18                     # 18 yoshdan boshlaydi
        
    def check_victory(self):
        """Maqsadga erishilganini tekshirish"""
        total_wealth = self.balance + self.savings
        return total_wealth >= self.target_money

    def daily_update(self):
        """Har bir qadamda pulni va holatni yangilash"""
        # Majburiy xarajatlar balansdan ayiriladi
        self.balance -= (self.monthly_expenses / 30) 
        if self.balance < 0:
            return False # Bankrot
        return True
import json
import os

# Player klassi ichiga qo'shing:
def to_dict(self):
    return {
        "name": self.name,
        "target_money": self.target_money,
        "balance": self.balance,
        "savings": self.savings,
        "monthly_income": self.monthly_income,
        "monthly_expenses": self.monthly_expenses,
        "health": self.health,
        "age": self.age
    }

def save_game(self, filename="data/save_game.json"):
    os.makedirs('data', exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(self.to_dict(), f)
    return "O'yin saqlandi!"

@staticmethod
def load_game(filename="data/save_game.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            # Yangi player yaratib, yuklangan ma'lumotlarni yuklaymiz
            p = Player(data['name'], data['target_money'])
            p.balance = data['balance']
            p.savings = data['savings']
            p.monthly_income = data['monthly_income']
            p.monthly_expenses = data['monthly_expenses']
            p.health = data['health']
            p.age = data['age']
            return p
    return None
