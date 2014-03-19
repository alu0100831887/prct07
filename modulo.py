#!/usr/bin/python
PI = 3.14159265358979323846264338327950288
def aproximacion(n):  
 if (n!=0):
   s = 0.0
   for i in range(1,n+1):
    a= float(i-1)/n
    b= float (i)/n
    xi= (i-0.5)/n
    fxi= 4.0/(1.0 + xi*xi)
    s+=fxi
   r=s/n
   return r
   
if (__name__=="__main__"):
  import sys
  if((len(sys.argv) ==1) or (len(sys.argv) == 2)):
    print("No se han introducido todos los argumentos")
    n = 10
    m = 10
  else:
    n= int(sys.argv[1])
    m= int(sys.argv[2])
  lista=[]
  for j in range (1, m+1):
    pi = aproximacion(j*m)
    lista = lista+[pi]
  print lista
