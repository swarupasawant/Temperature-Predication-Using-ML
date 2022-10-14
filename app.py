import pickle
from flask import Flask, request, app, jsonify,render_template
from flask import Response
import numpy as np 
import pandas as pd 
import json

app = Flask(__name__)
pickle_model = pickle.load(open('temp_pred_model.pkl','rb'))
@app.route('/')
def main():
    return render_template('main.html')


## FOR POSTMAN 
@app.route('/predict_api',methods=['POST'])
def predict_api():

    data = request.json['data']
    data_values = [float(x) for x in data.values()]
    print(272,data_values)
    new_data = [np.array(data_values)]
    print(799,new_data)
    output = pickle_model.predict(new_data)[0]
    print(279,output)
    # using repr function because int64 is not jsonserializble
    return repr(output)


## FOR HEROKU DEPLOYMENT
@app.route('/predict',methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        print(300,data)
        final_features = [np.array(data)]
        print(data)
        
        output = pickle_model.predict(final_features)[0]
        print(output,"output")

        return render_template('main.html',prediction_text = "For Year : {} and Month : {}  Predicted Temprature is{}".format(int(data[-2]),int(data[-1]),output))
    except Exception as e:
        print('Input error',e)
        return render_template('main.html',prediction_text = 'Oopss!!! Check the input again!')

        

if __name__=="__main__":
    app.run(debug=True)
