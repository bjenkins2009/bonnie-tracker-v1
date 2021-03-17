
# this will set the env variables for slack
import settings

import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash_extensions import Keyboard
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from slack_driver import slack_message
import datetime
from pytz import timezone

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

btn_attr = dict(size="lg",
                block=True,
                className="mr-1",
                style={'height': '10vh',
                       'font-size': '32px'},
                )
button_group = html.Div(
    [
        dbc.Button("Just Walk", id='button-walk', **btn_attr),
        dbc.Button("Pee", id='button-pee', **btn_attr),
        dbc.Button("Poop", id='button-poop', **btn_attr),
        dbc.Button("Fed", id='button-fed', **btn_attr)
    ],
    # vertical=True, size='lg'
)

app.layout = html.Div([
    button_group,
    dcc.Store(id='blank')
])

@app.callback(Output('blank', 'data'),
              Input('button-walk', 'n_clicks'),
              Input('button-pee', 'n_clicks'),
              Input('button-poop', 'n_clicks'))
def send_message(walk, pee, poop):
    cid = [p['prop_id'] for p in dash.callback_context.triggered][0]
    tz = timezone('US/Eastern')
    now = datetime.datetime.now(tz=tz)
    current_time = now.strftime("%H:%M:%S")

    if 'pee' in cid:
        slack_message(text=f'Bonnie peed at {current_time}')
    if 'poop' in cid:
        slack_message(text=f'Bonnie pooped at {current_time}')
    if 'walk' in cid:
        slack_message(text=f'Bonnie was out but did nothing at {current_time}')
    if 'fed' in cid:
        slack_message(text=f'Bonnie was fed at {current_time}')

if __name__ == '__main__':
    app.run_server(
        debug=True,
        # dev_tools_ui=True,
        # dev_tools_hot_reload=True,
    )

# slack_message(text='test')