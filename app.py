from flask import Flask, render_template, request, send_from_directory
import master_script

product_name = category = costs = quantity = region = start_month = end_month = price = None

app = Flask(__name__, static_folder='frontend', template_folder='frontend')

# Główna strona formularza
@app.route('/')
def form():
    return render_template('formularz.html')

# Obsługa danych formularza i wywołanie skryptu Pythona
@app.route('/submit', methods=['POST'])
def submit():
    global product_name, category, costs, quantity, region, start_month, end_month, price
    product_name = request.form['product_name'].title()
    category = request.form['category']
    costs = request.form['costs']
    quantity = request.form['quantity']
    region = request.form['region'].title()
    start_month = request.form['start_month']
    end_month = request.form['end_month']
    price = request.form.get('price', None)

    master_script.main()
    return f"Skrypt master_script.py został uruchomiony {product_name}, {region}"

@app.route('/frontend/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

if __name__ == "__main__":
    app.run(debug=True)
