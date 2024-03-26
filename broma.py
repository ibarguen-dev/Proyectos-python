import pickle

texto = "hey mano que vamos hacer el dia de hoy"

fichero = open("virus","wb")

pickle.dump(texto, fichero)

fichero.close()

del fichero