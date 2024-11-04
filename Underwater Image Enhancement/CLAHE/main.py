import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure

from sceneRadianceCLAHE import RecoverCLAHE
from sceneRadianceHE import RecoverHE

np.seterr(over='ignore')
if __name__ == '__main__':
    pass
# folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/HE" age theke cmnted
#folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/NonPhysical/ClAHE" ami cmnt korechi
folder ="F:/mydata"
# folder = "C:/Users/Administrator/Desktop/Databases/Dataset" age theke cmnted


path = folder + "/InputImages"
files = os.listdir(path)
files =  natsort.natsorted(files)

output_folder = folder + "/OutputImages/Clahe"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        #img = cv2.imread('InputImages/' + file)
        img = cv2.imread(folder + '/InputImages/' + file)
        sceneRadiance = RecoverCLAHE(img)
        cv2.imwrite(output_folder + '/' + prefix + '_CLAHE.jpg', sceneRadiance)
        # print('OutputImages/' + prefix + '_CLAHE.jpg')
        #cv2.imwrite('Temps/' + prefix + '_CLAHE.jpg', sceneRadiance)
print("done")