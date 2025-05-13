# Imagen base
FROM python:3.11-slim

# Crear carpeta en el contenedor
WORKDIR /app

# Copiar archivos
COPY requirements.txt requirements.txt

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos
COPY . .

# Exponer el puerto donde corre Flask
EXPOSE 5000

# Comando para arrancar el server
CMD ["python", "app.py"]
