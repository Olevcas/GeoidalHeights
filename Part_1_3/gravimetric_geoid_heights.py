import numpy as np
import pandas as pd
import sys
sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/')
from Part_1_2 import geometric_geoid_heights
sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_1_1/')
from MainCodes import main
from Constants import constants


df3 = pd.DataFrame(columns=['Latitude', 'Longitude', 'Geoidal_height'])



def gravimetric_heights():
    
    global df3  # Define df3 as a global variable

    for index, row in geometric_geoid_heights.df2.iterrows():
        
        longitude = round(float(row['Longitude']), 9)
        latitude = round(float(row['Latitude']), 9)

        df3_temp = pd.DataFrame({'Latitude': [latitude], 'Longitude': [longitude], 'Geoidal_height': [main.geoidalHeight(latitude, longitude, constants.r)]})
        df3 = pd.concat([df3, df3_temp], ignore_index=True)
        print(index)
        
    df3.to_csv('Part_1_3/gravimetric_heights_229_rows.txt', sep='\t', index=False, float_format='%.9f')

gravimetric_heights()





