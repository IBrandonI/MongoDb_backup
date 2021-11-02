from pymongo import MongoClient
#Todo crea un docker con una imagen de mongo db
#Todo Crea una base ficticia con varias collections y documents
#Todo crear script para que muestre las colecciones disponibles para una base en especifíco
# y que permita crear un respaldo de cada una de esas colecciones o de la base de datos
#Todo Un script que permita restaurar la base o las colecciones respaldadas por tu script

mongo_client = input("Ingresa el formato URI: ")
client = MongoClient(mongo_client)
database = input ("Ingresa el nombre de la base de datos: ")
txt_ = input ("¿Gustas un archivo txt con los archivos además de el respaldo de la base de datos?S/N: ").upper()
new_database = f"new_{database}"
db = client[database]
ndb = client[new_database]
collections = db.list_collection_names()
documents = []

for c in collections:
    print(f"Documentos de la coleccion {c}:")
    documents.append({c: db[c].find()})
    print(documents)

for x in range(len(collections)):
    collection_to_create = collections[x]
    document = documents[x][collection_to_create]
    col_created = ndb[collection_to_create]
    ndb.col_created.insertMany(document)

if txt_ == "S":
    with open(new_database, mode="w") as file:
        for d in documents:
            file.write(d)
