import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('./')
from Part_1_2 import geometric_geoid_heights


df_levelling_data = geometric_geoid_heights.df_levelling_data
df_computed_gravimetric_data_EGM2008 = pd.read_csv('Part_1_3/Data/gravimetric_heights_EGM2008.txt', encoding='latin1', sep='A')
#df_computed_gravimetric_data_GGM03S = pd.read_csv('Part_1_3/Data/gravimetric_heights_GGM03S.txt', encoding='latin1', sep='A')


df_residual = pd.DataFrame()
df_residual["residual"] = df_levelling_data["Geoid height"] - df_computed_gravimetric_data_EGM2008["Geoidal_height"]

'''
df_residual2 = pd.DataFrame()
df_residual2["residual"] = df_levelling_data["Geoid height"] - df_computed_gravimetric_data_GGM03S["Geoidal_height"]
'''

n = 1  # Adjust as needed
df_downsampled = df_residual.iloc[::n]
#df_downsampled2 = df_residual2.iloc[::n]

# Create subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plot residuals
ax.plot(df_downsampled.index, df_downsampled, '-', color='red', label='EGM2008')
#ax.plot(df_downsampled2.index, df_downsampled2, '-', color='green', label='GGM03S')

# Set labels and title
ax.set(xlabel='Station', ylabel='Residual [m]', title='Residuals Comparison')
ax.legend()

# Show plot
plt.show()

