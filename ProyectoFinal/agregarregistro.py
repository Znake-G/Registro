from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(_name_)
app.secret_key = 'tu_clave_secreta'  # Cambia esto por una clave segura

# Base de datos temporal para almacenar usuarios (simulación)
usuarios = {'admin': 'adminpass'}

# Función para verificar si el usuario está autenticado
def esta_autenticado():
    return 'usuario' in session

# Ruta de inicio de sesión
@app.route('/')
def inicio():
    if esta_autenticado():
        return render_template('index1.html', usuario=session['usuario'])
    return render_template('index.html')

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def iniciar_sesion():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    if usuario in usuarios and usuarios[usuario] == contrasena:
        session['usuario'] = usuario
        return redirect(url_for('inicio'))

    return 'Credenciales incorrectas'

# Ruta para cerrar sesión
@app.route('/logout')
def cerrar_sesion():
    session.pop('usuario', None)
    return redirect(url_for('inicio'))

# Ruta para registrar usuarios (solo accesible si el usuario está autenticado)
@app.route('/registrar', methods=['GET', 'POST'])
def registrar_usuario():
    if not esta_autenticado():
        return redirect(url_for('inicio'))

    if request.method == 'POST':
        nuevo_usuario = request.form['nuevo_usuario']
        nueva_contrasena = request.form['nueva_contrasena']
        # Puedes agregar lógica adicional aquí, como verificar si el usuario ya existe, etc.
        usuarios[nuevo_usuario] = nueva_contrasena
        return 'Usuario registrado con éxito'

    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)