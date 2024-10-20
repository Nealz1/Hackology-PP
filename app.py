from flask import Flask, render_template, request, send_from_directory
import subprocess
import os

# Utwórz aplikację Flask i wskaż ścieżki dla statycznych plików i szablonów
app = Flask(__name__, static_folder='frontend', template_folder='frontend')

# Główna strona formularza
@app.route('/')
def form():
    return render_template('formularz.html')

# Obsługa danych formularza i wywołanie skryptu Pythona
@app.route('/submit', methods=['POST'])
def submit():
    product_name = request.form['product_name']
    category = request.form['category']
    costs = request.form['costs']
    quantity = request.form['quantity']
    region = request.form['region']
    start_month = request.form['start_month']
    end_month = request.form['end_month']
    price = request.form.get('price', None)

    # Wywołanie master_script.py z parametrami
    subprocess.call(['python', 'master_script.py', product_name, category, costs, quantity, region, start_month, end_month, price])

    return f"Skrypt master_script.py został uruchomiony dla produktu {product_name}."

# Serwowanie plików statycznych (CSS, JS) z folderu frontend
@app.route('/frontend/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

if __name__ == "__main__":
    app.run(debug=True)
