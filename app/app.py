import FreeSimpleGUI as sg
from entiteit.converter import CurrencyConverter
from app.app_layout import AppLayout

class App:
    def __init__(self):
        self.converter = CurrencyConverter()
        self.currency_options = self.converter.get_currency_options()
        self.layout = AppLayout().create_layout(self.currency_options)
        self.window = sg.Window('Frankfurter', self.layout, finalize = True)

    def run(self):
        while True:
            event, values = self.window.read(timeout = 100)

            if event == sg.WIN_CLOSED or event == '-BTN-AFSLUITEN-':
                break

            from_currency = values['-MUNT-VAN-']
            to_currency = values['-MUNT-NAAR-']
            amount = values['-BEDRAG-VAN-']

            if from_currency and to_currency and amount.replace('.', '', 1).isdigit():
                converted, rate = self.converter.convert(from_currency, to_currency, float(amount))
                self.window['-BEDRAG-NAAR-'].update(value = f'{converted:.2f}')
                self.window['-WISSELKOERS-'].update(value = f'Wisselkoers: {rate}')

        self.window.close()