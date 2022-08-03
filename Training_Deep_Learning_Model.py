import arcpy # library from ArcGIS Pro software
from arcpy.ia import * # module that allows management and processing of images and raster data


# Defining the processor used
arcpy.env.processorType = "GPU" # specify the type of CPU or GPU
arcpy.env.gpuId = "0" # specifying the ID of the processor being used


# Defining parameters
in_folder =
"D:/Mateusz/ImageChips/MaskRCNN_Orto5_10cm_Mozaika2_wiecej_danych" # variable containing the path to the folder that contains image chips
out_folder = "D:/Mateusz/TrainedModels/Deep_Learning_Model_Groby" # variable containing the path indicating where the model is stored
max_epochs = 20 # variable taking the number of epochs (parameter described above)
model_type = "MASKRCNN" # variable containing model type
batch_size = 4 # variable taking a number indicating the number of training samples processed simultaneously - the higher the number the faster the model training process will be completed
arg = "chip_size '224'" # variable specifying the size of the images used to train the model
learning_rate = None # variable that determines at what rate existing information will be overwritten by new information acquired during the model learning process. If it is not defined it will be determined by the learning curve during the learning process
backbone_model = "RESNET50" # variable specifying the type of convolutional neural network that will be used to train the new model
pretrained_model = None # variable taking a path to another pre-trained model
validation_percent = 50 # variable specifying the percentage of data that will be delivered to the model as correctly specified
stop_training = "STOP_TRAINING" # variable specifying the possibility of premature termination of the model training process if the model stops improving with successive epochs. Takes the value CONTINUE_TRAINING or STOP_TRAINING
freeze = "FREEZE_MODEL" # lets you choose whether you want the layers in the pre-trained model to be frozen in the backbone model so that their parameters do not change. Accepts the FREEZE_MODEL or UNFREEZE_MODEL parameters.


# Train model - below command accepting variables as parameters to train a deep learning model
TrainDeepLearningModel(in_folder, out_folder, max_epochs, model_type,
batch_size, arg, learning_rate,
backbone_model, pretrained_model, validation_percent, stop_training, freeze)