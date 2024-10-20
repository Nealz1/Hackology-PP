def run_random_forest():
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.preprocessing import StandardScaler



    # Wczytanie danych
    data = pd.read_csv('GDS.csv')

    # Sprawdzenie braków
    print(data.isnull().sum())

    # Kodowanie zmiennych kategorycznych
    data_encoded = pd.get_dummies(data, columns=['Nazwa produktu', 'Kategoria produktu', 'Wojewodztwo', 'Typ sklepu'])

    # Podział danych na cechy i etykietę
    X = data_encoded
    y = data_encoded['Ilosc sprzedanych']

    # Podział na zestaw treningowy i testowy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=89)

    # Standaryzacja cech
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Ustawienia dla GridSearchCV
    param_grid = {
        'n_estimators': [100],
        'max_depth': [10],
        'min_samples_split': [2],
    }

    # Tworzenie obiektu Random Forest
    rf = RandomForestRegressor(random_state=89)

    # Tworzenie obiektu GridSearchCV
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=2, scoring='neg_mean_squared_error', verbose=2,
                            n_jobs=-1)

    # Dopasowanie modelu
    print("Rozpoczynam szkolenie")
    grid_search.fit(X_train, y_train)
    print("Koniec szkolenia")

    # Najlepsze parametry
    print(f'Najlepsze parametry: {grid_search.best_params_}')

    # Użycie najlepszego modelu do przewidywań
    best_model = grid_search.best_estimator_
    pred = best_model.predict(X_test)

    # Ocena modelu
    mse = mean_squared_error(y_test, pred)
    print(f'MSE: {mse}')

    # Tworzenie wykresu
    #plt.figure(figsize=(10, 6))
    #plt.scatter(pred, y_test, alpha=0.6, label='Predykcje')
    #plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linewidth=2, label='Idealna prognoza')
    #plt.title('Porównanie przewidywanych i rzeczywistych wartości sprzedaży')
    #plt.xlabel('Przewidywana ilość sprzedanych')
    #plt.ylabel('Rzeczywista ilość sprzedanych')
    #plt.legend()
    #plt.grid()
    #plt.show()

    results_df = pd.DataFrame({
        'Rzeczywista sprzedaż': y_test,
        'Przewidywana sprzedaż': pred
    })

    text_output_file = './Output/results.txt'
    with open(text_output_file, 'a') as file:
        file.write("#MODEL RFR#\n")
    # Zapisanie do pliku CSV
    results_df.to_csv('./Output/results.txt', index=False, mode='a')
