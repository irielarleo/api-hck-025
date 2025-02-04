from fastapi import FastAPI
import pandas as pd

#mengaktifkan / Create API object
app = FastAPI()

#read data
data= pd.read_csv('data.csv')

#coba root home API (get)
@app.get("/")
def root():
    return {'message':'My first API !'}

#endpoint sapaan
@app.get("/name/{name}") #> http://127.0.0.1:8000/name/iriel
def greet(name):
    return{'messege': f'Hai {name}, how are you ?'}

#endpoint return data
@app.get("/data")
def get_data():
    return data.to_dict(orient='records')

#http://127.0.0.1:8000/data

#get data by id
@app.get("/data/{id}")
def search_data(id:int):
    result = data[data['id']==id]
    return {'result': result.to_dict(orient='records')}

#http://127.0.0.1:8000/data/3
#http://127.0.0.1:8000/data/3 >>>>> buat test

#menambahkan data
#@app.post("/data/{add}")
#def add_data(new_data:string):
#    new_data = new_data.split('_')
#   new_row = {'id':new_data[0],
#              'nama':new_data[1],
#              'age':new_data[2],
#             'job':new_data[3]}
    
#  new_row = pd.DataFrame(new_data)
#data = pd.concat([data, new_row], ignore_index=True)

#return{'message': 'data is update !'}