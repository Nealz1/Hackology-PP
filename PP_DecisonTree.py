def run_decision_tree():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import mean_squared_error

    # Wczytanie danych z pliku CSV
    file_path = 'GDS.csv'
    df = pd.read_csv(file_path)

    # Przygotowanie danych
    # Zmienna celu - Cena detaliczna
    y = df['Cena detaliczna']

    # Zmienne objaśniające (możemy wybrać kolumny: Miesiąc, Typ sklepu, Ilość sprzedanych, Województwo)
    X = df[['Nazwa produktu','Kategoria produktu', 'Ilosc sprzedanych','Wojewodztwo','Miesiac','Promocja']]

    # Kodowanie zmiennych kategorycznych za pomocą one-hot encoding
    X = pd.get_dummies(X, columns=['Nazwa produktu','Kategoria produktu','Wojewodztwo'])

    #Podział danych na treningowe i testowe
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Trenowanie modelu drzewa decyzyjnego
    model = DecisionTreeRegressor( random_state=42)

    model.fit(X_train, y_train)

    nazwa=''
    kategoria=''
    ilosc=0
    wojewodztwo=''
    miesiac=0
    promocja=0

    # Nowe dane (zastąp wartości rzeczywistymi danymi)
    new_data = pd.DataFrame({
        'Nazwa produktu': [nazwa],
        'Kategoria produktu': [kategoria],
        'Ilosc sprzedanych':[ilosc],
        'Wojewodztwo':[wojewodztwo],
        'Miesiac':[miesiac],
        'Promocja':[promocja]
    })

    # Kodowanie zmiennych kategorycznych w nowych danych (tak jak w danych treningowych)
    new_data = pd.get_dummies(new_data, columns=[ 'Nazwa produktu','Kategoria produktu', 'Ilosc sprzedanych','Wojewodztwo','Miesiac','Promocja'])

    # Dopasowanie nowych danych do kolumn, które były używane w treningu modelu
    new_data = new_data.reindex(columns=X_train.columns, fill_value=0)

    # Przewidywanie ceny detalicznej na podstawie nowych danych
    predicted_price = model.predict(new_data)
    prediction_df = predicted_price

    text_output_file = './Output/results.txt'
    with open(text_output_file, 'a') as file:
        file.write("#MODEL DTR#\n")
        for i in range(len(prediction_df)):
            file.write(f"{prediction_df[i]:.2f}\n")
