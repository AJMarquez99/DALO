import os
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.offline as po
import scripts.data_retrieval as dr

def getGraph( sym ):
    x_vals = dr.get_values( sym, "date" )
    y_vals = dr.get_values( sym, "close" )

    fig = px.scatter( x=x_vals, y=y_vals)
    test = po.plot( fig, include_plotlyjs=False, output_type='div')

    return test

