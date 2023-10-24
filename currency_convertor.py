def convertor(amount, rates):
    return round(amount * rates, 3)


currency_rates = {
    "USD": 36.57,
    "EUR": 38.79,
    "GBP": 44.55, }


print("Choose your currency.")
while True:
    try:
        choice = int(input("1 - USD, 2 - EUR, 3 - GBP : "))
        if choice not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Choose currency 1 - 3.")
        continue

    user_amount = int(input("Your amount: "))

    if choice == 1:
        result = convertor(user_amount, currency_rates["USD"])
        print(f"{user_amount} USD = {result} UAH")
    elif choice == 2:
        result = convertor(user_amount, currency_rates["EUR"])
        print(f"{user_amount} EUR = {result} UAH")
    elif choice == 3:
        result = convertor(user_amount, currency_rates["GBP"])
        print(f"{user_amount} GBP = {result} UAH")
    break
