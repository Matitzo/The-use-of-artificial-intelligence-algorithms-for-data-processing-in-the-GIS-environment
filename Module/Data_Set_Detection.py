import arcpy # library from ArcGIS Pro software
from arcpy.ia import * # module that allows management and processing of images and raster data


# creation of a list with names of orthophotos based on the .txt file created in Stage #2
images_list = []
sciezka = 'D:\Mateusz\BUCM_pojedynczo\Lista_cmentarzy.txt'
f = open(sciezka, "r")
for line in f:
  name=line.split()[0]
  images_list.append(name)
f.close()

startTime = time.time() # assigning the current time to a variable


# Defining the processor used
arcpy.env.processorType = "GPU"
arcpy.env.gpuId = "0"


#The following loop performs the grave detection process sequentially on the cropped orthophotos.
# A "try" command with "except" was used to prevent errors from occurring and to get the name at which cemetery occurred
# however, none occurred during this process.for i in range(0,len(images_list)):
try:
  in_raster = "D:/Mateusz/Przyciete_rastry/Clip_"+images_list[i]+".tif" # variable storing the path to the image undergoing detection
  out_detected_objects = "D:/Mateusz/Detekcja_na_zbiorze/Detected_"+images_list[i]+"_ID_"+str(i)+".shp" # variable storing the path to save the detection results and indicating the file format
  in_model_definition = "D:/Mateusz/TrainedModels/Z_Pythona/5_bezlearning_rate/5_bezlearning_rate.emd" # variable storing the path to the deep learning model used for detection
  model_arguments = "padding 24; threshold 0.1; batch_size 4" # variable storing detection parameters
  run_nms = "NMS" # variable specifying whether duplicates are to be removed. Takes the values "NMS" or "NO_NMS"
  confidence_score_field = "Confidence" # variable defining the name of the field in the attributes of the resulting objects, containing the confidence level of detection of a given object
  class_value_field = "Class" # variable specifying the name of the field that defines the object classes in the input data
  max_overlap_ratio = 0 # variable specifying the maximum value of the overlap ratio of the detected objects
  processing_mode = None # variable defining the parameter that determines the mode of processing raster images in a mosaic dataset (if used). There are 2 modes: separate processing of individual rasters from the set or combining them into a mosaic and processing them sequentially. This parameter does not apply to our object (a single raster) but the program requires that it be assigned to it some value. It takes the values "PROCESS_ITEMS_SEPARATELY" or "PROCESS_AS_MOSAICKED_IMAGE".


  # Detection - below command accepting variables as parameters to perform object detection on the indicated image
  DetectObjectsUsingDeepLearning( in_raster, out_detected_objects,
  in_model_definition, model_arguments, run_nms, confidence_score_field,
  class_value_field, max_overlap_ratio, processing_mode)


except:
  print("Error", images_list[i]) # shows the name of the orthophotmap at which the error appeared


# performing code execution time measurement
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
