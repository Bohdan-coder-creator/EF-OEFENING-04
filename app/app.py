import FreeSimpleGUI as sg

from .app_layout import appLayout
from entiteit.kopofmunt import KopOfMunt
from bin.imagetkhelper import ImageTKHelper

class App:
    def __init__(self):
        self._kopOfMunt = KopOfMunt()

    def toon(self):
        venster = sg.Window(
            title = 'KOP-OF-MUNT',
            icon = 'assets/coin.png',
            layout = appLayout(),
            resizable = False,
            disable_close = True
        )

        while True:
            evt, vals = venster.read()

            match evt:
                case sg.WIN_CLOSED | '-BTN-AFSLUITEN-':
                    break

                case '-BTN-WERP-':
                    worp = self._kopOfMunt.werp()
                    venster['-IMG-KOPOFMUNT-'].update(data = ImageTKHelper.schaal(f'assets/{worp}.png', grootte = (200, 200)))
                    geschiedenis = self._kopOfMunt.geschiedenis()
                    venster['-LBX-MUNT-'].update(values = geschiedenis)

        venster.close()