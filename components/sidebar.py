import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout = dbc.Col([
                html.H1('MyBudget', className='text-primary'),
                html.P('By ASIMOV', className='text-info'), # classname = extrair as cores a partir dos temas
                html.Hr(),

    # Seção PERFIL -----------------------
                dbc.Button(id='botao_avatar',
                    children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                    ], style={'background-color':'transparent', 'border-color':'transparent'}),

    # Seção NOVO --------------------------
                dbc.Row([
                    dbc.Col([
                        dbc.Button(color='success', id='open-novo-receita',
                                children=['+ Receita'])
                    ], width=6),
                    dbc.Col([
                        dbc.Button(color='danger', id='open-novo-despesa',
                                children=['- Despesa'])
                    ], width=6)
                ])
            ])





# =========  Callbacks  =========== #
# Pop-up receita
