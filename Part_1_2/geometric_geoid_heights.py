import pandas as pd

# Specify the number of rows to skip

colspecs = [(10,27),(30,47),(90,107)]

df_levelling_data = pd.read_fwf('Part_1_2/Data/gps_levelling_data.txt', colspecs=colspecs, encoding='latin1', nrows = 100)

