import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import config
import datetime as dt
#######################################################
# This script is for reading from  a table in cassandra #
#######################################################
print('CHECKKKKKKKKK!!!!!!!')

from cassandra.cluster import Cluster

# from cassandra-driver import Cluster
# import config

CASSANDRA_NAMESPACE = config.KEYSPACE

cluster = Cluster(config.CASSANDRA_CLUSTER)  # config.CASSANDRA
session = cluster.connect()

session.execute('USE ' + CASSANDRA_NAMESPACE)
result1 = session.execute("SELECT dt,pressure,oil_bbl,water_bbl  FROM oil_production WHERE well_name = 'Well 1' ALLOW FILTERING")
result2 = session.execute("SELECT dt,pressure,oil_bbl,water_bbl  FROM oil_production WHERE well_name = 'Well 2' ALLOW FILTERING")
result3 = session.execute("SELECT dt,pressure,oil_bbl,water_bbl  FROM oil_production WHERE well_name = 'Well 3' ALLOW FILTERING")
date_x =[]
pressure1_y = []
oil1_y=[]
water1_y=[]
pressure2_y = []
oil2_y=[]
water2_y=[]
pressure3_y = []
oil3_y=[]
water3_y=[]
for row in result1:
        date_x.append(str(row.dt))
        pressure1_y.append(row.pressure)
        oil1_y.append(row.oil_bbl)
        water1_y.append(row.water_bbl)

for row in result2:
        pressure2_y.append(row.pressure)
        oil2_y.append(row.oil_bbl)
        water2_y.append(row.water_bbl)
for row in result3:
        pressure3_y.append(row.pressure)
        oil3_y.append(row.oil_bbl)
        water3_y.append(row.water_bbl)

#######################################################
# Setup Website with Dash #
#######################################################

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Intruder'),

    html.Div(children='''
        Oil Well Interference
        '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                go.Scatter(x = date_x,
                           y = pressure1_y,
                           mode = 'lines',
                           name = 'lines'),
                go.Scatter(x = date_x,
                           y = pressure2_y,
                           mode = 'lines',
                           name = 'lines'),
               go.Scatter(x = date_x,
                           y = pressure3_y,
                           mode = 'lines',
                           name = 'lines')
            ],
            'layout': go.Layout(
                yaxis=dict(range=[600,950]),
            )
        }
    ),

    dcc.Graph(
        id='example-2graph',
        figure={
            'data':[
                go.Scatter(x = date_x,
                           y = oil1_y,
                           mode = 'lines',
                           name = 'lines'),
                go.Scatter(x = date_x,
                           y = oil2_y,
                           mode = 'lines',
                           name = 'lines'),
               go.Scatter(x = date_x,
                           y = oil3_y,
                           mode = 'lines',
                           name = 'lines')
            ],
            'layout': go.Layout(
                yaxis=dict(range=[650,1550]),
            )
        }
    ),

    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=4 * 1000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    sql = "SELECT id, pressure_1, pressure_2, pressure_3, pressure_4 from well_pressure"
    stream_result = session.execute(sql)
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    t = []
    for row in stream_result:
        t.append(row.id)
        p1.append(row.pressure_1)
        p2.append(row.pressure_2)
        p3.append(row.pressure_3)
p4.append(row.pressure_4)
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 60, 'r': 60, 'b': 30, 't': 10
    }
    fig['layout']['xaxis'] = {'title': 'Time (seconds)'}
    fig['layout']['yaxis'] = {'title': 'pressure(psi)'}
    fig['layout']['yaxis'] = dict(range=[300,950])
    fig.append_trace(go.Scatter(
        x=t,
        y=p1,
        name='well 1',
        mode='lines+markers'
    ), 1, 1)
    fig.append_trace(go.Scatter(
        x=t,
        y=p2,
        name='well 2',
        mode='lines+markers'
    ), 1, 1)
    fig.append_trace(go.Scatter(
        x=t,
        y=p3,
        name='well 3',
        mode='lines+markers'
    ), 1, 1)
    fig.append_trace(go.Scatter(
        x=t,
        y=p4,
        name='well 4',
        mode='lines+markers'
    ), 1, 1)
 return fig




if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=80)
