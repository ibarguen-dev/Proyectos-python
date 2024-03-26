import sqlite3

try:
	
    #creamos la conexion del programa con la base de datos
    miConexion=sqlite3.connect("BaseDatos")
	

    #creamos el cursor que no permite hacer el manejo de la base de datos
    miCursor=miConexion.cursor()


    #insertamos datos a la base de datos
    miCursor.execute("select * from productos ")

    resultado = miCursor.fetchall()

    print(resultado)
    #comfirmanos los cambios de la base de datos
    miConexion.commit()


except Exception as e:
	print(e)

finally:
	#cerramos la conexion a la base de datos
	miConexion.close() 