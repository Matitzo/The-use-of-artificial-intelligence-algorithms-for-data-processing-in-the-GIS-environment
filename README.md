# The-use-of-artificial-intelligence-algorithms-for-data-processing-in-the-GIS-environment
## The project was developed as part of an engineering thesis which you can see in full in my repository.
 
The main goal was to create a deep learning model for grave detection in cemeteries based on orthophotos. ArcGIS Pro software was used because it has built-in AI models. The Mask-RCNN model was chosen for the study, allowing the result as a mask/location of objects created in the process of detecting them. The design section presents steps taken sequentially to train the model and the results obtained on the test object - the cemetery in the village of Grochowy (wielkopolskie voivodeship). Result was compared with the actual number of graves. Then the trained model has been applied to a set of 100 cemeteries located in the area of Wielkopolska and the correctness of the obtained results has been analyzed. The project turned out to be a success.

## Tools used in this project:
- ArcGIS Pro
- Python
- QGIS

## Preparing the data:
To donwload the orthophotos (aerial or satellite photographs wich defined position) first I donwloaded BUCM layer from the Internet (.shp files with defined postions of cemeteries) for Wielkopolska. Then I used their postions to donwload orthophotos for evey cemetery in Wielkopolska using QGIS. To this project I used ortophoto with resolution from 5 to 10 cm beacuse of big coverage of Poland.
 
## Training data:
To collect training samples of graves from images I used ArcGIS Pro. Their total number was 2353. The samples had to be various: small graves, big graves, in different colors, shaded and not shaded etc. 

## Training deep learning model:
This proces was also made in ArcGIS Pro using Python and ArcGIS library: arcpy (code on page 42). As deep learning model I used Mask-RCNN because it allows to get the localistaion and shape (poligon) of every detected object.

Loss function:

![image](https://user-images.githubusercontent.com/100380604/176911671-a51357f7-3240-448f-bc99-5eec7235e8aa.png)

## Object detection:
In this stage like previously I used ArcGIS Pro and Python (code on page 49). But before I run this process on orthophotos I used again BUCM layer to clip orthophotos to the area of cemeteries (also using python in ArcGIS Pro), this allowed to shorten the time of object detection and reduced the likelihood of wrong detections. 

## Results:
Firstly model was tested on a cementary in a village Grochowy. The precision score (the ratio of correct indications to all indications) was 96.9%. The recall score (the ratio of correct indications to the total number of objects that should be indicated) was 96.2%. 

![image](https://user-images.githubusercontent.com/100380604/176911425-e3a98f3f-84f3-456a-9b7c-2cf442fefba8.png)

After that model was used on 100 cemeteries in Wielkopolska (this process was made in Python). Depending of the cementery precision score and recall score were different. Differ results are caused by for example: different resolutions of orthophotos, insolation intensity and coverage of the cemeteries with trees which cover up graves. Most cemeteries get recall score around 70%, in some cases this score was near to 100%
