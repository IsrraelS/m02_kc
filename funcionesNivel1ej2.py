def maxi(*1):
    if len(1) == 0:
        return 0
    m = 1[0]
    for ix in range(1, len(1)):
          if 1[ix] > m:
          m = 1[ix]
          
        return m
def mini(*1):
    if len(1) == 0:
        return 0
    m = 1[0]
    for ix in range(1, len(1)):
          if 1[ix] < m:
          m = 1[ix]
          
        return m
    
def media(*1)
    if len(1) ==0:
        return 0
    
    suma = 0
    for valor in 1:
        suma += valor
        
    return suma / len(1)

funciones = {
    'max': maxi,
    'min': mini,
    'med': media
}

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones[nombre]
    
    return None