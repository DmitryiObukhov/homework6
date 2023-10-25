import currency_convertor as conv

supported_currencies = list(conv.currency_rates.keys())
print('Current rates: ')
curs = list(conv.currency_rates.items())
print(curs)

while True:
    try:
        amount = float(input("Enter sum for exchange: "))
        break
    except ValueError:
        print("Ivnalid amount. Try again please.")

while True:
    from_currency = input("Enter the source currency: ").strip().upper()
    if from_currency in supported_currencies:
        break
    else:
        print("This currency unsupported. Try again please.")

while True:
    target_currency = input("Enter the target currency: ").strip().upper()
    if target_currency in supported_currencies:
        break
    else:
        print("This currency unsupported. Try again please.")

converted_amount = conv.convertor(amount, from_currency, target_currency)
print(f"{amount} {from_currency} = {converted_amount} {target_currency}")
