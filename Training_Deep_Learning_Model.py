# Import modułów i pakietów
import arcpy # pakiet firmy ESRI zawierający dostęp do narzędzi ArcGIS
from arcpy.ia import * # moduł pozwalający na zarządzanie oraz przetwarzanie obrazów i danych rastrowych

# Definiowanie wykorzystywanego procesora
arcpy.env.processorType = "GPU" # określenie typu procesora CPU lub GPU
arcpy.env.gpuId = "0" # określenie ID wykorzystywanego procesora

# Definiowanie parametrow
in_folder =
"D:/Mateusz/ImageChips/MaskRCNN_Orto5_10cm_Mozaika2_wiecej_danych" # zmienna zawierająca
ścieżkę do folderu, który zawiera image chips
out_folder = "D:/Mateusz/TrainedModels/Deep_Learning_Model_Groby" # zmienna zawierająca ścieżkę wskazującą miejsce zapisu modelu
max_epochs = 20 # zmienna przyjmująca liczbę epok (parametr opisany wyżej)
model_type = "MASKRCNN" # zmienna zawierająca typ modelu
batch_size = 4 # zmienna przyjmująca liczbę określającą ilość próbek szkoleniowych przetwarzanych jednocześnie – im większa liczba tym szybciej ukończy się proces trenowania modelu
arg = "chip_size '224'" # zmienna określająca rozmiar obrazów, wykorzystywanych do trenowania modelu
learning_rate = None # zmienna określająca z jaką szybkością istniejące informacje zostaną nadpisane poprzez nowe zdobyte w procesie uczenia się modelu. Jeśli nie jest zdefiniowana zostanie ona określona poprzez krzywą uczenia się w trakcie procesu nauki
backbone_model = "RESNET50" # zmienna określająca typ konwolucyjnej sieci neuronowej, który zostanie wykorzystany do wytrenowania nowego modelu
pretrained_model = None # zmienna przyjmująca ścieżkę do innego wstępnie wytrenowanego modelu
validation_percent = 50 # zmienna określająca procent danych, które zostaną dostarczone modelowi jako poprawnie określone
stop_training = "STOP_TRAINING" # zmienna określająca możliwość na przedwczesne ukończenie procesu trenowania modelu, jeśli model przestanie się poprawiać z kolejnymi epokami. Przyjmuje wartość CONTINUE_TRAINING lub STOP_TRAINING
freeze = "FREEZE_MODEL" # pozwala wybrać czy w wstępnie wytrenowany modelu chcemy by warstwy w backbone model zostały zamrożone przez co ich parametry nie ulegną zmianie. Przyjmuje parametry FREEZE_MODEL lub UNFREEZE_MODEL

# Trenowanie modelu – poniżej komenda przyjmująca zmienne jako parametry do wyszkolenia modelu głębokiego uczenia
TrainDeepLearningModel(in_folder, out_folder, max_epochs, model_type,
batch_size, arg, learning_rate,
backbone_model, pretrained_model, validation_percent, stop_training, freeze)