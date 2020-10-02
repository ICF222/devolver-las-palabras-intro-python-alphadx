def main():
  #La variable palabras es una lista con cada palabra del archivo de entrada
  palabras = list() #["hola", "persona", "soy", "yo", "el", "profe"]
  with open("./listado-general-filtrado.txt", "r") as entrada:
    for i in entrada:
      palabras.append(i[0:-1])

  #La variable listaLetras es una lista donde en cada elemento habrá un símbolo de las letras recibidas por el usuario
  lista_letras = list(input("Ingrese el listado de letras: ")) #["p","a","l","a","b","r","a"]

  #escriba su lógica aquí

if(__name__ == "__main__"):
  main()