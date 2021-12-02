def quality(f,K,M ,p ):
    #cor inicial dos clusters
    m = [0]*K   #g1Q1 =(1,0,1 ), grQ1=(1,1,1), exQ1=(2,0,0 )
    
    #probabilidades dos clusters
    P = [0]*K  #g1Q2 =(1,0,1 ), grQ2=(1,1,1), exQ2=(2,0,0 )

  
    #primeiro cluster
    a = f[0]+1 #exQ0=(4,2,0 )
    
    
    for c in range(0,a-1): #g1Q3 =(1,0,1 ), grQ3=(1,2,1), exQ3=(6,3,0 )
        P[0]+=p[c] 
        m[0]+=c*p[c]
       
    #ultimo cluster
    b=f[K-2]+1 # calculo atribuido em exQ0 
 
    for c in range(b,M-1): #g1Q4 =(1,0,1 ), grQ4=(1,2,1), exQ4=(6,5,0 )
        P[K-1]+=p[c]
        m[K-1]+=c*p[c]
       
    
    #clusters intermediarios  
    if K>2 : # BQ g1 =(1,1,1 )
        d= K-1 
        for k in range(1,d-1):#g1BQk1 =(1,0,1 ), grBQk1=(1,2,1) exBQk1=(4,3,0 )
            a =f[k-1]+1 #
            b=f[k]+1
            for j in range(a,b-1):#g1BQk2 =(1,0,1 ), grBQk2=(1,2,1) exBQk2=(6,3,0 )
                P[k]+=p[j]
                m[k]+=j*p[j]
                
    mG=0
    for i in range(0,K):#g1Q5 =(1,0,1 ), grQ5=(1,1,1) exQ5=(3,2,0 )
         mG+=P[i]*m[i]
         
    Q = 0
    for i in range(0,K): #g1Q6 =(1,0,1 ), grQ6=(1,1,1) exQ6=(3,5,0 )
        Q+=P[i]*(m[i]-mG)**2
    
    
    return Q
