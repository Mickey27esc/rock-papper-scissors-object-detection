# rock-paper-scissors-object-detection

Este proyecto es una aplicación que utiliza un modelo YOLOv8 entrenado mediante Roboflow para detectar la posición de las manos y jugar al clásico juego de Piedra, Papel o Tijeras utilizando la webcam. La aplicación consume el modelo a través de una API Key de Roboflow y detecta la forma de la mano que hace el jugador en tiempo real.

### ¿Cómo funciona?
La aplicación permite que el jugador realice los gestos del juego de Piedra, Papel o Tijeras frente a la webcam, y el modelo YOLOv8 identifica si se trata de "piedra", "papel" o "tijeras". Una vez identificada la forma, la aplicación reacciona en consecuencia. Para usarla, sólo necesitas clonar el repositorio, instalar las dependencias y ejecutar el archivo principal.

## Características
- Utiliza un modelo YOLOv8 entrenado mediante Roboflow.
- Detecta las posiciones de las manos y determina el gesto de Piedra, Papel o Tijeras.
- Despliega una ventana con la detección en tiempo real usando la webcam.
- Requiere Python 3.11 para ejecutarse correctamente.

## Requisitos
- Python 3.11
- Librerías y dependencias especificadas en el archivo `requirements.txt`.

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local (Windows):

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/usuario/rock-paper-scissors-object-detection.git

    Navega al directorio del proyecto:

cd rock-paper-scissors-object-detection

Se recomienda crear un entorno virtual para evitar conflictos con otras librerías. Si no tienes virtualenv instalado, puedes hacerlo con el siguiente comando:

pip install virtualenv

Luego, crea un entorno virtual con:

virtualenv venv

    En sistemas Unix (Linux/macOS):

source venv/bin/activate

En Windows:

    venv\Scripts\activate

Instala las dependencias:

    pip install -r requirements.txt

Uso

Para iniciar la aplicación, sigue estos pasos:

    Una vez que las dependencias estén instaladas, corre el siguiente comando:

    python app.py

    Esto abrirá una ventana donde podrás hacer los gestos de piedra, papel o tijeras frente a tu webcam. La aplicación utilizará el modelo YOLOv8 para reconocer el gesto y mostrarlo en la pantalla.

    Para finalizar la aplicación, simplemente presiona la tecla Q en tu teclado, lo que cerrará la ventana de la aplicación.

Notas adicionales:

    API Key de Roboflow: Asegúrate de tener una API Key de Roboflow válida y configurada correctamente. Esta se utiliza para cargar el modelo YOLOv8 entrenado y hacer las predicciones de los gestos.
