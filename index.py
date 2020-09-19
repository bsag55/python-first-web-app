#En la carpeta templates van los HTML que quiero enviar al usuario
#En la carpeta static van los estilos CSS
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # Página Principal
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__": # Asegurar que siempre esté "escuchando" 
    app.run(debug=True)  # Esto es para que no haya que reiniciar cada vez que haya un cambio
#CTRL + Shift + R, recarga la pagnina en el explorador sin caché