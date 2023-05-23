from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle



model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [int(x) for x in request.form.values()]
    input_query = [np.array(int_features)]
    result = model.predict(input_query)

    return render_template('index.html', prediction_text='The disease is:{}'.format(result))

if __name__ == '__main__':
    app.run(debug=True)