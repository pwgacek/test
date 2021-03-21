def hoare_partition(T, l, p):
  i = l
  j = p
  x = T[(l+p)//2] # better to choose mid value from 3 instead of a single shot
  
  while i<=j:
    while T[i] < x:
      i+=1
    while T[j]>x:
      j-=1
    if i<=j:
      T[j],T[i]=T[i],T[j]
      i+=1
      j-=1
  
  return i
