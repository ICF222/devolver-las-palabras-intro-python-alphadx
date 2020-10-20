def crea_lista_letras():
  lista_letras = []
  lista_letras = input("Ingrese las letras separadas por un espacio entre ellas:   ")
  return lista_letras

def validacion(lista_letras, linea):
  lista_respaldo = []
  for index in lista_letras:
    lista_respaldo.append(index)
  for i in linea:
    encontrado = False
    for j in lista_respaldo:
      if i == j:
        encontrado = True
        lista_respaldo.remove(j)
        break
    if encontrado == False:
      return False
  return True




def lee_archivo(lista_letras):
  f = open ('listado-general-filtrado.txt','r')
  lista_palabras_aceptadas = []
  for i in f:
    linea = i
    linea = linea.rstrip('\n')
    if validacion(lista_letras, linea) == True:
      lista_palabras_aceptadas.append(linea)

  print(lista_palabras_aceptadas)


def main():
  lista_letras = crea_lista_letras()

  lee_archivo(lista_letras)
  

if(__name__ == "__main__"):
    main()