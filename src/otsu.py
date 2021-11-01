
from utils import quality as q 
#precisa realizar a leitura dos dados

R= []
G = []
B = []
C =[]

A = 10
L = 20
M = 256
K = 4
###
n = A*L

#inicialização 
#pesquisar o init_time em py

#init_time()
#Transformação da imagem colorida em preto-e-branco como descrito acima, atribuindo a
#cada pixel da imagem uma cor entre 0 e 255.
for i in range(0, n- 1):
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
#tmpInit= get_time();


#processo iterativo

#init_time()

Qmax =0
iter =0

tmfMax =  K-1 # tamnho de fMax
fMax = [0]*tmfMax

if K==2:
    f=[]
    f[0]=0
    for  i in range(0,M-K):
        iter += 1
        Q= q.quality(f,K,M,p)
        
        if Q>Qmax:
            Qmax = Q
            for j in range(0,K-1):
                fMax[j] = f[j]
                
elif K==3:
    f=[]
    f[1]= f[0]+1
    for  i in range(0,M-(K-1)):
        iter += 1
        Q= q.quality(f,K,M,p)
        
        if Q>Qmax:
            Qmax = Q
            for j in range(0,K-1):
                fMax[j] = f[j]
elif K==4:
       print("continue")
    

time = 0 #get_time(); 

tempoPorIteracao = time/iter
print(tempoPorIteracao)





