import numpy as np
import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('air_quality_data.csv')

# Chuyển đổi cột 'datetime' thành datetime với định dạng dd/mm/yyyy
df['datetime'] = pd.to_datetime(df['datetime'], dayfirst=True, format='mixed')


# Tạo một hàm để tính toán NowCast cho 12 giờ trước đó
def calculate_nowcast(c_values):
    # Tính C_min và C_max
    C_min = np.min(c_values)
    C_max = np.max(c_values)

    # Tính trọng số w*
    w_star = C_min / C_max

    # Xác định w
    if w_star <= 0.5:
        w = 0.5
    else:
        w = w_star

    # Tính NowCast
    if w == 0.5:
        nowcast = sum((0.5**(i + 1) * c_values[11 - i]) for i in range(len(c_values)))
    else:
        nowcast = sum((w**(i) * c_values[i]) for i in range(len(c_values))) / sum(w**(i) for i in range(len(c_values)))

    return nowcast

# Sắp xếp dữ liệu theo ngày giờ để dễ tính toán
df = df.sort_values(by='datetime')

# Tạo một cột mới cho kết quả NowCast PM2.5
df['nowcast_pm10'] = np.nan

# Tính NowCast dựa trên dữ liệu của 12 giờ trước đó cho từng dòng
for i in range(11, len(df)):  # Bắt đầu từ dòng thứ 12 để có đủ 12 giờ trước đó
    pm25_values = df['pm10'].iloc[i-11:i+1].values  # Lấy 12 giá trị PM2.5
    if len(pm25_values) == 12:  # Đảm bảo có đủ 12 giá trị
        nowcast_value = calculate_nowcast(pm25_values)
        df.at[i, 'nowcast_pm10'] = nowcast_value  # Gán giá trị NowCast cho hàng tương ứng

df.to_csv('air_quality_data.csv', index=False)
