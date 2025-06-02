import FreeSimpleGUI as sg

sg.theme('LightBlue3')

class AppLayout:
    def create_layout(self, currency_options):
        logo_and_title = sg.Column(
            [
                [
                    sg.Image(
                        filename = 'assets/coin.png', 
                        size = (40, 40), 
                        pad = (0, 0)
                    ),
                    sg.Text(
                        'Frankfurter', 
                        font = ('Calibri', 24, 'bold'), 
                        pad = ((10, 0), (5, 5))
                    )
                ]
            ],
            justification = 'center',
            element_justification = 'center',
            expand_x = True
        )
        layout = [
            [
                logo_and_title
            ],
            [
                sg.HorizontalSeparator(
                    color = '#4a90e2', 
                    pad = (0, 10)
                )
            ],
            [
                sg.Frame(
                    'Te converteren', 
                    layout = [
                        [
                            sg.Text(
                                'Munt van:', 
                                size = (10, 1), 
                                pad = ((10, 5), (10, 10))
                            ),
                            sg.Combo(
                                currency_options, 
                                key = '-MUNT-VAN-', 
                                size = (20, 1), 
                                pad = (0, 10), 
                                readonly = True
                            ),
                            sg.Text(
                                'Bedrag van:', 
                                size = (10, 1), 
                                pad = ((20, 5), (10, 10))
                            ),
                            sg.Input(
                                key = '-BEDRAG-VAN-', 
                                size = (15, 1), 
                                justification = 'right', 
                                pad = (10, 10)
                            )
                        ]
                    ], 
                    pad = ((10, 10), (0, 10)), 
                    relief = sg.RELIEF_RIDGE, 
                    border_width = 2, 
                    expand_x = True
                )
            ],
            [
                sg.Frame(
                    'Geconverteerd', 
                    layout = [
                        [
                            sg.Text(
                                'Munt naar:', 
                                size = (10, 1), 
                                pad = ((10, 5), (10, 10))
                            ),
                            sg.Combo(
                                currency_options, 
                                key = '-MUNT-NAAR-', 
                                size = (20, 1), 
                                pad = (0, 10), 
                                readonly = True
                            ),
                            sg.Text(
                                'Bedrag naar:', 
                                size = (10, 1), 
                                pad = ((20, 5), (10, 10))
                            ),
                            sg.Input(
                                key = '-BEDRAG-NAAR-', 
                                size = (15, 1), 
                                justification = 'right', 
                                disabled = True, 
                                pad = (10, 10)
                            )
                        ]
                    ], 
                    pad = ((10, 10), (0, 10)), 
                    relief = sg.RELIEF_RIDGE, 
                    border_width = 2, 
                    expand_x = True
                )
            ],
            [
                sg.HorizontalSeparator(
                    color = '#4a90e2', 
                    pad = (0, 15)
                )
            ],
            [
                sg.Text(
                    'Wisselkoers:', 
                    key = '-WISSELKOERS-', 
                    font = ('Calibri', 12), 
                    pad = ((10, 0), (0, 0)), 
                    expand_x = True
                ),
                sg.Button(
                    'App afsluiten', 
                    key = '-BTN-AFSLUITEN-', 
                    size = (17, 2), 
                    button_color = ('white', '#4a90e2'), 
                    border_width = 0, 
                    pad = ((10, 10), (0, 0))
                )
            ]
        ]
        return layout