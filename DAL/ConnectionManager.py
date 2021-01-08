import sqlite3


class ConnectionManager:

    def crear_conexion(self, base_datos):
        try:
            conexion = sqlite3.connect(base_datos)
            return conexion
        except:
            return None

    def crear_tabla(self, conexion, tabla):
        cursor = conexion.cursor()
        cursor.execute(tabla)
        conexion.commit()