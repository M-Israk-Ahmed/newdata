import os
import numpy as np
import cv2
import natsort

from BL import getAtomsphericLight
from EstimateDepth import DepthMap
from getRefinedTramsmission import Refinedtransmission
from TM import getTransmission
from sceneRadiance import sceneRadianceRGB

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

# folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/Physical/MIP"
folder ="C:/Users/HP Envy/OneDrive/Desktop/My MSc Thesis/Masters Thesis Final/NEW PAPER/enhance code/testimg"
path = folder + "/InputImages"
files = os.listdir(path)
files =  natsort.natsorted(files)


output_folder = folder + "/OutputImages"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        img = cv2.imread(folder +'/InputImages/' + file)

        blockSize = 9

        largestDiff = DepthMap(img, blockSize)
        transmission = getTransmission(largestDiff)
        transmission = Refinedtransmission(transmission,img)
        AtomsphericLight = getAtomsphericLight(transmission, img)
        sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)

        cv2.imwrite(output_folder +'/' + prefix + '_MIP_TM.jpg', np.uint8(transmission * 255))
        cv2.imwrite(output_folder +'/'+ prefix + '_MIP.jpg', sceneRadiance)
