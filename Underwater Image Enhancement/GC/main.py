
import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure

from sceneRadianceGC import RecoverGC

np.seterr(over='ignore')
if __name__ == '__main__':
    pass
# folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/NonPhysical/GC"
# folder = "C:/Users/Administrator/Desktop/Databases/Dataset"
folder = "F:/mydata"

path = folder + "/InputImages"
files = os.listdir(path)
files =  natsort.natsorted(files)

output_folder = folder + "/OutputImages/gc"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        # img = cv2.imread('InputImages/' + file)
        img = cv2.imread(folder + '/InputImages/' + file)
        sceneRadiance = RecoverGC(img)
        print('sceneRadiance',sceneRadiance)
        cv2.imwrite(output_folder + '/' + prefix + '_GC.jpg', sceneRadiance)
