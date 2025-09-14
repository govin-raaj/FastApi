from fastapi import FastAPI,HTTPException,Path,Query
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



@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data