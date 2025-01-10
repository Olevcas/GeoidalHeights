import numpy as np
import pandas as pd
import sys
sys.path.append('./Part_1_1/')
from MainCodes import main
from Constants import constants

#Instantiates the dataframes made to contain the data from EGM2008 and GGM03S
df_plot_data_EGM2008 = pd.DataFrame(columns=['Latitude', 'Longitude', 'Geoidal_height'])
df_plot_data_GGM03S = pd.DataFrame(columns=['Latitude', 'Longitude', 'Geoidal_height'])

#Step size for how often to calculate the geoidal height 
step_size = 1

#Area of interest
longitudes = np.arange(-30, 30 + step_size, step_size)
latitudes = np.arange(45, 75 + step_size, step_size)

# Create meshgrid of latitudes and longitudes, and then estimate geoidal heights for all points inside this grid with the chosen step size
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
            print("Current lat: ", lat, ", current lon: ", lon)

    df_plot_data_EGM2008.to_csv('Part_1_1/Plots/Data/plot_data_EGM2008.txt', sep='A', index=False)
    df_plot_data_GGM03S.to_csv('Part_1_1/Plots/Data/plot_data_GGM03S.txt', sep='A', index=False)


#Example of how to generate data used for plotting
#make_plot_data(latitudes, longitudes)
    








