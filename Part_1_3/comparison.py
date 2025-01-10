import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('./')
from Part_1_2 import geometric_geoid_heights


df_levelling_data = geometric_geoid_heights.df_levelling_data
df_computed_gravimetric_data_EGM2008 = pd.read_csv('Part_1_3/Data/gravimetric_heights_EGM2008.txt', encoding='latin1', sep='A')
df_computed_gravimetric_data_GGM03S = pd.read_csv('Part_1_3/Data/gravimetric_heights_GGM03S.txt', encoding='latin1', sep='A')


df_residual = pd.DataFrame()
df_residual["residual"] = df_levelling_data["Geoid height"] - df_computed_gravimetric_data_EGM2008["Geoidal_height"]


df_residual2 = pd.DataFrame()
df_residual2["residual"] = df_levelling_data["Geoid height"] - df_computed_gravimetric_data_GGM03S["Geoidal_height"]


n = 5 # Adjust as needed
df_downsampled = df_residual.iloc[::n]
df_downsampled2 = df_residual2.iloc[::n]


# Calculate standard deviation and mean difference for EGM2008
std_egm2008 = df_residual["residual"].std()
mean_diff_egm2008 = df_residual["residual"].abs().mean()

# Calculate standard deviation and mean difference for GGM03S
std_ggm03s = df_residual2["residual"].std()
mean_diff_ggm03s = df_residual2["residual"].abs().mean()

min_residual_egm2008 = df_residual["residual"].abs().min()
max_residual_egm2008 = df_residual["residual"].abs().max()

# Find minimal and maximal residuals for GGM03S
min_residual_ggm03s = df_residual2["residual"].abs().min()
max_residual_ggm03s = df_residual2["residual"].abs().max()

# Print the results
print(f"EGM2008: Standard Deviation = {std_egm2008:.4f}, Mean Difference = {mean_diff_egm2008:.4f}")
print(f"EGM2008: Min Residual = {min_residual_egm2008:.4f}, Max Residual = {max_residual_egm2008:.4f}")

print(f"GGM03S: Standard Deviation = {std_ggm03s:.4f}, Mean Difference = {mean_diff_ggm03s:.4f}")
print(f"GGM03S: Min Residual = {min_residual_ggm03s:.4f}, Max Residual = {max_residual_ggm03s:.4f}")

# Create subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Plot residuals
ax.plot(df_downsampled.index, df_downsampled, '-', color='red', label='EGM2008')
ax.plot(df_downsampled2.index, df_downsampled2, '-', color='green', label='GGM03S')

# Set labels and title with increased size
ax.set_xlabel('Station', fontsize=14)  # Adjust font size for x-axis label
ax.set_ylabel('Residual [m]', fontsize=14)  # Adjust font size for y-axis label
ax.set_title('Residuals Comparison', fontsize=25)  # Adjust font size for title

# Adjust legend size
ax.legend(fontsize=20)  # Increase legend font size

# Set labels and title
ax.legend()

# Show plot
plt.show()

