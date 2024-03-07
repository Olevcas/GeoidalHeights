import numpy as np
import pandas as pd
import pygmt
import sys
sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_1_1/')
from MainCodes import main
from Constants import constants

step_size = 2

longitudes = np.arange(-40, 40 + step_size, step_size)
latitudes = np.arange(30, 80 + step_size, step_size)
region = [-40, 40, 30, 80]  # Define region of interest (xmin, xmax, ymin, ymax)
spacing = 3  # Grid spacing


# Create meshgrid of latitudes and longitudes
lons, lats = np.meshgrid(longitudes, latitudes)

# Flatten the arrays and create an array of tuples
coordinates = np.column_stack((lats.flatten(), lons.flatten()))


heights = np.array([])

for coordinate in coordinates:
    # Access latitude and longitude values of each tuple
    latitude = coordinate[0]
    longitude = coordinate[1]
    heights = np.append(heights,main.geoidalHeight(latitude,longitude,constants.r))
    


# Create grid coordinates
x = np.arange(region[0], region[1] + spacing, spacing)
y = np.arange(region[2], region[3] + spacing, spacing)


# Create grid file from coordinates and heights
grid_file = "grid.nc"
pygmt.xyz2grd(
    x=coordinates[:, 1],
    y=coordinates[:, 0],
    z=heights,
    G=grid_file,
    R=region,
    I=spacing,
)

cmap1 = pygmt.makecpt(
    cmap="jet",  # Choose a base colormap (e.g., "jet")
    series=[np.min(heights)-5, np.max(heights)+5, (np.max(heights)-np.min(heights))/25],  # Specify the intervals
    continuous=False,  # Interpolate colors continuously between intervals
)

# Plot the grid as squares with colors representing heights using grdimage
fig = pygmt.Figure()
fig.grdimage(grid=grid_file, cmap="jet", frame=True, transparency=10)
fig.coast(shorelines="0.2p", transparency=30,region=region)
fig.colorbar(position="JMR", frame='+l"Heights"')
fig.show()
