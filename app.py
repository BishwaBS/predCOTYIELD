import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
# from flask_caching import Cache
# config = {
#     "DEBUG": True,          # some Flask specific configs
#     "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
#     "CACHE_DEFAULT_TIMEOUT": 300 }


app = Flask(__name__)
# cache= Cache(app)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    int_features = [int(x) for x in request.form.values()]
    # print(int_features)
    # int_features= [33, 2,5]
    final_features = np.array(int_features)
    final_features=final_features.reshape(1,-1)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text="Predicted Cotton Yield", prediction_val="{} kg/ha".format(output))

def main():
    cache.init_app(app, config=your_cache_config)

    with app.app_context():
        cache.clear()


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)