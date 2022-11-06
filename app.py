from re import X
from model.utils import heart
import pickle
import numpy as np
from flask import Flask,jsonify,request

app=Flask(__name__)
prun_model=pickle.load(open('DT_prun_model.pkl','rb'))

@app.route('/')
def result():
    return jsonify ({"sms":25})

@app.route("/op")
def ans():
    X= [float(x) for x in request.form.values()]
    features = [np.array(X)]
    prediction = prun_model.predict(features)
    return jsonify ({"result":f"the user has heart dieseas  {prediction}"})
if __name__=="__main__":
    app.run()