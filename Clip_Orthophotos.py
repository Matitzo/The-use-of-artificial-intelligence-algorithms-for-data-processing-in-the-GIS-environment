import arcpy # library from ArcGIS Pro software
import time


# creation of a list with the names of orthophotos based on the .txt file created in the process of their download containing a description of the downloaded data
images_list = []
sciezka = 'D:\Mateusz\Ortofotomapa_5_10cm_Wielkopolska\pobieracz_ortofoto_20211118232243.txt'
f = open(sciezka, "r")
for line in f:
    name = line.split('.')[0]
    images_list.append(name)
    images_list.pop(0)  # usuwamy pierwsza wartość bo to nazwa kolumny
f.close()


# The following code executes two loops that make each cemetery polygon layer
# is sequentially paired with each orthophotomap until the clipping process is done correctly.
# Once it is done, the program stops further pairing and moves to the next layer with polygon after which it
# repeats the pairing process. This process requires the use of "try" and "except" commands, because if the range of the
# of the polygon is not within the range of the orthophotos an error appears.

startTime = time.time()  # assigning the current time to a variable
for n in range(1, 101):  # loop created for 100 layers of cemeteries
    for i in range(0, len(images_list)):
        try:
            # Defining paramaters for the "Clip Raster" tool:
            in_raster = "D:/Mateusz/Ortofotomapa_5_10cm_Wielkopolska/" + images_list[
                i] + ".tif"  # variable storing the raster storage path
            rectangle = "#"  # the program itself will determine the extent of the rectangle to which it will crop the raster
            out_raster = "D:/Mateusz/Przyciete_rastry/Clip_" + images_list[i] + ".tif"  # variable storing the raster storage path
            in_template_dataset = "D:/Mateusz/BUCM_pojedynczo/" + str(n) + ".shp"  # variable storing the layer to which trimming will be performed
            nodata_value = '256'  # Value for pixels to be treated as NoData.
            clipping_geometry = 'ClippingGeometry'   # Determines whether the data will be clipped to the minimum bounding rectangle or to the geometry of the object class. This parameter takes two values: NONE - the minimum bounding rectangle (default) will be used to clipping the data, ClippingGeometry - the geometry of the specified objects will be used to clipping the data.
            maintain_clipping_extent = 'MAINTAIN_EXTENT'  # Parametr takes two values: MAINTAIN_EXTENT - the rows and columns will be adjusted and the pixels will be sampled to match the indicated clipping range, NO_MAINTAIN_EXTENT - the output range will be adjusted and the raster cells fed into the tool will be aligned
            arcpy.Clip_management(in_raster, rectangle, out_raster, in_template_dataset, nodata_value, # command that invokes the Clip Raster tool
                                  clipping_geometry,
                                  maintain_clipping_extent)


            # saving the names of orthophotos to a .txt file
            sciezka2 = "D:/Mateusz/BUCM_pojedynczo/Lista_cmentarzy.txt"
            z = open(sciezka2, "a")
            z.write(images_list[i] + "\n")
            z.close()
            print("Done ", n)
            break  # stopping the loop after the orthophoto has been correctly cropped

        except:
            pass
            # performing code execution time measurement
            executionTime = (time.time() - startTime)
            print('Execution time in seconds: ' + str(executionTime))