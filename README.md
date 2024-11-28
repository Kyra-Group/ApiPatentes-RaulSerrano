Este proyecto es una API desarrollada con FastAPI para gestionar patentes. La API proporciona funcionalidades para consultar, agregar y actualizar patentes, utilizando una base de datos MongoDB como almacenamiento. La aplicación añade registros a la base de datos desde un archivo Excel el cual contiene registros de patentes.

Tecnologías utilizadas:
FastAPI: Framework para la creación de APIs.
Uvicorn: Servidor para ejecutar la aplicación FastAPI.
MongoDB: Base de datos SQL para almacenar la información de las patentes.
Pandas: Para manipulación y análisis de datos, especialmente al leer el archivo Excel.
Motor: Driver de MongoDB para Python.
GitHub Actions: Para CI/CD.

Requisitos para ejecutar este proyecto en un entorno local:
Python 3.10 o superior
MongoDB (puede ser local o en la nube)
Dependencias del proyecto (en el archivo requirements.txt)

Instalación y configuración:
1. Clonar el repositorio a una máquina local:
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
2. Instalar las dependencias:
pip install -r requirements.txt
3. Configurar MongoDB:
La aplicación requiere un URI de conexión a MongoDB. Puedes crear un secreto en GitHub llamado MONGO_URI que contenga el URI de conexión.
En el caso de usar MongoDb Atlas: mongodb+srv://usuario:contraseña@cluster.mongodb.net/base_de_datos?retryWrites=true&w=majority
En el caso de usar MongoDB local: mongodb://localhost:27017
4. Coloca el archivo Excel Caducidades_Patentes_Europeas_2024.xlsx en la carpeta adecuada de tu proyecto y actualiza la ruta en el flujo de trabajo de GitHub Actions si es necesario.

Uso de la API:
Una vez que hayas configurado todo lo anterior, puedes iniciar la API con el siguiente comando:
uvicorn patentes:app --host 127.0.0.1 --port 8000 --log-level warning
La API estará disponible en http://127.0.0.1:8000. Puedes consultar la documentación interactiva de la API accediendo a:
http://127.0.0.1:8000/docs

Inicialización de la base de datos:
Para inicializar la base de datos, debes asegurarte de que MongoDB esté funcionando y accesible mediante el URI proporcionado. Si es necesario, puedes ejecutar un script que conecte y cree las colecciones si no existen:

from motor.motor_asyncio import AsyncIOMotorClient
async def init_db():
    client = AsyncIOMotorClient("MONGO_URI")  # Habría que reemplazar MONGO_URI con tu URI de MongoDB
    db = client['patentes']
    # Crear las colecciones necesarias si no existen
    await db.create_collection('patentes', check_exists=False)
    print("Base de datos inicializada")

Pasos de despliegue utilizando GitHub Actions:
Este proyecto tiene configurado GitHub Actions para automatizar la integración continua. Cada vez que se haga un push a la rama main o se envíe un pull request, GitHub Actions ejecutará el flujo de trabajo que está definido en .github/workflows/ci-cd.yml. Este flujo se asegura de que el código esté funcionando correctamente antes de ser desplegado.

Flujo de trabajo en GitHub Actions:
1. Instalación de dependencias: El flujo comienza instalando todas las dependencias necesarias desde requirements.txt.
2. Ejecución de pruebas: 
3. Prueba de la API: Se realiza una prueba básica para verificar que la API está respondiendo correctamente.
4. Despliegue:

Configuración del archivo de flujo en GitHub Actions:
El flujo de trabajo está configurado en el archivo .github/workflows/ci-cd.yml. Este flujo se ejecutará cada vez que se haga un push de código a la rama main o se cree un pull request a esa rama. El archivo ci-cd.yml configura la instalación de dependencias, la puesta en marcha de la API y la verificación de que todo esté funcionando correctamente.

Estructura de la base de datos:
La base de datos de MongoDB se utiliza para almacenar los datos de las patentes. Su estructura básica es la siguiente:

Base de datos: practicas
Colección: patentes
Campos:
numero: Número de la patente.
titulo: Título de la patente.
fecha_publicacion: Fecha de publicación de la patente.
fecha_vencimiento: Fecha de vencimiento de la patente.
pais: País de registro de la patente.
titular: Nombre del titular de la patente.

Este sería el esquema de la estructura de la base de datos:

practicas (Base de datos)
|
|-- patentes (Colección)
    |
    |-- numero: string
    |-- titulo: string
    |-- fecha_publicacion: datetime
    |-- fecha_vencimiento: datetime
    |-- pais: string
    |-- titular: string
