from io import open

archivo_texto = open("archivo_texto.txt", "r+")

lista_texto = archivo_texto.readlines()

lista_texto[0] = "Hola carlos"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()