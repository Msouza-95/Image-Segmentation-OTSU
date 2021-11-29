def quality(f,K,M ,p ):
    m = [0]*K  #cor inicial dos clusters
    P = [0]*K #probabilidades dos clusters

  
    #primeiro cluster
    a = f[0]+1
    
    for c in range(0,a-1):
        P[0]+=p[c]
        m[0]+=c*p[c]
       
    #ultimo cluster
    b=f[K-2]+1
    
    for c in range(b,M-1):
        P[K-1]+=p[c]
        m[K-1]+=c*p[c]
       
    
    #clusters intermediarios  
    if K>2 :
        d= K-1
        for k in range(1,d):
            a =f[k-1]+1
            b=f[k]+1
            for j in range(a,b):
                P[k]+=p[j]
                m[k]+=j*p[j]
                
    mG=0
    for i in range(0,K):
         mG+=P[i]*m[i]
         
    Q = 0
    for i in range(0,K):
        Q+=P[i]*(m[i]-mG)**2
    
    
    return Q
