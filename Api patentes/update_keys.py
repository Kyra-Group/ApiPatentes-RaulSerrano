from pymongo import MongoClient

MONGO_URI = "mongodb+srv://raulserranovillar:12345678.@cluster0.g6iai.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client['practicas']
collection = db['patentes']

key_mapping = {
    "Unnamed: 0": "FECHA PUBLICACIÓN CADUCIDAD",
    "Unnamed: 1": "NÚM. SOLICITUD (Enlace a CEO)",
    "Unnamed: 2": "NÚM. PUBLICACIÓN (Enlace a INVENES)",
    "Unnamed: 3": "TÍTULO PATENTE",
    "Unnamed: 4": "Descripción CIP",
    "Unnamed: 5": "CIP"
}

def update_documents():
    for doc in collection.find():
        updated_doc = {}
        for old_key, new_key in key_mapping.items():
            if old_key in doc:
                updated_doc[new_key] = doc.pop(old_key)
        updated_doc.update(doc)
        collection.replace_one({"_id": doc["_id"]}, updated_doc)

update_documents()
print("Actualización completada.")
