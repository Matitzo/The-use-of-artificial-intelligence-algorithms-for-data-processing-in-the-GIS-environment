# Import pakietów i modułów
import arcpy # pakiet firmy ESRI zawierający dostęp do narzędzi ArcGIS
from arcpy.ia import * # modułu pozwalający na zarządzanie oraz przetwarzanie obrazów i danych rastrowych

# Definiowanie wykorzystywanego procesora
arcpy.env.processorType = "GPU" # określenie typu procesora CPU lub GPU
arcpy.env.gpuId = "0" # określenie ID wykorzystywanego procesora

#Definiowanie parametrów
in_raster = "D:/Mateusz/Ortofotomapy_wielkopolska/ Clip_Grochowy_5cm_10cm.tif" # zmienna przechowująca ścieżkę do obrazu poddawanego detekcji
out_detected_objects = "D:/Mateusz/Modele_Testowe/Detection_Output/ Clip_Grochowy_5cm_10cm.shp" # zmienna przechowująca ścieżkę zapisu wyników detekcji i wskazująca format pliku
in_model_definition = "D:/Mateusz/TrainedModels/Deep_Learning_Model_Groby/ Deep_Learning_Model_Groby.emd" # zmienna przechowująca ścieżkę do wykorzystywanego do detekcji modelu głębokiego nauczania
model_arguments = "padding 24; threshold 0.1; batch_size 4" # zmienna przechowująca parametry detekcji
run_nms = "NMS" # zmienna określająca czy duplikaty mają zostać usunięte. Przyjmuje wartości „NMS” lub „NO_NMS”
confidence_score_field = "Confidence" # zmienna definiująca nazwę pola w atrybutach wynikowych obiektów, zawierającego poziom ufności detekcji danego obiektu
class_value_field = "Class" # zmienna określająca nazwę pola, w którym zawarto klasy obiektów
max_overlap_ratio = 0 # zmienna określająca maksymalną wartość współczynnika nakładania się wykrytych obiektów
processing_mode = "PROCESS_ITEMS_SEPARATELY" # zmienna definiująca parametr określający tryb przetwarzania obrazów rastrowych w mozaikowym zbiorze danych (jeśli stosowany). Dostępne są 2 tryby: osobne przetwarzanie poszczególnych rastrów ze zbioru lub połączenie ich w mozaikę i kolejno przetworzenie. Parametr ten nie dotyczy naszego obiektu (pojedynczego rastra) ale program wymaga aby została przypisana mu jakaś wartość. Przyjmuje wartości „PROCESS_ITEMS_SEPARATELY” lub „PROCESS_AS_MOSAICKED_IMAGE”

# Detekcja - poniżej komenda przyjmująca zmienne jako parametry do wykonania detekcji obiektów na wskazanym obrazie
DetectObjectsUsingDeepLearning( in_raster, out_detected_objects,
in_model_definition, model_arguments, run_nms, confidence_score_field,
class_value_field, max_overlap_ratio, processing_mode)