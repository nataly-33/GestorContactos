# Imagen base
FROM node:20

# Crear carpeta en el contenedor
WORKDIR /app

# Copiar archivos de package
COPY package*.json ./

# Instalar dependencias
RUN npm install 

# Copiar el resto de archivos del proyecto
COPY . .

# Exponer el puerto donde corre Vite
EXPOSE 5173

# Comando para arrancar Vite
CMD ["npm", "run", "dev", "--", "--host"]
