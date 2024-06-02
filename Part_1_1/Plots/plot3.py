import numpy as np
import pandas as pd
import pygmt

df_plot_data_EGM2008 = pd.read_csv('Part_1_1/Plots/Data/plot_data_EGM2008.txt', encoding='latin1', sep='A')
df_plot_data_GGM03S = pd.read_csv('Part_1_1/Plots/Data/plot_data_GGM03S.txt', encoding='latin1', sep='A')

latitudes = df_plot_data_EGM2008['Latitude'].values
longitudes = df_plot_data_EGM2008['Longitude'].values
heights_EGM2008 = df_plot_data_EGM2008['Geoidal_height'].values
heights_GGM03S = df_plot_data_GGM03S['Geoidal_height'].values


# Determine grid parameters
region = [-40, 40, 30, 80]  # Define region of interest (xmin, xmax, ymin, ymax)
spacing = 0.1  # Grid spacing
min_height = min(np.min(heights_EGM2008),np.min(heights_GGM03S))
max_height = max(np.max(heights_EGM2008),np.max(heights_GGM03S))
color_interval = [min_height - 10, max_height + 10, (max_height - min_height)/20]

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

cmap1 = pygmt.makecpt(
    cmap="jet",  # Choose a base colormap (e.g., "jet")
    series=color_interval,  # Specify the intervals
    continuous=False,  # Interpolate colors continuously between intervals
)

# Plot the interpolated grid as an image on the map
fig.grdimage(grid=grid, cmap=cmap1, frame="ag",projection="S0/90/12c",region=region, transparency=10)
fig.coast(shorelines="0.2p", transparency=30,region=region)
fig.colorbar(position='JMR', frame='+l"Heights EGM2008"')
fig.text(text="Geoidal height model using EGM2008", x=5, y=15, font="12p,Helvetica-Bold", justify="LM")
fig.show()


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
fig2.grdimage(grid=grid2, cmap=cmap2, frame="ag",projection="S0/90/12c",region=region, transparency=10)
fig2.coast(shorelines="0.2p", transparency=30,region=region)
fig2.colorbar(position='JMR', frame='+l"Heights GGM03S"')
fig.text(text="Geoidal height model using GGM03S", x=5, y=15, font="12p,Helvetica-Bold", justify="LM")
fig2.show()

#projection="S0/90/12c"
