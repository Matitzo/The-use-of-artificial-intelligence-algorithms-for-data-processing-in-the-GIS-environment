# Import pakietów i modułów
import arcpy
import time

# tworzenie listy z nazwami ortofotomap na podstawie pliku .txt stworzonego w procesie ich pobierania zawierającego opis pobranych danych
images_list = []
sciezka = 'D:\Mateusz\Ortofotomapa_5_10cm_Wielkopolska\pobieracz_ortofoto_20211118232243.txt'
f = open(sciezka, "r")
for line in f:
    name = line.split('.')[0]
    images_list.append(name)
    images_list.pop(0)  # usuwamy pierwsza wartość bo to nazwa kolumny
f.close()

# Poniższy kod wykonuje dwie pętle, które sprawiają, że każda warstwa z poligonem cmentarza jest kolejno parowana z każda ortofotomapą, aż do momentu poprawnego wykonania procesu przycinania. Po jego wykonaniu program przerywa dalsze parowanie i przechodzi do kolejnej warstwy z poligonem po czym powtarza proces parowania. Proces ten wymaga zastosowania komend „try” i „except”, ponieważ jeśli zakres poligonu nie znajduje się w zakresie ortofotomapy pojawia się błąd.
startTime = time.time()  # przypisanie aktualnej godziny do zmiennej
for n in range(1, 101):  # petla stworzona dla 100 warstw cmentarzy
    for i in range(0, len(images_list)):
        try:
            # Okreslenie paramatrów dla narzędzia „Clip Raster”:
            in_raster = "D:/Mateusz/Ortofotomapa_5_10cm_Wielkopolska/" + images_list[
                i] + ".tif"  # zmienna przechowująca ścieżkę zapisu rastra
            rectangle = "#"  # program sam określi zakres prostokąta do którego będzie przycinał raster
            out_raster = "D:/Mateusz/Przyciete_rastry/Clip_" + images_list[i] + ".tif"  # zmienna
            przechowująca
            ścieżkę
            zapisu
            rastra
            in_template_dataset = "D:/Mateusz/BUCM_pojedynczo/" + str(n) + ".shp"  # zmienna
            przechowująca
            warstwę, do
            którego
            wykonane
            zostanie
            przycinanie
            nodata_value = '256'  # Wartość dla pikseli, które mają być traktowane jako NoData.
            clipping_geometry = 'ClippingGeometry'  # Określa, czy dane będą przycinane do minimalnego prostokąta ograniczającego, czy do geometrii klasy obiektów. Parametr ten przyjmuje dwie wartości: NONE – do przycięcia danych wykorzystany zostanie minimalny prostokąt ograniczający (default), ClippingGeometry - do przycięcia danych użyta zostanie geometria określonych obiektów.
            maintain_clipping_extent = 'MAINTAIN_EXTENT'  # Pramater przyjmuje dwie wartości: MAINTAIN_EXTENT – wiersze i kolumny zostaną dopasowane a piksele zostaną spróbkowane by odpowiadały wskazanemu zakresowi przycinania, NO_MAINTAIN_EXTENT – zakres wyjściowy ulegnie dostosowaniu a komórki rastra wprowadzanego do narzędzia zostaną wyrównane

            arcpy.Clip_management(in_raster, rectangle, out_raster, in_template_dataset, nodata_value,
                                  clipping_geometry,
                                  maintain_clipping_extent)  # komenda wywołująca narzędzie Clip Raster
            # zapisywanie nazw ortofotomap do pliku .txt
            sciezka2 = "D:/Mateusz/BUCM_pojedynczo/Lista_cmentarzy.txt"
            z = open(sciezka2, "a")
            z.write(images_list[i] + "\n")
            z.close()
            print("Done ", n)
            break  # zatrzymanie pętli po poprawnym przycięciu ortofotomapy

        except:
            pass
            # wykonanie pomiaru czasu wykonania kodu
            executionTime = (time.time() - startTime)
            print('Execution time in seconds: ' + str(executionTime))