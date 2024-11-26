import cv2
from inference import get_model
import supervision as sv


# Cargar el modelo preentrenado YOLOv8n
model = get_model(model_id="rock-paper-scissors-x10ua/2", api_key="YOUR-API-KEY")

# Inicializar la captura de video
video_capture = cv2.VideoCapture(0)

# Reducir la resolución para mejorar el rendimiento
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Configuración de la detección en intervalos
detection_interval = 12  # Realizar detección cada tercer frame
frame_count = 0
last_detections = None  # Variable para almacenar las detecciones del último frame procesado

# Anotadores
bounding_box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

# Función para capturar y procesar un frame de la webcam
def get_frame(video_capture):
    # Capturar el frame de la webcam
    ret, frame = video_capture.read()
    if not ret:
        return None
    global frame_count, last_detections

    # Realizar inferencia solo en frames específicos
    if frame_count % detection_interval == 0:
        # Ejecutar inferencia y actualizar last_detections
        results = model.infer(frame)[0]
        last_detections = sv.Detections.from_inference(results)
        
        
    print(last_detections.confidence)
    # Si tenemos detecciones del último frame procesado, anotar el frame actual
    if last_detections is not None:
        annotated_image = bounding_box_annotator.annotate(scene=frame, detections=last_detections)
        annotated_image = label_annotator.annotate(scene=annotated_image, detections=last_detections)
        return annotated_image
    else:
        return frame  # En caso de que no haya detecciones, devolver el frame sin anotar

# Ciclo principal para mostrar los frames
while True:
    # Obtener el frame procesado
    frame = get_frame(video_capture)
    frame_count += 1

    # Si no se capturó ningún frame, termina el bucle
    if frame is None:
        print("[ERROR]: No se pudo capturar el frame.")
        break

    # Mostrar el frame
    cv2.imshow('Webcam', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.getWindowProperty('Webcam', cv2.WND_PROP_VISIBLE) < 1 or cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Liberar recursos
video_capture.release()
cv2.destroyAllWindows()
