import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import config

app = dash.Dash(__name__,
                meta_tags=[
                    {
                        'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1, shrink-to-fit=no',
                        'charset':'utf-8'
                    }
                ])

app.title = config.layout['appTitle']

app.layout = html.Div([

	dcc.Interval(
        id='interval-component',
        interval=config.updateTime*1000, # in milliseconds
        n_intervals=0
    ),

    html.Div([
    	html.H1(config.layout['headingText'], className='text-muted', style={'font-size':str(config.layout['headingSize'])+'px'}),
    	html.Br(),
        html.Br(),
    	html.H1(id='text-update', className='font-weight-bold text-primary', style={'font-size':str(config.layout['dataSize'])+'px'}),
    ],className='container-fluid text-center')

],className='jumbotron d-flex align-items-center min-vh-100', style={'margin':'0px', 'padding':'0px', 'font-family': 'Comic Sans MS , cursive, sans-serif'})

@app.callback(
    Output('text-update', 'children'),
    [Input('interval-component', 'n_intervals')])
def update(n):
	return config.data()

if __name__ == '__main__':
    app.run_server(debug=True)