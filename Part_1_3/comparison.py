import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/')
from Part_1_2 import geometric_geoid_heights

colspecs = [(0,12),(12,24),(25,41)]
column_names = ['Latitude', 'Longitude', 'Geoidal_height']

df2 = geometric_geoid_heights.df2
df4 = pd.read_fwf('Part_1_3/gravimetric_heights_229_rows.txt', colspecs=colspecs, encoding='latin1', sep='\t',names=column_names, skiprows=1)

df_residual = pd.DataFrame()
df_residual["residual"] = df2["Geoid height"] - df4["Geoidal_height"]

n = 5  # Adjust as needed
df_downsampled = df_residual.iloc[::n]

# Plot the downsampled data
fig, ax = plt.subplots(figsize=(12,7))
ax.plot(df_downsampled.index, df_downsampled["residual"], '-', color='purple')
ax.set(xlabel='Station', ylabel='Residual', title='Residual [m]')
plt.show()
