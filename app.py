# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 02:19:30 2020

@author: Amol
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='Templates')
model = pickle.load(open('knn_classifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    if prediction==[0]:
        return render_template('index.html', prediction_text='The Predicted Value is {}'.format(prediction),pred= 'Banknote is real.')
    else:
        return render_template('index.html', prediction_text='The Predicted Value is {}'.format(prediction),pred='Banknote is fake.')




    

if __name__ == "__main__":
    app.run(debug=True)
