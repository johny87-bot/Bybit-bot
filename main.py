import ccxt

# Налаштування підключення до Bybit
exchange = ccxt.bybit({
    'apiKey': '4MdvQ4d3oxeMJ4b8Xk',
    'secret': 'QCkZgvwuDLjE7G2p4T6qR5KGmJC4ZOzSZJKi',
})

# Отримання балансу
try:
    balance = exchange.fetch_balance()
    print("Баланс:", balance)
except Exception as e:
    print("Помилка підключення:", str(e))
