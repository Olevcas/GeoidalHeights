import numpy as np
import pandas as pd
import pygmt

#Just run this file to generate the plots

#Reading the plot data
df_plot_data_EGM2008 = pd.read_csv('Part_1_1/Plots/Data/plot_data_EGM2008.txt', encoding='latin1', sep='A')
df_plot_data_GGM03S = pd.read_csv('Part_1_1/Plots/Data/plot_data_GGM03S.txt', encoding='latin1', sep='A')

latitudes = df_plot_data_EGM2008['Latitude'].values
longitudes = df_plot_data_EGM2008['Longitude'].values
heights_EGM2008 = df_plot_data_EGM2008['Geoidal_height'].values
heights_GGM03S = df_plot_data_GGM03S['Geoidal_height'].values
height_difference = heights_EGM2008 - heights_GGM03S

#Finding the max/min to create the color mapping scale
min_height = min(np.min(heights_EGM2008),np.min(heights_GGM03S))
max_height = max(np.max(heights_EGM2008),np.max(heights_GGM03S))
color_interval = [min_height - 10, max_height + 10, (max_height - min_height)/20]

min_height2 = min(np.min(height_difference),np.min(height_difference))
max_height2 = max(np.max(height_difference),np.max(height_difference))
color_interval2 = [min_height2 - 0.2, max_height2 + 0.2, (max_height2 - min_height2)/20]


# Determine grid parameters
region = [-30, 30, 45, 75]  
spacing = 0.1 


# Interpolate heights onto a grid using pygmt.surface
grid = pygmt.surface(
    x=longitudes,
    y=latitudes,
    z=heights_EGM2008,
    region=region,
    spacing=spacing,
)

# Plot the interpolated grid as an image on the map
fig = pygmt.Figure()
pygmt.config(MAP_TITLE_OFFSET="0.5c")
pygmt.config(FONT_ANNOT_PRIMARY="10p")


cmap1 = pygmt.makecpt(
    cmap="jet",  # Choose a base colormap (e.g., "jet")
    series=color_interval,  # Specify the intervals
    continuous=False,  # Interpolate colors continuously between intervals
)

# Plot the interpolated grid as an image on the map
fig.grdimage(grid=grid, cmap=cmap1, projection="S0/90/12c", frame=["x10g10", "y10g10", "+tGeoidal heights over Northern Europe using EGM2008"])
fig.coast(shorelines="0.2p", transparency=30,region=region)
fig.colorbar(position='JMR', frame='+l"Geoidal height (N)"')
fig.show()


#Doing the same thing for the GGM03S plot
grid2 = pygmt.surface(
    x=longitudes,
    y=latitudes,
    z=heights_GGM03S,
    region=region,
    spacing=spacing,
)

fig2 = pygmt.Figure()

cmap2 = pygmt.makecpt(
    cmap="jet",  # Choose a base colormap (e.g., "jet")
    series=color_interval,  # Specify the intervals
    continuous=False,  # Interpolate colors continuously between intervals
)

# Plot the interpolated grid as an image on the map
fig2.grdimage(grid=grid2, cmap=cmap2, projection="S0/90/12c", frame=["x10g10", "y10g10", "+tGeoidal heights over Northern Europe using GGM03S"])
fig2.coast(shorelines="0.2p", transparency=30,region=region)
fig2.colorbar(position='JMR', frame='+l"Geoidal height (N)"')
fig2.show()

grid3 = pygmt.surface(
    x=longitudes,
    y=latitudes,
    z=height_difference,
    region=region,
    spacing=spacing,
)

fig3 = pygmt.Figure()

cmap3 = pygmt.makecpt(
    cmap="jet",  # Choose a base colormap (e.g., "jet")
    series=color_interval2,  # Specify the intervals
    continuous=False,  # Interpolate colors continuously between intervals
)

# Plot the interpolated grid as an image on the map
fig3.grdimage(grid=grid3, cmap=cmap3, frame="ag",projection="S0/90/12c",region=region, transparency=10)
fig3.coast(shorelines="0.2p", transparency=30,region=region)
fig3.colorbar(position='JMR', frame='+l"Heights GGM03S"')
fig3.text(text="Height difference", x=5, y=15, font="12p,Helvetica-Bold", justify="LM")
fig3.show()
