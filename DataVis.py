#Jhon Patrick Tacio
#Prog Act 1-Data Vis

import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'weather_data.csv')
print(f"Looking for CSV at: {csv_path}")

df = pd.read_csv(csv_path)
df['Day'] = range(1, len(df) + 1)

avg_high = df['High_Temp_C'].mean()

plt.figure(figsize=(10, 6)) 
plt.plot(df['Day'], df['High_Temp_C'], 
         color='red', linestyle='-', marker='o', label='High Temp')
plt.plot(df['Day'], df['Low_Temp_C'], 
         color='blue', linestyle='--', marker='s', label='Low Temp')

plt.axhline(y=avg_high, color='orange', linestyle=':', linewidth=2, 
            label=f'Avg High: {avg_high:.1f}°C')

plt.title('Daily High vs Low Temperature Trends - January (30 Days)')
plt.xlabel('Days of the Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True, alpha=0.3) 

output_path = os.path.join(script_dir, 'temperature_trends.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')

plt.show()
print(f"Plot saved as '{output_path}'. Average High: {avg_high:.1f}°C")
