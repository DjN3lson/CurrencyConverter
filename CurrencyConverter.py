def convert_currency(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': {'EUR': 0.92, 'CAD': 1.35, 'MXN': 16.88},
        'EUR': {'USD': 1.09, 'CAD': 1.47, 'MXN': 18.40},
        'CAD': {'USD': 0.74, 'EUR': 0.68, 'MXN': 12.49},
        'MXN': {'USD': 0.059, 'EUR': 0.054, 'CAD': 0.080}
    }

    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        exchange_rates = exchange_rates[from_currency][to_currency]
        converted_amount = amount * exchange_rates
        return converted_amount
    else:
        return None

def main():
    amount = float(input("Enter the amount:"))
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} equals {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency pair or currency not supported.")
    
if __name__ == "__main__":
    main()