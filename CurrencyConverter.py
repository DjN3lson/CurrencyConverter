import requests as rq

def get_exchange_rates(api_key, base_currency, target_currency):

    """
    Get the exchange rate for converting from a base currency to a target currency.
    
    Parameters:
        api_key (str): API key for accessing the Open Exchange Rates API.
        base_currency (str): Base currency code (e.g., 'USD').
        target_currency (str): Target currency code (e.g., 'EUR').
    
    Returns:
        float or None: Exchange rate from base to target currency, or None if an error occurs.
    """

    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    headers = {"Authorization": f"Token {api_key}"}
    
    try:
        response = rq.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse JSON response
        
        # Extract exchange rate for target currency
        exchange_rate = data['rates'].get(target_currency)
        return exchange_rate
    
    except rq.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except rq.exceptions.JSONDecodeError as e:
        print(f"JSON decoding error occurred: {e}")
    
    return None

def convert_currency(amount, from_currency, to_currency, exchange_rate):

    """
    Convert an amount from one currency to another using the given exchange rate.
    
    Parameters:
        amount (float): Amount to convert.
        from_currency (str): Currency code to convert from.
        to_currency (str): Currency code to convert to.
        exchange_rate (float): Exchange rate from base to target currency.
    
    Returns:
        float or None: Converted amount, or None if exchange rate is not provided.
    """

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

def main():

    """
    Main function to execute the currency converter.
    
    Prompts user for amount, base currency, and target currency.
    Fetches exchange rate from Open Exchange Rates API.
    Converts amount using exchange rate and prints result.
    """

    api_key = '41019c2df0a8434c83f6c1c505d76c21'
    amount = float(input("Enter the amount:"))
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()

    exchange_rate = get_exchange_rates(api_key, from_currency, to_currency)
    if exchange_rate is not None:
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rate)
        print(f"{amount} {from_currency} equals {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency pair or currency not supported.")
    
if __name__ == "__main__":
    main()