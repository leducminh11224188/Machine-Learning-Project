import pandas as pd

breakpoints = {
    "CO": [
        (0, 10000, 0, 50), (10000, 30000, 50, 100), (30000, 45000, 100, 150),
        (45000, 60000, 150, 200), (60000, 90000, 200, 300), (90000, 120000, 300, 400), (120000, 150000, 400, 500)
    ],
    "SO2": [
        (0, 125, 0, 50), (125, 350, 50, 100), (350, 550, 100, 150),
        (550, 800, 150, 200), (800, 1600, 200, 300), (1600, 2100, 300, 400), (2100, 2630, 400, 500)
    ],
    "NO2": [
        (0, 100, 0, 50), (100, 200, 50, 100), (200, 700, 100, 150),
        (700, 1200, 150, 200), (1200, 2350, 200, 300), (2350, 3100, 300, 400), (3100, 3850, 400, 500)
    ],
    "O3": [
        (0, 160, 0, 50), (160, 200, 50, 100), (200, 300, 100, 150),
        (300, 400, 150, 200), (400, 800, 200, 300), (800, 1000, 300, 400), (1000, 1200, 400, 500)
    ],
}


# Hàm tính AQI dựa trên công thức số 1
def calculate_aqi(concentration, breakpoints):
    for BP_low, BP_high, I_low, I_high in breakpoints:
        if BP_low <= concentration <= BP_high:
            # Công thức số 1
            aqi = ((I_high - I_low) / (BP_high - BP_low)) * (concentration - BP_low) + I_low
            return aqi
    return None


# Đường dẫn file CSV
file_path = 'air_quality_data.csv'


data = pd.read_csv(file_path)

# Kiểm tra xem các cột cần thiết có trong file không
required_columns = ['co', 'so2', 'no2', 'o3']
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    print(f"Thiếu các cột sau trong file CSV: {', '.join(missing_columns)}")
    exit()

# Tạo cột AQI cho từng chất
data['aqi_co'] = data['co'].apply(lambda x: calculate_aqi(x, breakpoints['CO']))
data['aqi_so2'] = data['so2'].apply(lambda x: calculate_aqi(x, breakpoints['SO2']))
data['aqi_no2'] = data['no2'].apply(lambda x: calculate_aqi(x, breakpoints['NO2']))
data['aqi_o3'] = data['o3'].apply(lambda x: calculate_aqi(x, breakpoints['O3']))

# In kết quả ra màn hình
print(data[['co', 'so2', 'no2', 'o3', 'aqi_co', 'aqi_so2', 'aqi_no2', 'aqi_o3']])

# Lưu lại kết quả về file cũ
data.to_csv(file_path, index=False)
print(f"Kết quả đã được lưu vào: {file_path}")
