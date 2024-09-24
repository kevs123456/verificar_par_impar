# Dockerfile
# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo del programa al contenedor
COPY verificar_par_impar.py .

# Establecer el comando predeterminado para ejecutar el programa
CMD ["python", "verificar_par_impar.py"]
