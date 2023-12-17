from flask import Flask, request, jsonify
import pandas as pd
from pycaret.regression import load_model, predict_model
from datetime import datetime

# Cargar los modelos con nombres descriptivos
RandomForest = load_model('model_B1')
ExtraTreesRegressor = load_model('model_v2')
RidgeRegression = load_model('model_v3')

app = Flask(__name__)

def log_prediction(model_name, valor_predicho, current_date):
    with open('model_logs.log', 'a') as archivo_modificado:
        strLog = f'{model_name},{valor_predicho},{current_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
        archivo_modificado.write(strLog)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    data_to_predict = pd.json_normalize(data)
    current_date = datetime.now()

    models = {'RandomForest': RandomForest, 'ExtraTreesRegressor': ExtraTreesRegressor, 'RidgeRegression': RidgeRegression}
    predictions = {}

    for model_name, model in models.items():
        try:
            prediccion = predict_model(model, data=data_to_predict)
            valor_predicho = round(prediccion['prediction_label'][0], 4)  # Usar 'prediction_label'
            predictions[model_name] = valor_predicho
            log_prediction(model_name, valor_predicho, current_date)

        except Exception as e:
            error_msg = f'Error: {str(e)}'
            predictions[model_name] = error_msg
            log_prediction(model_name, error_msg, current_date)

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
