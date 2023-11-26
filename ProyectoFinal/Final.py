from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_bd', methods=['POST'])
def crear_bd():
    try:
        con = sqlite3.connect("base_de_datos.db")
        con.commit()
        con.close()
        return jsonify({'mensaje': 'Base de datos creada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/create_table', methods=['POST'])
def create_table():
    try:
        con = sqlite3.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                        name text, 
                        surname text, 
                        age integer, 
                        gender text, 
                        cellphone integer, 
                        email text,
                        password text)""")
        con.commit()
        con.close()
        return jsonify({'mensaje': 'Tabla creada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        name = data.get('name')
        surname = data.get('surname')
        age = data.get('age')
        gender = data.get('gender')
        cellphone = data.get('cellphone')
        email = data.get('email')
        password = data.get('password')

        con = sqlite3.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, surname, age, gender, cellphone, email, password))
        con.commit()
        con.close()

        return jsonify({'mensaje': 'Usuario registrado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = data.get('user')
        password = data.get('password')

        con = sqlite3.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute('SELECT name, password FROM usuarios WHERE name=? AND password=?', (user, password))
        if cursor.fetchall():
            return jsonify({'mensaje': 'Ingreso completo'})
        else:
            return jsonify({'error': 'El usuario o la contraseña son incorrectos'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)