import numpy as np
import pandas as pd
import pygmt
import sys
sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_1_1/')
from MainCodes import main
from Constants import constants

step_size = 5

longitudes = np.arange(-40, 40 + step_size, step_size)
latitudes = np.arange(30, 80 + step_size, step_size)

# Create meshgrid of latitudes and longitudes
lons, lats = np.meshgrid(longitudes, latitudes)

# Flatten the arrays and create an array of tuples
coordinates = np.column_stack((lats.flatten(), lons.flatten()))


heights = np.array([])
height2 = np.array([])


for coordinate in coordinates:
    # Access latitude and longitude values of each tuple
    latitude = coordinate[0]
    longitude = coordinate[1]
    heights = np.append(heights,main.geoidalHeight(latitude,longitude,constants.r,constants.df_EGM2008))
    heights2 = np.append(heights,main.geoidalHeight(latitude,longitude,constants.r,constants.df_EGM2008))

    
# Determine grid parameters
region = [-40, 40, 30, 80]  # Define region of interest (xmin, xmax, ymin, ymax)
spacing = 0.1  # Grid spacing

# Interpolate heights onto a grid using pygmt.surface
grid = pygmt.surface(
    x=coordinates[:, 1],
    y=coordinates[:, 0],
    z=heights,
    region=region,
    spacing=spacing,
)
grid2 = pygmt.surface(
    x=coordinates[:, 1],
    y=coordinates[:, 0],
    z=heights2,
    region=region,
    spacing=spacing,
)

# Plot the interpolated grid as an image on the map
fig = pygmt.Figure()
fig2 = pygmt.Figure()


cmap1 = pygmt.makecpt(
    cmap="jet",  # Choose a base colormap (e.g., "jet")
    series=[np.min(heights)-5, np.max(heights)+5, (np.max(heights)-np.min(heights))/20],  # Specify the intervals
    continuous=False,  # Interpolate colors continuously between intervals
)

# Plot the interpolated grid as an image on the map
fig.grdimage(grid=grid, cmap=cmap1, frame="ag",projection="Cyl_stere/30/-20/12c",region=region, transparency=10)
fig.coast(shorelines="0.2p", transparency=30,region=region)
fig.colorbar(position='JMR', frame='+l"Heights"')
fig.show()

# Plot the interpolated grid as an image on the map
fig2.grdimage(grid=grid2, cmap=cmap1, frame="ag",projection="Cyl_stere/30/-20/12c",region=region, transparency=10)
fig2.coast(shorelines="0.2p", transparency=30,region=region)
fig2.colorbar(position='JMR', frame='+l"Heights"')
fig2.show()

#projection="S0/90/12c"
