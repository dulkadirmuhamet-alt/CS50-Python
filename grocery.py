payment = int(input("Insert Coin: "))

if payment == 25 or payment == 10 or payment == 5:
    remaining = 50 - payment
else:
    remaining = 50
while remaining > 0:
    print("Amount Due: ", remaining)
    next_coin = int(input("Insert Coin: "))

    if next_coin == 25 or next_coin == 10 or next_coin == 5:
        remaining = remaining - next_coin

if remaining <= 0:
    print("Change Owed:",abs(remaining))






