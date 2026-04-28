import random

class EventManager:
    def __init__(self):
        # Hodisalar ro'yxati: (Nomi, Balansga ta'siri, Sog'liqqa ta'siri, Xabar)
        self.random_events = [
            {"name": "Kasal bo'lish", "money": -200, "health": -20, "msg": "Siz qattiq shamolladingiz. Dorilar va davolanishga pul ketdi."},
            {"name": "Mukofot puli", "money": 150, "health": 0, "msg": "Ishxonangizda yaxshi ishlaganingiz uchun bonus berildi!"},
            {"name": "Telefon buzilishi", "money": -300, "health": 0, "msg": "Ekraningiz sinib qoldi, uni tuzatish kerak."},
            {"name": "Tug'ilgan kun", "money": -100, "health": 10, "msg": "Do'stingizning tug'ilgan kuniga bordingiz. Mazza qildingiz, lekin sovg'aga pul ketdi."},
            {"name": "Jarima", "money": -50, "health": 0, "msg": "Yo'l harakati qoidasini buzganingiz uchun jarima keldi."},
            {"name": "Kutilmagan topilma", "money": 20, "health": 0, "msg": "Eski kurtkangiz cho'ntagidan pul topib oldingiz!"}
        ]

    def trigger_random_event(self, player):
        # 30% ehtimollik bilan hodisa sodir bo'ladi
        if random.random() < 0.3:
            event = random.choice(self.random_events)
            player.balance += event["money"]
            player.health += event["health"]
            return True, f"⚠️ KUTILMAGAN VOQEA: {event['msg']} (Pul: {event['money']}$, Sog'liq: {event['health']})"
        return False, ""
