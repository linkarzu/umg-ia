# Deteccion Mascarillas

## Requerimientos

- El objetivo de este proyecto es desarrollar un modelo de inteligencia
  artificial que pueda detectar si las personas en una imagen están usando
  mascarillas o tapabocas.
  - Este modelo será entrenado con imágenes de personas con y sin mascarillas.
  - Se evaluará su capacidad para clasificar correctamente nuevas imágenes.
- Descripción del Proyecto
  - Recopilación de Datos:
    - Imágenes con Mascarillas: Recopilar un conjunto de imágenes de personas
      usando mascarillas o tapabocas.
    - Imágenes sin Mascarillas: Recopilar un conjunto de imágenes de personas
      sin mascarillas.
    - Etiquetado: Asegurarse de que cada imagen esté correctamente etiquetada
      como "con mascarilla" o "sin mascarilla".
  - Preparación de los Datos:
    - Limpieza de Datos: Eliminar imágenes duplicadas o de baja calidad.
    - Aumento de Datos: Aplicar técnicas de aumento de datos (data augmentation)
      como rotación, escalado y cambio de brillo para aumentar la diversidad del
      conjunto de datos.
  - Diseño del Modelo:
    - Utilizar una red neuronal convolucional (CNN) debido a su eficacia en
      tareas de clasificación de imágenes.
    - Implementar el modelo utilizando bibliotecas de aprendizaje profundo como
      TensorFlow o PyTorch.
  - Entrenamiento del Modelo:
    - Dividir los datos en conjuntos de entrenamiento y validación.
    - Entrenar el modelo con el conjunto de entrenamiento y ajustar los
      hiperparámetros para mejorar el rendimiento.
    - Evaluar el modelo con el conjunto de validación para asegurarse de que no
      haya sobreajuste.
  - Evaluación del Modelo:
    - Probar el modelo con un conjunto de imágenes no vistas (conjunto de
      prueba) para evaluar su precisión y capacidad de generalización.
    - Utilizar métricas como la precisión, la sensibilidad y la especificidad
      para evaluar el rendimiento del modelo.
  - Implementación y Pruebas:
    - Desarrollar una interfaz simple donde se pueda cargar una imagen y el
      modelo indique si las personas en la imagen están usando mascarillas o no.
    - Realizar pruebas con imágenes de diferentes contextos y condiciones de
      iluminación para asegurar la robustez del modelo.
- Uso de la Tecnología
  - Librerías y Herramientas:
    - TensorFlow/Keras o PyTorch: Para la implementación y entrenamiento del
      modelo de red neuronal.
    - OpenCV: Para la manipulación y preprocesamiento de imágenes.
    - NumPy y Pandas: Para la manipulación de datos.
    - Matplotlib/Seaborn: Para la visualización de resultados y métricas.
  - Hardware:
    - Se recomienda utilizar una GPU para acelerar el proceso de entrenamiento
      del modelo, especialmente si se trabaja con un conjunto de datos grande.
- Resultados Esperados
  - Modelo Entrenado: Un modelo de red neuronal capaz de clasificar imágenes de
    personas con y sin mascarillas con alta precisión.
  - Interfaz de Usuario: Una aplicación simple donde se pueda cargar una imagen
    y obtener una predicción sobre el uso de mascarillas.
  - Evaluación del Modelo: Un informe detallado sobre el rendimiento del modelo,
    incluyendo métricas de evaluación y ejemplos de predicciones.

## Crear cuenta y obtener el API Token

- Visitar [kaggle.com](https://www.kaggle.com) y pulsa **Sign Up**.
  - Puedes registrarte con Google, GitHub o correo electrónico.
- Completa el "Onboarding" (nombre de usuario, país, etc.).
  - No hace falta llenar datos de pago; todo es gratuito.
- Abre tu foto de perfil (arriba a la derecha) → **Account - Settings**.
  - En la sección **API** pulsa **Create New API Token**.
- Se descargará `kaggle.json` (contiene tu `username` y `key`).
  - Copia el archivo al lugar correcto y fija permisos:

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

- Prueba la CLI, voy a crear un ambiente virtual para instalar dependencias ahí

```bash
python3 -m venv venv
source venv/bin/activate

pip install kaggle
kaggle datasets list -s "face mask"
```

- Deberías ver una lista de datasets relacionados.

## Link al proyecto de Colab

- [Proyecto Colab Christian Arzu](https://colab.research.google.com/drive/1zgkUG3s1wVcDQVA_4vDefte-FtQe1vl0?usp=sharing)

## Dataset a utilizar

- Voy a usar este notebook de kaggle como base
- [face-mask-detection-using-cnn-98-accuracy/notebook](https://www.kaggle.com/code/arbazkhan971/face-mask-detection-using-cnn-98-accuracy/notebook)
- Abro el proyecto en collab
- ![Image](./readme-img/250528-195919.avif)
- Guardar una copia del notebook para poder hacer cambios
- ![Image](./readme-img/250528-200024.avif)
- Cambio el runtime para usar una GPU
- ![Image](./readme-img/250528-195933.avif)
- La parte de entrenar el model se tomó un tiempo
- ![Image](./readme-img/250529-055346.avif)

## Probar modelo

- En la fase de prueba voy a subir imagenes con mascarilla para ver si las
  detecta correctamente
- ![Image](./readme-img/250529-071213.avif)
- ![Image](./readme-img/250529-071436.avif)
- ![Image](./readme-img/250529-071518.avif)
- ![Image](./readme-img/250529-071607.avif)
-

## Informe Final - Detección de Mascarillas con CNN

### 📌 Objetivo del Proyecto

Desarrollar un modelo de inteligencia artificial capaz de detectar si las
personas en una imagen están usando mascarilla o no. El modelo debe ser capaz de
clasificar imágenes nuevas con alta precisión.

---

### 📁 Recopilacion y Preparacion de Datos

- Se utilizó un dataset con dos clases: `with_mask` y `without_mask`.
- Las imágenes fueron organizadas en carpetas por clase.
- Se aplicó aumento de datos (`aug_transforms`) para mejorar la robustez del
  modelo.
- Las imágenes fueron redimensionadas a 224x224 píxeles.
- Se dividieron en conjunto de entrenamiento y validación (80/20).

---

### 🧠 Arquitectura del Modelo

- Se empleó una red neuronal convolucional preentrenada: `ResNet50`.
- Se aplicó aprendizaje por transferencia (`transfer learning`).
- El modelo fue entrenado con `fine_tune()` y luego ajustado con `unfreeze()` +
  `fit_one_cycle`.

---

### 📊 Evaluacion del Modelo

- Se alcanzó una precisión (`accuracy`) superior al 99% en validación.
- Se utilizó `ClassificationInterpretation` para generar la matriz de confusión.
- Se visualizaron errores con `plot_top_losses`.

---

### 🖼️ Interfaz de Usuario

- Se implementó una interfaz simple en notebook:
  - Subida de imagen (`files.upload()`)
  - Visualización (`matplotlib`)
  - Predicción (`learn.predict`)
- El modelo muestra la imagen y devuelve si la persona tiene o no mascarilla.

---

### 💾 Guardado del Modelo

- El modelo fue exportado como `export.pkl` para ser reutilizado sin necesidad
  de reentrenar.

---

### ✅ Resultados Esperados

- Modelo entrenado y probado con imágenes nuevas.
- Interfaz funcional para predicción individual.
- Informe con métricas, visualizaciones y explicación del proceso completo.
