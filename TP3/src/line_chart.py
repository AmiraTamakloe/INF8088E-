'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template
import plotly.graph_objects as go
import pandas as pd

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. 
        Select a cell in the heatmap for more information.
        MUMU'S NOTE: WHAT DOES THE ABOVE MEAN
    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    fig = go.Figure()

    fig.add_annotation(
        text='No data to display. Select a cell in the heatmap for more information.',
        xref='paper',
        yref='paper',
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=15)
    )

    fig.update_layout(
        dragmode=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )

    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle

    pale_color = THEME['pale_color']

    fig.add_shape(
        type='rect',
        x0=0, x1=1, y0=0.25, y1=0.75,
        xref='paper', yref='paper',
        line=dict(width=0),
        fillcolor=pale_color
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        paper_bgcolor=pale_color,
        plot_bgcolor=pale_color,
        shapes=[
            dict(
                type='rect',
                x0=0,
                x1=1,
                y0=0.25,
                y1=0.75,
                xref='paper',
                yref='paper',
                line=dict(width=0),
                fillcolor=pale_color
            )
        ]
    )

    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template

    line_data['Date_Plantation'] = pd.to_datetime(line_data['Date_Plantation'])
    filtered_data = line_data[(line_data['Date_Plantation'].dt.year == year) & (line_data['Arrond_Nom'] == arrond)]

    # Generate the line chart
    fig = px.line(
        filtered_data,
        x='Date_Plantation',
        y='Trees',
        title=f'{arrond} - {year}',
        labels={
            'Date_Plantation': 'Date',
            'Trees': 'Trees'
        }
    )

    fig.update_layout(
        xaxis=dict(
            tickformat="%d-%b",
            tickmode="linear",
            dtick="M1"
        ),
        yaxis_title='Trees',
        title={
            'text': f'{arrond} - {year}',
            'x': 0.5
        }
    )

    # Handle the case with only one data point
    if len(filtered_data) == 1:
        fig.update_traces(mode='markers')

    fig.show()

    return fig
