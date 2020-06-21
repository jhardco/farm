import plotly
import geopandas as gpd
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

ele = pd.read_csv(r'D:\desktopcopy\farmsurface.csv', names=['x','y','z'])
z_values= pd.DataFrame(ele['z'].values.reshape(-1, len(ele['x'].unique())), index=ele['y'].unique(),columns=ele['x'].unique())
fig = go.Figure(data=[go.Surface(z=z_values,x=z_values.columns,y=z_values.index,colorscale=px.colors.sequential.deep[::-1],colorbar=dict(title = 'Meters Above Sea Level'))])
fig.update_layout(title=dict(text='Farm Surface Elevation',font=dict(family='Century Gothic',size=24, color = "#6495ED")), autosize=False,
                  width=1200, height=1000,paper_bgcolor='black', plot_bgcolor='black',
                 font=dict(
                    family="Century Gothic, monospace",
                    size=14,
                    color="#6495ED"
                ))
fig.update_layout(
    scene = dict(zaxis = dict(nticks=5, range=[1050,1100])),
    margin=dict(r=20, l=10, b=10, t=45))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Deahl Farm SUrface Elevations',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(children='An app to visualize surfaces for fun.', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        dcc.Graph(id = 'October Counts',figure=fig, style={'textalign':'center'})
])

if __name__ == '__main__':
    app.run_server(debug=True)




import sys

print(sys.version)
