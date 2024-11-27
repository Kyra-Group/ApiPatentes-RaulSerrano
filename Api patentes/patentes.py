from fastapi import FastAPI
import pandas as pd
from pymongo import MongoClient
from fastapi.responses import JSONResponse

app = FastAPI()

excel_path = "C:/Users/Raul/Downloads/patentes/Caducidades_Patentes_Europeas_2024.xlsx"

MONGO_URI = "mongodb+srv://raulserranovillar:12345678.@cluster0.g6iai.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client['practicas']
collection = db['patentes']

@app.on_event("startup")
async def startup_db():
    try:
        print("Conectando con MongoDB...")
        print("Leyendo el archivo Excel...")
        df = pd.read_excel(excel_path)

        data_dict = df.to_dict(orient="records")

        print("Insertando registros en MongoDB...")
        collection.insert_many(data_dict)

        print("Conexión exitosa con MongoDB.")
        print("Registros cargados desde el archivo Excel.")

    except Exception as e:
        print(f"Error durante la carga del Excel o conexión a MongoDB: {e}")

@app.get("/")
def read_root():
    return {"message": "API funcionando"}

