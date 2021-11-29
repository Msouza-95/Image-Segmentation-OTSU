import time as t

from numpy.core.fromnumeric import reshape
from PIL import Image
from utils import quality as q
from utils import createImage as newImg
from matplotlib import image
import numpy as np
from matplotlib import pyplot

imagePath = 'D:/Projetos/Engenharia de Programas/Image-Segmentation-OTSU/Data/MulherBrancaN4.jpg'
img = image.imread(imagePath)
#precisa realizar a leitura dos dados

n = int(img.size/3)
R, G , B = np.reshape(img[:,:,0], n), np.reshape(img[:,:,1],n),np.reshape(img[:,:,2],n)
C = [0]*n
M = 256
K = 2

#inicialização
init_time = t.time()

#Transformação da imagem colorida em preto-e-branco como descrito acima, atribuindo a
#cada pixel da imagem uma cor entre 0 e 255.
for i in range(0,n-1):
    C[i]=int(0.2989*R[i]+0.5870*G[i]+0.1140*B[i])


#Calcular o número de pixels de cada cor de 0 a 255 (histograma p)
tmP = M-1 # tamnho de P
p = [0] * tmP  #inicializando com 0 todas as cores

#varrendo os pixels contando o numero de cada cor
for i in range(0, n-1):
    p[C[i]]+=1

#normalizando o histograma
for j in range(0, M-1):
    p[j]=p[j]/n

stop_time = t.time()
tmpInit= round(stop_time - init_time,4)

#processo iterativo

iterativo_time = t.time()
Qmax =0
iter =0

tm = K-1
fMax = [0]*tm
f = [0]*tm

if K==2:
    for  f[0] in range(0,M-1):
        for f[0] in range(f[0]+1, M):
            iter += 1
            Q= q.quality(f,K,M,p)
            if Q>Qmax:
                Qmax = Q
                for k in range(0,K-1):
                    fMax[k] = f[k]

elif K==3:
    for  f[0] in range(0,M-2):
        for  f[0] in range(f[0]+1,M-1):
            for  f[0] in range(f[0]+1,M):
                iter += 1
                Q= q.quality(f,K,M,p)
                if Q>Qmax:
                    Qmax = Q
                    for m in range(0,K-1):
                        fMax[m] = f[m]
elif K==4:
    for  f[0] in range(0,M-3):
            for  f[0] in range(f[0]+1,M-2):
                for  f[0] in range(f[0]+1,M-1):
                    for f[0] in range(f[0]+1,M):
                        iter += 1
                        Q= q.quality(f,K,M,p)
                        if Q>Qmax:
                            Qmax = Q
                            for m in range(0,K-1):
                                fMax[m] = f[m]


end_time = t.time()

time = round(end_time - iterativo_time,4)

tempoPorIteracao = round(time/iter, 4)
print("#----------------------------------------#")

print("tempo de inicialização", tmpInit )
print('Iteracao',iter)
print("tempo por iteração ",tempoPorIteracao)
print("#----------------------------------------#")

newImage = newImg.createImage(imagePath, fMax)
pyplot.imshow(newImage)




    
