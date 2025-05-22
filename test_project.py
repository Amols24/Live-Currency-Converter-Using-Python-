import unittest
from unittest.mock import patch, Mock
from currency_converter import rate_parser, convert, currencies

class TestCurrencyConverter(unittest.TestCase):

    @patch('currency_converter.requests.get')
    def test_rate_parser_success(self, mock_get):
        # Mock the HTML response content
        mock_html = """
        <html>
        <body>
            <span class="DFlfde SwHCTb">0.85</span>
        </body>
        </html>
        """
        mock_get.return_value = Mock(text=mock_html)

        # Test the rate_parser function
        rate = rate_parser("USD", "EUR")
        self.assertEqual(rate, 0.85)

    @patch('currency_converter.requests.get')
    def test_rate_parser_failure(self, mock_get):
        # Mock the HTML response with incorrect content
        mock_get.return_value = Mock(text="<html></html>")

        # Test the rate_parser function when no rate is found
        rate = rate_parser("USD", "EUR")
        self.assertIsNone(rate)

    @patch('currency_converter.rate_parser')
    def test_convert_success(self, mock_rate_parser):
        # Mock the rate_parser function
        mock_rate_parser.return_value = 0.85

        # Test the convert function
        rate, converted_amount = convert("USD", "EUR", 100)
        self.assertEqual(rate, 0.85)
        self.assertEqual(converted_amount, 85.0)

    @patch('currency_converter.rate_parser')
    def test_convert_failure(self, mock_rate_parser):
        # Mock the rate_parser function to return None
        mock_rate_parser.return_value = None

        # Test the convert function when rate_parser fails
        rate, converted_amount = convert("USD", "EUR", 100)
        self.assertIsNone(rate)
        self.assertIsNone(converted_amount)

    def test_get_valid_currency_input(self):
        with patch('builtins.input', return_value='USD'):
            result = get_valid_currency_input("Enter currency: ", currencies)
            self.assertEqual(result, 'USD')

        with patch('builtins.input', side_effect=['XYZ', 'EUR']):
            result = get_valid_currency_input("Enter currency: ", currencies)
            self.assertEqual(result, 'EUR')

if __name__ == '__main__':
    unittest.main()
