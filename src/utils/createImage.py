from PIL import Image 
import numpy as np

def createImage(path, fMax):
    image2 = Image.open(path)


    imgray= image2.convert(mode = 'L')

    data = np.asarray(imgray)

    newImage = np.array(data)

    for i in range(0,len(newImage)):
        for j in range(0,len(newImage[i])):
            if(newImage[i][j]>fMax[0]):
                newImage[i][j]=255
            else:
                newImage[i][j]=0



    return newImage 