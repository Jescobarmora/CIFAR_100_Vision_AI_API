from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision import datasets

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir las transformaciones a aplicar a las imágenes
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5071, 0.4867, 0.4408], std=[0.2675, 0.2565, 0.2761])
])

# Cargar el modelo preentrenado
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = torch.load("Models/efficientnet_b0_model.pkl", map_location=torch.device(device))
model.eval()  # Poner el modelo en modo de evaluación

# Cargar los nombres de las clases CIFAR-100
cifar100 = datasets.CIFAR100(root='./data', train=False, download=True)
cifar100_classes = cifar100.classes

# Ruta para verificar que la API esté en funcionamiento
@app.get("/")
def read_root():
    return {"message": "API de clasificación de imágenes con EfficientNet"}

# Ruta para realizar predicciones
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Cargar la imagen enviada
    img = Image.open(file.file)
    
    # Aplicar las transformaciones
    img_tensor = transform(img).unsqueeze(0)  # Añadir dimensión para el batch
    
    # Hacer la predicción con el modelo
    with torch.no_grad():
        output = model(img_tensor)
        _, predicted_class = torch.max(output, 1)
    
    # Obtener el nombre de la clase predicha
    predicted_class_name = cifar100_classes[predicted_class.item()]
    
    return JSONResponse(content={"predicción": predicted_class_name})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)