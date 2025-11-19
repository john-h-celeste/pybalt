import seaborn as sb
import numpy as np
import pandas as pd

df = sb.load_dataset("taxis")

print(df)

print(f'Number of rows: {len(df)}')
print(f'Number of columns: {len(df.columns)}')
print(f'Average fare: ${df.fare.mean():.4}')
print()


df['pickup'] = pd.to_datetime(df['pickup'])
expensive_ride_count = 0
night_ride_count = 0
for _, row in df.iterrows():
    if row['fare'] > 50:
        expensive_ride_count += 1
    hour = row['pickup'].hour
    if hour >= 20 or hour < 6:
        night_ride_count += 1

print("Rides > $50:", expensive_ride_count)
print("Night Rides:", night_ride_count)
print()

print(f'Number of rides with a fare greater than $50: {len(df[df.fare > 50])}')
print(f'Number of rides at night: {len(df[df['pickup'].map(lambda pickup: pickup.hour >= 20 or pickup.hour < 6)])}')
print()

print(f'Number of rides at night: {sum(1 for pickup in df['pickup'] if pickup.hour >= 20 or pickup.hour < 6)}')
print()

print(f'Number of rides with 3 or more passengers: {len(df[df['passengers'] >= 3])}')
print(f'Ride with highest fare was picked up at {df.iloc[np.argmax(df.fare)]['pickup']}')
print(f'Average fare for night rides: ${df[df['pickup'].map(lambda pickup: pickup.hour >= 20 or pickup.hour < 6)].fare.mean():.4}')
print()
