import pandas as pd
import pygmt

df_plot_data_EGM2008 = pd.read_csv('Part_1_1/Plots/Data/plot_data_EGM2008.txt', encoding='latin1', sep='A')
df_plot_data_GGM03S = pd.read_csv('Part_1_1/Plots/Data/plot_data_GGM03S.txt', encoding='latin1', sep='A')

# Create grid coordinates
latitudes = df_plot_data_EGM2008['Latitude'].values
longitudes = df_plot_data_EGM2008['Longitude'].values

heights_EGM2008 = df_plot_data_EGM2008['Geoidal_height'].values
heights_GGM03S = df_plot_data_GGM03S['Geoidal_height'].values
height_difference = heights_EGM2008 - heights_GGM03S

region = [-40, 40, 30, 80]  # Define region of interest (xmin, xmax, ymin, ymax)
spacing = 5  # Grid spacing


# Create grid file from coordinates and heights
grid1 = pygmt.xyz2grd(
            x=longitudes,
            y=latitudes,
            z=heights_EGM2008,
            region=region,
            spacing=spacing,
        )

# Plot the grid as squares with colors representing heights using grdimage
fig = pygmt.Figure()
fig.grdimage(grid=grid1, cmap="bathy", frame=True, transparency=10)
fig.coast(shorelines="0.2p", transparency=30,region=region)
fig.colorbar(position="JMR", frame='+l"Heights EGM2008"')
fig.show()


grid2 = pygmt.xyz2grd(
            x=longitudes,
            y=latitudes,
            z=heights_GGM03S,
            region=region,
            spacing=spacing,
        )

# Plot the grid as squares with colors representing heights using grdimage
fig2 = pygmt.Figure()
fig2.grdimage(grid=grid2, cmap="bathy", frame=True, transparency=10)
fig2.coast(shorelines="0.2p", transparency=30,region=region)
fig2.colorbar(position="JMR", frame='+l"Heights GGM03S"')
fig2.show()


grid3 = pygmt.xyz2grd(
            x=longitudes,
            y=latitudes,
            z=height_difference,
            region=region,
            spacing=spacing,
        )       

# Plot the grid as squares with colors representing heights using grdimage
fig3 = pygmt.Figure()
fig3.grdimage(grid=grid3, cmap="bathy", frame=True, transparency=10)
fig3.coast(shorelines="0.2p", transparency=30,region=region)
fig3.colorbar(position="JMR", frame='+l"Height difference"')
fig3.show()