import pandas as pd

# Đọc file CSV
df = pd.read_csv('air_quality_data.csv')

# Chọn 6 cột cần tìm max (thay bằng tên cột thực tế)
cols = ['aqi_co', 'aqi_so2', 'aqi_no2', 'aqi_o3', 'aqi_pm2.5', 'aqi_pm10']

# Tìm giá trị lớn nhất của từng dòng trong các cột này
df['AQI per hour'] = df[cols].max(axis=1)

# Hiển thị kết quả
print(df[['AQI per hour']])

df.to_csv('air_quality_data.csv', index=False)
