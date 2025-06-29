import requests
import pandas as pd

url = 'https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&hourly=temperature_2m,windspeed_10m'
data = requests.get(url).json()

hours = data['hourly']['time']
t = data['hourly']['temperature_2m']
windspeed = data['hourly']['windspeed_10m']

weather = []
for i in range(len(data['hourly']['time'])):
    date_time = data['hourly']['time'][i]
    date = date_time.split('T')[0]
    time = date_time.split('T')[1]
    weather.append({
        'date': date,
        'hour': hours,
        'temperature': data['hourly']['temperature_2m'][i],
        'windspeed': data['hourly']['windspeed_10m'][i]
    })
df = pd.DataFrame(weather)

next_3days = df.iloc[:72]

min_t = next_3days['temperature'].min()
max_t = next_3days['temperature'].max()
avg_t = next_3days['temperature'].mean()

print(f'Miнімальна температура: {min_t}')
print(f'Максимальна температура: {max_t}')
print(f'Середня температура: {avg_t}')

avg_windspeed = df['windspeed'].mean()
windspeed_hours = df[df['windspeed'] > avg_windspeed]

print(f"Кількість годин, коли швидкість вітру перевищує загальну середню швидкість вітру: {len(windspeed_hours)}")

      




