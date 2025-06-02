from datetime import datetime
import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = 'https://api.frankfurter.app'
        self.currencies = self._load_currencies()

    def _load_currencies(self):
        try:
            response = requests.get(f'{self.api_url}/currencies')
            data = response.json()
            return list(data.keys())
        except:
            return ['EUR', 'USD', 'GBP']

    def get_currency_options(self):
        return self.currencies

    def convert(self, from_currency, to_currency, amount):
        if from_currency == to_currency:
            today = datetime.today().strftime('%d %B %Y')
            return amount, today

        response = requests.get(
            f"{self.api_url}/latest",
            params = {"amount": amount, "from": from_currency, "to": to_currency}
        )
        data = response.json()
        rate = data['rates'][to_currency]
        date_str = data['date']

        formatted_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d %B %Y')

        return rate, formatted_date