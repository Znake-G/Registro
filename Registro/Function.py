import sqlite3
try:
    con=sqlite3.connect("usuarios.db")
    con.commit()
    con.close()
except:
    print("Error al conectar con la base de datos")
    pass
def create_table():
    con.connect("usuarios.db")
    cursor=con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        Name text,
        Password text,
        Email text,
        Work Position text,
        Salary Integer)""")
    cursor = con.cursor()
    
    
def register(Name,Email,Password):
    con=sqlite3.connect("usuarios.db")
    cursor=con.cursor()
    cursor.execute("INSERT INTO usuarios VALUES(?,?,?)",
                   (Name,Email,Password))
    
    con.commit()
    con.close()
    return True