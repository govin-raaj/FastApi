from fastapi import FastAPI,HTTPException,Path
import json


app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


@app.get("/")
def home():
    return {'message':"This is the home page for the app"}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get("/patient/{patient_id}")
def patient_details(patient_id:str = Path(...,description='Id of the patient ',example='P001')):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient not found')
