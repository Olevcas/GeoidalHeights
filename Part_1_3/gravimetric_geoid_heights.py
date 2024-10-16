import numpy as np
import pandas as pd
import sys
sys.path.append('./')
from Part_1_2 import geometric_geoid_heights
sys.path.append('./Part_1_1/')
from MainCodes import main
from Constants import constants


#Initializing the dataframes that will contain the coordinates of the 2329 stations, and the estimated geoidal height using the two different gravimetric models
df_gravimetric_EGM2008 = pd.DataFrame(columns=['Latitude', 'Longitude', 'Geoidal_height'])
df_gravimetric_GGM03S = pd.DataFrame(columns=['Latitude', 'Longitude', 'Geoidal_height'])


#This function only needs to be called once, as the results of the calculations are written onto two .txt files
#One for EGM2008 and one for GGM03S
def gravimetric_heights():

    global df_gravimetric_EGM2008 # Define df3 as a global variable
    global df_gravimetric_GGM03S  # Define df3 as a global variable

#For each row in the dataframe containing the coordinates of the 2329 stations, 
#the geoidal height is estimated using the program created in Part_1_1 and the two different gravimetric models
    for index, row in geometric_geoid_heights.df_levelling_data.iterrows():
        
        longitude = float(row['Longitude'])
        latitude = float(row['Latitude'])

#After each calculation, the results are added to the dataframes created earlier
        df_gravimetric_EGM2008_temp = pd.DataFrame({'Latitude': [latitude], 'Longitude': [longitude], 'Geoidal_height': [main.geoidalHeight(latitude, longitude, constants.r, constants.df_EGM2008)]})
        df_gravimetric_EGM2008 = pd.concat([df_gravimetric_EGM2008, df_gravimetric_EGM2008_temp], ignore_index=True)

        #df_gravimetric_GGM03S_temp = pd.DataFrame({'Latitude': [latitude], 'Longitude': [longitude], 'Geoidal_height': [main.geoidalHeight(latitude, longitude, constants.r, constants.df_GGM03S)]})
        #df_gravimetric_GGM03S = pd.concat([df_gravimetric_GGM03S, df_gravimetric_GGM03S_temp], ignore_index=True)

        print("This is line nr. ", index)

#And finally the content of the dataframes is written onto two text files
    df_gravimetric_EGM2008.to_csv('Part_1_3/Data/gravimetric_heights_EGM2008.txt', sep='A', index=False)
    #df_gravimetric_GGM03S.to_csv('Part_1_3/Data/gravimetric_heights_GGM03S.txt', sep='A', index=False)


#Two text files are created every time the code is run, and if two files already exist, these will be overwritten and replaced by the new ones 
gravimetric_heights()





