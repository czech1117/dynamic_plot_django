from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.embed import components
import pandas as pd

def bokeh_plot(data_list):
    # Set column data source
    data_df = pd.DataFrame(data_list)
    source = ColumnDataSource(data=dict(
        y=data_df.y,
        x=data_df.x,
        id=data_df.id
    ))
    # create hovertool html box
    hover = HoverTool(tooltips="""
                <div style="width:100px; height:100px;">
                    <ul>
                        <li>ID: @id</li>   
                        <li>X: @x</li> 
                        <li>Y: @y</li>             
                    </ul>
                </div>
                """
                      )
    # Plot scatter
    p = figure(plot_width=400, plot_height=400, tools=[hover])
    p.yaxis.axis_label = 'y'
    p.xaxis.axis_label = 'x'
    p.circle('x', 'y', size=20, source=source)

    # Store and return components
    script, div = components(p)

    return script, div

