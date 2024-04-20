from motion_detector import df
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool,ColumnDataSource
from datetime import datetime as dt

df['Start_String'] = df['Start'].dt.strftime('%Y-%d-%m %H:%M:%S')
df['End_String'] = df['End'].dt.strftime('%Y-%d-%m %H:%M:%S')

cds=ColumnDataSource(df)

p = figure(x_axis_type='datetime',width=500,height=250,title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.yaxis.ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[('Start', '@Start_String'),('End','@End_String')])
p.add_tools(hover)


q = p.quad(left='Start',right='End',top=1,bottom=0 , color='green',source=cds)

output_file('Motion_Graph.html')

show(p)