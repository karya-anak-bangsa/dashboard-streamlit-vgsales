# library ui-dashboard
import streamlit as st

# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

# function for create barplot
def barplot(data, x, y, title):
    
    # create barplot with plotly express
    fig = px.bar(data_frame=data, x=x, y=y, text_auto='.3s')

    # update traces barplot
    fig.update_traces(
        marker_color = px.colors.diverging.RdYlBu,
        textposition='outside'
    )

    # update layout barplot
    fig.update_layout(
        title = title,
        xaxis_title = "",
        yaxis_title = "",
        xaxis=dict(tickangle=0),
        yaxis=dict(tickangle=0),
    )

    return fig

# function for create barplot
def grouped_barplot(data, x, y, title):
    
    # create barplot with plotly express
    fig = px.bar(data_frame=data, x=x, y=y, color="Region", barmode="group")

    # update traces barplot
    rdylbu_colors = px.colors.diverging.RdYlBu
    for i, trace in enumerate(fig.data):
        trace.marker.color = rdylbu_colors[i % len(rdylbu_colors)]

    # update layout barplot
    fig.update_layout(
        title = title,
        xaxis_title = "",
        yaxis_title = "",
        xaxis=dict(tickangle=0),
        yaxis=dict(tickangle=0),
        legend=dict(title="", orientation='h', yanchor='top', y=1.06, xanchor='center', x=0.5),
    )

    return fig