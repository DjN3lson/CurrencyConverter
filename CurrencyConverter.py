import requests as rq

def get_exchange_rates(api_key, base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latetst/{base_currency}"
    headers = {"Authorization": f"Token {api_key}"}
    response = rq.get(url, headers=headers)
    data = response.json()

    if rq.status_codes == 200:
        return data['rates'].get(target_currency)
    else:
        print("Failed to fetch exchange rate:", data.get('error'))
        return None

def convert_currency(amount, from_currency, to_currency, exchange_rate):
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

def main():
    api_key = '41019c2df0a8434c83f6c1c505d76c21'
    amount = float(input("Enter the amount:"))
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()

    exchange_rate = get_exchange_rates(api_key, from_currency, to_currency)
    if exchange_rate is not None:
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rate)
        print(f"{amount} {from_currency} equals {convert_currency:.2f} {to_currency}")
    else:
        print("Invalid currency pair or currency not supported.")
    
if __name__ == "__main__":
    main()