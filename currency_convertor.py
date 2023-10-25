def convertor(amount, from_currency, to_currency):
    if from_currency not in currency_rates:
        raise ValueError(f"'{from_currency}' not support")
    if to_currency not in currency_rates:
        raise ValueError(f"'{to_currency}' not support")
    amount_in_usd = amount / currency_rates[from_currency]
    converted_amount = amount_in_usd * currency_rates[to_currency]
    return round(converted_amount, 2)


currency_rates = {
    "USD": 1.0,
    "EUR": 0.95,
    "GBP": 0.82,
    "UAH": 36.53,
    "PLN": 4.23}