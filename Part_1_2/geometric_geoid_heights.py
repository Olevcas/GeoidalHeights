import pandas as pd

#Readint the levelling data and storing it inside a pandas dataframe

colspecs = [(10,27),(30,47),(90,107)]
df_levelling_data = pd.read_fwf('Part_1_2/Data/gps_levelling_data.txt', colspecs=colspecs, encoding='latin1', nrows=1001)

