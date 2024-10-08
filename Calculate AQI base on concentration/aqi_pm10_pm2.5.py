import pandas as pd

breakpoints = {
    "PM2.5": [
        (0, 25, 0, 50), (25, 50, 50, 100), (50, 80, 100, 150),
        (80, 150, 150, 200), (150, 250, 200, 300), (250, 350, 300, 400), (350, 500, 400, 500)
    ],
    "PM10": [
        (0, 50, 0, 50), (50, 150, 50, 100), (150, 250, 100, 150),
        (250, 350, 150, 200), (350, 420, 200, 300), (420, 500, 300, 400), (500, 600, 400, 500)
    ]
}


# Hàm tính AQI dựa trên công thức số 1
def calculate_aqi(nowcast, breakpoints):
    for BP_low, BP_high, I_low, I_high in breakpoints:
        if BP_low <= nowcast <= BP_high:
            # Công thức số 1
            aqi = ((I_high - I_low) / (BP_high - BP_low)) * (nowcast - BP_low) + I_low
            return aqi
    return None  # Nếu không tìm được khoảng phù hợp


# Đường dẫn file CSV
file_path = 'air_quality_data.csv'

data = pd.read_csv(file_path)

required_columns = ['nowcast_pm2.5', 'nowcast_pm10']
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    print(f"Thiếu các cột sau trong file CSV: {', '.join(missing_columns)}")
    exit()

# Tạo cột AQI cho từng chất
data['aqi_pm2.5'] = data['nowcast_pm2.5'].apply(lambda x: calculate_aqi(x, breakpoints['PM2.5']))
data['aqi_pm10'] = data['nowcast_pm10'].apply(lambda x: calculate_aqi(x, breakpoints['PM10']))

# Lưu lại kết quả về file cũ
data.to_csv(file_path, index=False)
print(f"Kết quả đã được lưu vào: {file_path}")
