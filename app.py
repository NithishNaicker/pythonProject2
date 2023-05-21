from flask import Flask,request,jsonify
import numpy as np
import pickle



model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['GET'])
def predict():
    Symptom_1 = request.form.get('Symptom_1')
    Symptom_2 = request.form.get('Symptom_2')
    Symptom_3 = request.form.get('Symptom_3')




    result = model.predict([[int(Symptom_1),int(Symptom_2),int(Symptom_3)]])

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)