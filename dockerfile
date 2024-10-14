# Imagen base de Python
FROM python:3.10.12

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la app
COPY . .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]