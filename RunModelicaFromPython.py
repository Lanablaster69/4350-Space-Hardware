
# coding: utf-8

# In[2]:


from OMPython import ModelicaSystem

mod=ModelicaSystem("D:/school 22-23/4350 Space Hardware/P-setion","Sattrak.Sattest", ["Modelica.Constants"])


# In[3]:


R = 40.e3
L = 500.e-6
C = 200.e-12

ParamSet = ["R=%1.3e" % R, "L=%1.3e" % L, "C=%1.3e" % C]
ParamSet


# In[4]:


mod.setParameters(ParamSet)

mod.getParameters()


# In[5]:


mod.setSimulationOptions(["startTime=0.", "stopTime=100.e-6", "stepSize=2.e-7"])

mod.getSimulationOptions()


# In[6]:


mod.simulate()


# In[7]:


mod.getSolutions()


# In[8]:


[time, V] = mod.getSolutions(["time", "V"])
time, V


# In[11]:


from bokeh.plotting import figure, output_notebook, output_file, show
from bokeh.models import HoverTool
output_notebook()

p = figure(x_range=[0., 100e-6], y_range=[0., 50.], 
           width=900, height=700, 
           title="Open Modelica Output - RLCSwitched",
          tools="pan,wheel_zoom,box_zoom,reset,crosshair, save")

p.xaxis.axis_label = 'time (seconds)'
p.yaxis.axis_label = 'Voltage - V (Volts)'
p.background_fill_color = "khaki"

p.xgrid.grid_line_color = 'black'
p.xgrid[0].grid_line_alpha=0.8
p.xgrid.minor_grid_line_color = 'black'
p.xgrid.minor_grid_line_alpha = 0.2

p.ygrid.grid_line_color = 'black'
p.ygrid[0].grid_line_alpha=0.8
p.ygrid.minor_grid_line_color = 'black'
p.ygrid.minor_grid_line_alpha = 0.25

l1 = p.line(x=time, y=V, color='green', line_width=2, legend_label='Elevation')
p.add_tools(HoverTool(renderers=[l1], tooltips=[("(t, V)", "($x, $y)"),]))


show(p)


# In[ ]:




