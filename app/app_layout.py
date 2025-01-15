import FreeSimpleGUI as sg

from bin.imagetkhelper import ImageTKHelper

sg.theme('DefaultNoMoreNagging')

kolomLinks = sg.Column(
    key = '-KOLOM-LINKS-',
    scrollable = True,
    vertical_scroll_only = True,
    layout = [
        [
            sg.Listbox(
                values = [],
                key = '-LBX-MUNT-',
                no_scrollbar = True,
                size = (30, 16) 
            )
        ]
    ],
    size = (200, 290)
)

kolomRechts = sg.Column(
    scrollable = False,
    layout = [
        [
            sg.Image(
                key = '-IMG-KOPOFMUNT-',
                size = (200, 200)
            )
        ],
        [
            sg.Button(
                button_text = 'Werp',
                key = '-BTN-WERP-',
                size = (25, 2),
                expand_x = True
            )
        ],
        [
            sg.Button(
                button_text = 'Afsluiten',
                key = '-BTN-AFSLUITEN-',
                size = (25, 2),
                expand_x = True
            )
        ]
    ]
)

def appLayout():
    return[
        # RIJ 1
        [
            sg.Push(),
            sg.Image(
                source = 'assets/coin.png'
            ),
            sg.Text(
                text = 'KOP-OF-MUNT',
                font = ('Calibri', 20, 'bold')
            ),
            sg.Push()
        ],
        # RIJ 2
        [
            kolomLinks,
            sg.VerticalSeparator(
                pad = ((12, 12), (0, 0))
            ),
            kolomRechts
        ]
    ]