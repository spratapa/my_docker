import pickle
import sys
import numpy as np
from sklearn.linear_model import LogisticRegression

# Load the pickle file 
with open('./model.pkl', 'rb') as model_pkl:
    model = pickle.load(model_pkl)
    
# Import Flask for creating API
from flask import Flask, request
    
# Initialise a Flask object
app = Flask(__name__)

# Create an API endpoint for predicting
@app.route('/predict')
def predict_cancer():
    # Read all necessary request parameters
    s1 = request.args.get('s1')
    s2 = request.args.get('s2')
    s3 = request.args.get('s3')
    s4 = request.args.get('s4')
    s5 = request.args.get('s5')
    s6 = request.args.get('s6')
    s7 = request.args.get('s7')
    s8 = request.args.get('s8')
    s9 = request.args.get('s9')
    s10 = request.args.get('s10')  
    
    s11 = request.args.get('s11')
    s12 = request.args.get('s12')
    s13 = request.args.get('s13')
    s14 = request.args.get('s14')
    s15 = request.args.get('s15')
    s16 = request.args.get('s16')
    s17 = request.args.get('s17')
    s18 = request.args.get('s18')
    s19 = request.args.get('s19')
    s20 = request.args.get('s20')  
    
    s21 = request.args.get('s21')
    s22 = request.args.get('s22')
    s23 = request.args.get('s23')
    s24 = request.args.get('s24')
    s25 = request.args.get('s25')
    s26 = request.args.get('s26')
    s27 = request.args.get('s27')
    s28 = request.args.get('s28')
    s29 = request.args.get('s29')
    s30 = request.args.get('s30') 

    # Use the predict method of the model to 
    # get the prediction for unseen data
    unseen_data = np.array([[s1, s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30]]).astype(np.float64)
    
    result = model.predict(unseen_data)
    
    # return the result back
    return 'Predicted result for observation ' + str(unseen_data) + ' is: ' + str(result)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)

