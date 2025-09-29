from flask import Flask, render_template, request, redirect, url_for
from services.xml_parser import cargar_configuracion, generar_salida
from services.simulador import Simulador

app = Flask(__name__)

invernaderos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cargar', methods=['POST'])
def cargar():
    archivo = request.files['archivo']
    archivo.save('entrada.xml')
    global invernaderos
    invernaderos = cargar_configuracion('entrada.xml')
    return redirect(url_for('index'))

@app.route('/simular', methods=['POST'])
def simular():
    invernadero_nombre = request.form['invernadero']
    plan = request.form['plan']
    # Aquí se debe buscar el invernadero y plan seleccionados
    simulador = Simulador(None, plan)  # reemplazar None por invernadero
    simulador.ejecutar()
    generar_salida('salida.xml', simulador)
    return render_template('reporte.html', datos=simulador)

if __name__ == '__main__':
    app.run(debug=True)
