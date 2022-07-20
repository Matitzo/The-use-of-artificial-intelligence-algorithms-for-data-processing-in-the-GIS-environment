# Import pakietów i modułów
import arcpy
from arcpy.ia import *

#tworzenie listy z nazwami ortofotomap na podstawie pliku .txt stworzonego w Etapie nr 2
images_list = []
sciezka = 'D:\Mateusz\BUCM_pojedynczo\Lista_cmentarzy.txt'
f = open(sciezka, "r")
for line in f:
  name=line.split()[0]
  images_list.append(name)
f.close()

startTime = time.time() #przypisanie aktualnej godziny do zmiennej
# Definiowanie wykorzystywanego procesora
arcpy.env.processorType = "GPU"
arcpy.env.gpuId = "0"
#Poniższa pętla wykonuje kolejno proces detekcji grobów na przyciętych ortofotomapach. Zastosowano komendę „try” z „except” by zapobiegać pojawienia się błędów i uzyskać nazwę, przy którym cmentarzu wystąpił – w czasie tego procesu nie pojawiły się jednak żadne.
for i in range(0,len(images_list)):
try:
  in_raster = "D:/Mateusz/Przyciete_rastry/Clip_"+images_list[i]+".tif" # zmienna przechowująca ścieżkę do obrazu poddawanego detekcji
  out_detected_objects = "D:/Mateusz/Detekcja_na_zbiorze/Detected_"+images_list[i]+"_ID_"+str(i)+".shp" # zmienna przechowująca ścieżkę zapisu wyników detekcji i wskazująca format pliku
  in_model_definition = "D:/Mateusz/TrainedModels/Z_Pythona/5_bezlearning_rate/5_bezlearning_rate.emd" # zmienna przechowująca ścieżkę do wykorzystywanego do detekcji modelu głębokiego nauczania
  model_arguments = "padding 24; threshold 0.1; batch_size 4" # zmienna przechowująca parametry detekcji
  run_nms = "NMS" # zmienna określająca czy duplikaty mają zostać usunięte. Przyjmuje wartości „NMS” lub „NO_NMS”
  confidence_score_field = "Confidence" # zmienna definiująca nazwę pola w atrybutach wynikowych obiektów, zawierającego poziom ufności detekcji danego obiektu
  class_value_field = "Class" # zmienna określająca nazwę pola definiującego klasy obiektów w danych wejściowych
  max_overlap_ratio = 0 # zmienna określająca maksymalną wartość współczynnika nakładania się wykrytych obiektów
  processing_mode = None # zmienna definiująca parametr określający tryb przetwarzania obrazów rastrowych w mozaikowym zbiorze danych (jeśli stosowany). Dostępne są 2 tryby: osobne przetwarzanie poszczególnych rastrów ze zbioru lub połączenie ich w mozaikę i kolejno przetworzenie. Parametr ten nie dotyczy naszego obiektu (pojedynczego rastra) ale program wymaga aby została
  przypisana mu jakaś wartość. Przyjmuje wartości „PROCESS_ITEMS_SEPARATELY” lub „PROCESS_AS_MOSAICKED_IMAGE”
  # Detekcja - poniżej komenda przyjmująca zmienne jako parametry do wykonania detekcji obiektów na wskazanym obrazie
  DetectObjectsUsingDeepLearning( in_raster, out_detected_objects,
  in_model_definition, model_arguments, run_nms, confidence_score_field,
  class_value_field, max_overlap_ratio, processing_mode)
except:
  print("Nie udalo się", images_list[i]) #pokazuje nazwę ortofotmapy, przy której pojawił się błąd

# wykonanie pomiaru czasu wykonania kodu
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))