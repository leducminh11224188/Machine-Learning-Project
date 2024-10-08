# Machine-Learning-Project
- Đây là một dự án về học máy sử dụng các mô hình hồi quy trong học máy để dự đoán chỉ số AQI. Chỉ số AQI là một chỉ số quan trọng, được dùng để đánh giá chất lượng không khí.
- Bộ dữ liệu được lấy từ trang web: https://openweathermap.org/. Trang web này cho phép người dùng lấy được các thông tin thời tiết của hiện tại và quá khứ thông qua API, tuy nhiên, trong tập dữ liệu gốc chỉ có nồng độ của các chất, nên tôi đã tính toán giá trị AQI của từng chất theo thang tính của Việt Nam, tham khảo đường dẫn sau: https://cem.gov.vn/storage/news_file_attach/QD%201459%20TCMT%20ngay%2012.11.2019%20AQI.pdf. Các file tính toán được đưa vào folder có tên: 'Calculate AQI base on concentration'
- Dự án học máy này sử dụng các mô hình hồi quy: Linear Regression, Decision Tree Regressor, Random Forest Regressor và XGBRegressor. Sau khi huấn luyện 4 mô hình này, sẽ chọn ra 1 mô hình có hiệu suất cao nhất
- Sau khi chọn ra được mô hình, tôi đã tạo ra một giao diện đơn giản để người dùng có thể nhập được chỉ số AQI của từng chất và hiển thị chỉ số AQI dựa trên dữ liệu đã nhập.

![Screenshot 2024-10-08 220634](https://github.com/user-attachments/assets/8fc53fb6-32b2-4bd5-a7be-ae50df8db63e)
