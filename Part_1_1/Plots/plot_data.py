import numpy as np
import pandas as pd
import sys
sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_1_1/')
from MainCodes import main
from Constants import constants

#This python script creates csv files containing the estimated gravimetric geoid height for a grid of latitudes and longitudes.
#By saving the results to csv files, we avoid having to run the main function every time we want to plot the data. 
#This saves a lot of of computational power.

df_plot_data_EGM2008 = pd.DataFrame(columns=['Latitude', 'Longitude', 'Geoidal_height'])
df_plot_data_GGM03S = pd.DataFrame(columns=['Latitude', 'Longitude', 'Geoidal_height'])


step_size = 5

longitudes = np.arange(-40, 40 + step_size, step_size)
latitudes = np.arange(30, 80 + step_size, step_size)

# Create meshgrid of latitudes and longitudes

def make_plot_data(latitudes, longitudes):

    global df_plot_data_EGM2008
    global df_plot_data_GGM03S

    for lat in latitudes:
        for lon in longitudes:
         # Compute height for the current pair
            heights = main.geoidalHeight(lat,lon,constants.r,constants.df_EGM2008)
            heights2 = main.geoidalHeight(lat,lon,constants.r,constants.df_GGM03S)
        
            # Append the data to the DataFrame
            df_EGM2008_temp = pd.DataFrame({'Latitude': [lat], 'Longitude': [lon], 'Geoidal_height': [heights]})
            df_plot_data_EGM2008 = pd.concat([df_plot_data_EGM2008, df_EGM2008_temp], ignore_index=True)

            df_GGM03S_temp = pd.DataFrame({'Latitude': [lat], 'Longitude': [lon], 'Geoidal_height': [heights2]})
            df_plot_data_GGM03S = pd.concat([df_plot_data_GGM03S, df_GGM03S_temp], ignore_index=True)

    df_plot_data_EGM2008.to_csv('Part_1_1/Plots/Data/plot_data_EGM2008.txt', sep='A', index=False)
    df_plot_data_GGM03S.to_csv('Part_1_1/Plots/Data/plot_data_GGM03S.txt', sep='A', index=False)

#make_plot_data(latitudes, longitudes)
    

df8 = pd.read_csv('Part_1_1/Plots/Data/plot_data_GGM03S.txt', encoding='latin1', sep='A')
print(df8)






