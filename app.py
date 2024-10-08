from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('rf.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = [float(x) for x in request.form.values()]
        input_data = np.array(input_data).reshape(1, -1)

        prediction = model.predict(input_data)

        return render_template('index.html', prediction_text = f"Kết quả dự đoán: {prediction[0]}")

if __name__ == "__main__":
    app.run(debug=True)