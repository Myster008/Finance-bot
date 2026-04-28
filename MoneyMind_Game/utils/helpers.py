def draw_progress_bar(current, total, length=20):
    """Sog'liq yoki pul uchun vizual progress bar chizish"""
    percent = float(current) / total
    arrow = '-' * int(round(percent * length) - 1) + '>'
    spaces = ' ' * (length - len(arrow))
    return f"[{arrow + spaces}] {int(percent * 100)}%"

def format_currency(amount):
    """Pulni chiroyli formatda ko'rsatish: $1,250.00"""
    return f"${amount:,.2f}"
