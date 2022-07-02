#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

# dash-labs plugin call, menu name and route
register_page(__name__, path="/storytelling")

from components.markdown.markformat import markformat
from components.maps.mapsample import mapsample

file1 = open('./data/mdsamples/story1.md')
file2 = open('./data/mdsamples/story2.md')
file3 = open('./data/mdsamples/story3.md')
file4 = open('./data/mdsamples/story4.md')



texto1  = markformat('Class Imbalance', file1.read())
texto2  = markformat('Correlation of our Variables', file2.read())
texto3  = markformat('What can we do?', file3.read())
texto4  = markformat('How representing is it?', file4.read())



mapa_ejemplo_story = mapsample('Mapa elecciones', 'id_mapa_story1')


# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H1(['Data Characterization'],id="div_title_maps"),
                 html.Hr()
            ], lg=12), 
           
        ]),

        dbc.Row([
            dbc.Col([
                 texto1.show()

            ], lg=4), 

            dbc.Col([
                 html.Img(src='/assets/CountByState.png', id='cbs', style={'height':'90%'})

            ], lg=8), 
   
        ]),


        dbc.Row([
            dbc.Col([
                 texto2.show()

            ], lg=4), 

            dbc.Col([
                 html.Img(src='/assets/PreliminarCorr.png', id='cbs', style={'height':'90%'})
                 

            ], lg=8), 
   
        ]),
        
        html.Hr(),
        
        dbc.Row([
            dbc.Col([
                 texto3.show()

            ], lg=4), 

            dbc.Col([
                 html.Img(src='/assets/FinalCorrelation.png', id='cbs', style={'height':'90%'})


            ], lg=8), 
   
        ]),
        
        dbc.Row([
            dbc.Col([
                 texto4.show()

            ], lg=4), 

            dbc.Col([
                 html.Img(src='/assets/Aporte.png', id='cbs', style={'height':'90%'})


            ], lg=8), 
   
        ]),



        
    ]
)