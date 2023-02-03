# # BaseModel is used to for the setup of the inputs of which model accepts


# from fastapi import FastAPI
# from pydantic import BaseModel
# import pickle
# import json

# app = FastAPI()

# # defines the inputs for the model
# # or defines the input formtat we need 
# class model_input(BaseModel):
#     Pregnancies : int
#     Glucose : int
#     BloodPressure : int
#     SkinThickness : int
#     Insulin : int
#     BMI : float
#     DiabetesPedigreeFunction : float
#     Age : int


# # load the saved pickle model
# # rb means reading the files in bytes
# diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# # save as @app.post()

# @app.post('/diabetes_prediction') # the endpoint parameter is pass as a paranmeter in the post

# def diabetes_pred(input_parameters : model_input) :
#     input_data = input_parameters.json()  # recieved data as a json
#     input_dictionary = json.loads(input_data) # then convert it as a dictionary as model needs

#     preg = input_dictionary['Pregnancies']
#     glu = input_dictionary['Glucose']
#     bp = input_dictionary['BloodPressure']
#     skin = input_dictionary['SkinThickness']
#     insulin = input_dictionary['Insulin']
#     bmi = input_dictionary['BMI']
#     dpf = input_dictionary['DiabetesPedigreeFunctio']
#     age = input_dictionary['Age']

#     input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

#     prediction = diabetes_model.predict([input_list])

#     if (prediction[0] == 0) :
#         return " The person is not Diabetic"
#     else :
#         return " The Person is not Diabetic"
    
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

class model_input(BaseModel):
    
    pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int       
        
# loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    