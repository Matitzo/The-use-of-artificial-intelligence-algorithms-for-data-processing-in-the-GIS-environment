import arcpy # library from ArcGIS Pro software
from arcpy.ia import * # module that allows management and processing of images and raster data


# Defining the processor used
arcpy.env.processorType = "GPU" # specify the type of CPU or GPU
arcpy.env.gpuId = "0" # specifying the ID of the processor being used


# Defining parameters
in_raster = "D:/Mateusz/Ortofotomapy_wielkopolska/ Clip_Grochowy_5cm_10cm.tif" # variable storing the path to the image undergoing detection
out_detected_objects = "D:/Mateusz/Modele_Testowe/Detection_Output/ Clip_Grochowy_5cm_10cm.shp" # variable storing the path to save the detection results and indicating the file format
in_model_definition = "D:/Mateusz/TrainedModels/Deep_Learning_Model_Groby/ Deep_Learning_Model_Groby.emd" # variable storing the path to the deep learning model used for detection
model_arguments = "padding 24; threshold 0.1; batch_size 4" # variable storing detection parameters
run_nms = "NMS" # variable specifying whether duplicates are to be removed. Takes the values "NMS" or "NO_NMS"
confidence_score_field = "Confidence" # variable defining the name of the field in the attributes of the resulting objects, containing the confidence level of detection of a given object
class_value_field = "Class" # variable specifying the name of the field that contains the object classes
max_overlap_ratio = 0 # variable specifying the maximum value of the overlap ratio of the detected objects
processing_mode = "PROCESS_ITEMS_SEPARATELY" # variable defining the parameter that determines the mode of processing raster images in a mosaic dataset (if used). There are 2 modes: separate processing of individual rasters from the set or combining them into a mosaic and processing them sequentially. This parameter does not apply to our object (a single raster), but the program requires that some value be assigned to it. It takes the values "PROCESS_ITEMS_SEPARATELY" or "PROCESS_AS_MOSAICKED_IMAGE".


# Detection - below command accepting variables as parameters to perform object detection on the indicated image
DetectObjectsUsingDeepLearning( in_raster, out_detected_objects,
in_model_definition, model_arguments, run_nms, confidence_score_field,
class_value_field, max_overlap_ratio, processing_mode)