import json
import csv
from datetime import datetime

def json_file_to_csv(json_file, csv_file):
    # Mở và đọc dữ liệu từ file JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Mở file CSV để ghi dữ liệu
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)

        header = ['lon', 'lat', 'aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3', 'datetime']
        csv_writer.writerow(header)
        
        # Lấy dữ liệu từ JSON và ghi vào file CSV
        coord = data['coord']
        for item in data['list']:
            main = item['main']
            components = item['components']
            dt = item['dt']
            
            # Chuyển đổi timestamp thành định dạng ngày giờ
            datetime_str = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
            
            # Ghi một dòng dữ liệu vào CSV
            row = [
                coord['lon'],
                coord['lat'],
                main['aqi'],
                components['co'],
                components['no'],
                components['no2'],
                components['o3'],
                components['so2'],
                components['pm2_5'],
                components['pm10'],
                components['nh3'],
                datetime_str
            ]
            csv_writer.writerow(row)

# Tên file JSON của bạn
json_file = 'air_quality_data.json'

csv_file = 'air_quality_data.csv'

# Chuyển đổi từ JSON sang CSV
json_file_to_csv(json_file, csv_file)

