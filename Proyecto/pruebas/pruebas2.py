import sqlite3 as sql
nr="R.Circular"
conex = sql.connect("rutas.db")
cursor = conex.cursor()
p1 = cursor.execute(f"SELECT parada_1 FROM rutas WHERE nombre_ruta='{nr}'").fetchall()
p1 = p1[0][0]
p2 = cursor.execute(f"SELECT parada_2 FROM rutas WHERE nombre_ruta='{nr}'").fetchall()
p2 = p2[0][0]
p3 = cursor.execute(f"SELECT parada_3 FROM rutas WHERE nombre_ruta='{nr}'").fetchall()
p3= p3[0][0]
p4 = cursor.execute(f"SELECT parada_4 FROM rutas WHERE nombre_ruta='{nr}'").fetchall()
p4 = p4[0][0]
conex.commit()
conex.close()
