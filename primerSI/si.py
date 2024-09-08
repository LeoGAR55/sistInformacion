import os
import sys

import mariadb

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root", password="12345", host="127.0.0.1", port=3306, database="nombres"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

nombre = input("Nombre a guardar:")
with open("C:/Users/Leo/Desktop/nombre.txt", "w") as file:
    file.write(nombre)
# insert information
try:
    cur.execute("INSERT INTO alumnos (nombre) VALUES (?)", (nombre,))
    conn.commit()
    print("Nombre guardado")
except mariadb.Error as e:
    print(f"Error: {e}")

# cerrar conexiones ?)
