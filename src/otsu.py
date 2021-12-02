import time as t

from numpy.core.fromnumeric import reshape
from utils import quality as q
from utils import createImage as newImg
from matplotlib import image
import numpy as np
from matplotlib import pyplot

imagePath = 'D:/Projetos/Engenharia de Programas/Image-Segmentation-OTSU/Data/N1.jpg'
img = image.imread(imagePath)
#precisa realizar a leitura dos dados

n = int(img.size/3)
print("Tamanho da imagem", n)
R, G , B = np.reshape(img[:,:,0], n), np.reshape(img[:,:,1],n),np.reshape(img[:,:,2],n)
C = [0]*n
M = 256
K = 3


#inicialização
init_time = t.time()

#Transformação da imagem colorida em preto-e-branco como descrito acima, atribuindo a
#cada pixel da imagem uma cor entre 0 e 255.
for i in range(0,n-1): #g1I1 =(1,0,1 ), grI1=(1,1,1) , exI1=(2,5,0)
    C[i]=int(0.2989*R[i]+0.5870*G[i]+0.1140*B[i])


#Calcular o número de pixels de cada cor de 0 a 255 (histograma p)
# tamnho de P
tmP = M-1  #(1,1,0)
#inicializando com 0 todas as cores
p = [0] * tmP  # #g1I2 =(1,0,1 ), grI2=(1,1,1) , exI2=(2,0,0)

#varrendo os pixels contando o numero de cada cor
for i in range(0, n-1): #g1I3 =(1,0,1 ), grI3=(1,1,1) , exI3=(2,1,0)
    p[C[i]]+=1

#normalizando o histograma
for j in range(0, M-1): #g1I3 =(1,0,1 ), grI3=(1,1,1) , exI3=(3,1,0 )
    p[j]=p[j]/n

stop_time = t.time()
tmpInit= stop_time - init_time

#processo iterativo

iterativo_time = t.time()

Qmax =0 #exT0=(3,1,0 ) : corresponde a essa linha e as duas seguintes 
iter =0 
tm = K-1


fMax = [0]*tm #g1T1 =(1,0,1 ), grT1=(1,1,1) , exT1=(2,0,0 )
f = [0]*tm #g1T2 =(1,0,1 ), grT2=(1,1,1) , exT2=(2,0,0 )


if K==2:# 
    for  f[0] in range(0,M):#g13 =(1,0,1 ), gr3=(1,3,1) , ex3=(2,1,1 )
        iter += 1
        Q= q.quality(f,K,M,p)
        if Q>Qmax:
            Qmax = Q
            for k in range(0,K-1):#g1T4 =(1,0,1 ), grT4=(1,2,1) , exT4=(2,0,0 )
                fMax[k] = f[k]
elif K==3: # 1 comparaçao 
    for  f[0] in range(0,M-1):
        for f[1] in range(f[0]+1, M):
            iter += 1
            Q= q.quality(f,K,M,p)
            if Q>Qmax:
                Qmax = Q
                for k in range(0,K-1):
                    fMax[k] = f[k]

elif K==4: #g1T3 =(0,0,1 )
    for  f[0] in range(0,M-2): 
        for  f[1] in range(f[0]+1,M-1):  
            for  f[2] in range(f[1]+1,M):
                iter += 1
                Q= q.quality(f,K,M,p)
                if Q>Qmax: #g1T5 
                    Qmax = Q
                    for m in range(0,K-1):
                        fMax[m] = f[m]
# elif K==5:
#     for  f[0] in range(0,M-3):
#             for  f[1] in range(f[0]+1,M-2):
#                 for  f[2] in range(f[1]+1,M-1):
#                     for f[3] in range(f[2]+1,M):
#                         iter += 1
#                         Q= q.quality(f,K,M,p)
#                         if Q>Qmax:
#                             Qmax = Q
#                             for m in range(0,K-1):
#                                 fMax[m] = f[m]


end_time = t.time()

time = end_time - iterativo_time

tempoPorIteracao = time/iter
print("#----------------------------------------#")
print("numero de K", K)
print("tempo de inicialização", tmpInit )
print('Iteracao',iter)
print('tempo', time)
print("tempo por iteração ",tempoPorIteracao)
print("#----------------------------------------#")

newImage = newImg.createImage(imagePath, fMax)
pyplot.imshow(newImage)




    
