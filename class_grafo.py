class Grafo:
  def __init__(self,V):
    self.V = V
    self.infinito=10000
    self.c=[]
    self.w=[]
    self.custo=[]
    i=0
    j=0

    for i in range(V+1):
      self.custo.append([])	
      self.c.append(-2)
      self.w.append(i)
      for j in range(V+1):
        self.custo[i].append(self.infinito)
        if(i==j):
          self.custo[i].append(0)
         



  def addAresta(self,v1, v2, cus):
    if(v1!=0 or v2!=0):
      self.custo[v1-1][v2-1]=cus
      self.custo[v2-1][v1-1]=self.custo[v1-1][v2-1]


  def prim(self):

      orig=0
      p1=[]
      p2=[]
      self.lst=0
      st=0
      n=self.V
      self.c[orig]=orig
 
 
      t=0
      for t in range(n):
        p1.append(self.V+1)
        p2.append(self.V+1)
        if(self.w[t]==self.c[t]):
          if(t!=0):
            self.w[t]=-t
          else:
            self.w[t]=-1

     #Passo 1:
#      while(k!=self.V+1):
      k=0
      i=orig
      while(k!=self.V-1):
        menor=100000
        t=0
        for t in range(self.V):
          if( t== self.w[t] ):
            j=0
            for j in range(self.V):
              if(self.c[j]==j):
                if((self.custo[j][t]<menor)==True):
                  menor=int(self.custo[j][t])
                  p1[k]=int(j)
                  p2[k]=int(t)
                  i=int(t)
              j+=1
          t+=1
        
        self.c[i]=int(i)
        self.w[i]=-int(i)
        self.lst+=int(menor)
        self.element="ST = {"

        t=0
        for t in range(k+1):
          if(t==k):
            self.element+="("+str(p1[t]+1)+","+str(p2[t]+1)+")";
          else:
            self.element+="("+str(p1[t]+1)+","+str(p2[t]+1)+");";
          t+=1
        
        self.element+="}";
        k+=1






  def retornaValorCusto(self):
      return self.lst


  def retornaValorRota(self):
      return self.element
