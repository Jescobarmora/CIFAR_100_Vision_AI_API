# Clasificación de Imágenes con EfficientNet en CIFAR-100

Este repositorio contiene la solución para entrenar un modelo de clasificación de imágenes utilizando **EfficientNet** y/o **ResNet50** sobre el dataset **CIFAR-100**. El modelo se entrena en **Google Colab**/**Kaggle** con ayuda de una **GPU**, alcanzando una precisión de al menos **95%**. Posteriormente, el modelo entrenado se guarda en formato `.pkl` y se despliega a través de una API **FastAPI**, contenedorizada con **Docker**, permitiendo realizar predicciones en tiempo real.

## Contenido del Proyecto

1. **Entrenamiento del Modelo en Google Colab/Kaggle**: Entrenamiento del modelo con EfficientNet/ResNet50 en CIFAR-100.
2. **Exportación del Modelo**: El modelo entrenado se guarda como un archivo en formato `.pkl`.
3. **API FastAPI**: Se desarrolla una API con FastAPI para realizar predicciones de imágenes.
4. **Despliegue en Docker**: La aplicación FastAPI se despliega en Docker para ejecutar predicciones en tiempo real sobre imágenes cargadas. 

## Despliegue en Docker Hub

Este proyecto está disponible en **Docker Hub**. Puedes descargar y ejecutar la imagen directamente desde el siguiente enlace:

[Repositorio DockerHub](https://hub.docker.com/repository/docker/jescobarmora/fastapi-image-classifier/general)

### Descargar la imagen

Para descargar la imagen desde **Docker Hub**, ejecuta el siguiente comando:

```bash
docker pull jescobarmora/fastapi-image-classifier:latest
