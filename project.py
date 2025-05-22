import requests
from bs4 import BeautifulSoup

def rate_parser(input_curr, output_curr):
    query = f"{input_curr} to {output_curr} exchange rate"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure we raise an exception for HTTP errors
        content = response.text

        # Debugging: Print the first 1000 characters of the page content
        print("Debug: Page content snippet:")
        print(content[:1000])

        soup = BeautifulSoup(content, 'html.parser')

        # Find the exchange rate element
        result_element = soup.find("span", class_="DFlfde SwHCTb")
        if result_element:
            currency_text = result_element.get_text().replace(',', '')  # Remove comma
            rate = float(currency_text.split()[0])
            return rate
        else:
            print(f"Element not found for {input_curr} to {output_curr}.")
            return None
    except requests.RequestException as req_err:
        print(f"Request error: {req_err}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def convert(base, dest, amount):
    rate = rate_parser(base, dest)
    if rate is not None:
        new_amount = rate * amount
        return rate, new_amount
    else:
        return None, None

currencies = ["USD", "EUR", "CAD", "MAD", "GBP", "AUD", "JPY"]

def get_valid_currency_input(prompt, valid_currencies):
    user_input = input(prompt).upper()
    while user_input not in valid_currencies:
        print("Invalid currency entered. Please choose from the supported currencies.")
        user_input = input(prompt).upper()
    return user_input

def print_supported_currencies():
    print("Supported Currencies: ", ", ".join(currencies))

def main():
    print("Welcome to the Currency Converter!")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print_supported_currencies()

    base = get_valid_currency_input("Enter source currency: ", currencies)
    print_supported_currencies()

    dest = get_valid_currency_input("Enter destination currency: ", currencies)

    current_rate, converted_amount = convert(base, dest, amount)
    if current_rate is not None and converted_amount is not None:
        print("\nConversion Result:")
        print(f"Amount: {amount} {base}")
        print(f"From currency: {base}")
        print(f"To currency: {dest}")
        print(f"Current exchange rate: 1 {base} = {current_rate} {dest}")
        print(f"Converted amount: {converted_amount:.2f} {dest}")
    else:
        print("Conversion could not be completed. Please try again later.")

if __name__ == '__main__':
    main()
