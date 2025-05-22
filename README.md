
My project’s title:				                Currency Converter
My name:					                    Amol Sadare
My GitHub and edX usernames:			        Amols24,	amol_114
My city and country:				            India 	Mumbai
and, the date you have recorded this video: 	08-09-2024

Watch the Video Demo https://youtu.be/dCjKTMLGQvg
Description

Currency Converter

This Python script converts currency amounts based on real-time exchange rates retrieved from Google search results.
Overview

The Currency Converter script fetches exchange rates by querying Google for currency conversion rates and calculates the equivalent amount in the target currency.
Features

    Convert amounts between various currencies.
    Fetch exchange rates directly from Google search results.
    Display the conversion result along with the current exchange rate.

Requirements

    Python 3.x
    requests library
    beautifulsoup4 library

Installation

    Clone the Repository (if applicable):

    bash

git clone <repository-url>
cd <repository-directory>

Install the Required Libraries: You can install the required Python libraries using pip:

bash

    pip install requests beautifulsoup4

Usage

    Run the Script:

    bash

    python currency_converter.py

    Follow the Prompts:
        Enter the amount you want to convert.
        Choose the source currency from the supported currencies.
        Choose the destination currency from the supported currencies.

    View the Conversion Result: The script will display the converted amount along with the current exchange rate.

Example

yaml

Welcome to the Currency Converter!
Enter the amount: 100
Supported Currencies: USD, EUR, CAD, MAD, GBP, AUD, JPY
Choose the source currency:
Enter source currency: USD
Supported Currencies: USD, EUR, CAD, MAD, GBP, AUD, JPY
Choose the destination currency:
Enter destination currency: EUR

Conversion Result:
Amount: 100 USD
From currency: USD
To currency: EUR
Current exchange rate: 1 USD = 0.85 EUR
Converted amount: 85.00 EUR

Notes

    Web Scraping Limitations: The script uses web scraping to fetch exchange rates from Google search results. Changes in Google's HTML structure may affect the script's ability to retrieve data. Ensure that you comply with Google's terms of service when scraping their content.
    Currency Support: The script supports a predefined list of currencies. You can modify the currencies list in the script to add or remove currencies.

Troubleshooting

    No Exchange Rate Found: If the script cannot find the exchange rate, verify that the HTML structure of the Google search results page has not changed. Update the class names in the rate_parser function if necessary.
    Network Issues: Ensure you have a stable internet connection and that there are no issues accessing Google's search results page.
