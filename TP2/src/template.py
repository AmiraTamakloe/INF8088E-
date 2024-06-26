'''
    Creates the theme to be used in our bar chart.
'''
import plotly.graph_objects as go
import plotly.io as pio

THEME = {
    'bar_colors': [
        '#861388',
        '#d4a0a7',
        '#dbd053',
        '#1b998b',
        '#A0CED9',
        '#3e6680'
    ],
    'background_color': '#ebf2fa',
    'font_family': 'Montserrat',
    'font_color': '#898989',
    'label_font_size': 16,
    'label_background_color': '#ffffff'
}


def create_template():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary.

        The plot background and paper background
        are the background color defined
        above in the THEME dictionary.

        Also, sets the hover label to have a
        background color and font size
        as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. The hover mode
        is set to 'closest'.

        Also sets the colors for the bars in
        the bar chart to those defined in
        the THEME dictionary.

    '''
    template = go.layout.Template()
    template.layout.font.family = THEME['font_family']
    template.layout.font.color = THEME['font_color']
    template.layout.paper_bgcolor = THEME['background_color']
    template.layout.plot_bgcolor = THEME['background_color']
    template.layout.hoverlabel.bgcolor = THEME['label_background_color']
    template.layout.hoverlabel.font.size = THEME['label_font_size']
    template.layout.hoverlabel.font.color = THEME['font_color']
    template.layout.hovermode = 'closest'
    template.layout.colorway = THEME['bar_colors']
    pio.templates['our_template'] = template

    return 'our_template'