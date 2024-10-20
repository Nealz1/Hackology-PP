import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Ładowanie danych
data = pd.read_csv('miasta2.csv', encoding='ISO-8859-1')
print("Dane załadowane poprawnie.\n")


def show():
    print("=======================================================================")
    print(data.isnull().sum())
    # print("=======================================================================")
    # print(data[data.isnull().any(axis=1)])
    # print("=======================================================================")


def end():
    input("Naciśnij Enter, aby kontynuować...")
    os.system('cls')


def menu():
    print("1. Wyświetl aktualne statystyki.")
    print("2. Usuń brakujące dane.")
    print("3. Wypełnianie brakujących wartości w kolumnie 'area' średnią wartością.")
    print("4. Przykład imputacji regresyjnej dla kolumny 'area'.")
    print("7. Zakończ działanie. \n")


while True:
    menu()

    while True:
        user_input = input("Podaj numer opcji: ").strip()
        if user_input.isdigit():
            option = int(user_input)
            break
        else:
            print("Błąd: Proszę podać poprawny numer opcji.")

    match option:
        case 1:
            show()
            end()
        case 2:
            # Usunięcie brakujących danych, jeśli nie są potrzebne
            data.dropna(inplace=True)
            data.to_csv('p1.csv', index=False)
            print("Brakujące dane zostały usunięte i zapisane do 'p1.csv'.")
            end()
        case 3:
            data['area'] = data['area'].fillna(data['area'].mean())
            end()
        case 4:
            # Przykład imputacji regresyjnej dla kolumny 'area'
            kolumna = 'area'

            train_set = data.dropna()
            train_set = pd.get_dummies(train_set, drop_first=True)

            X = train_set.drop([kolumna], axis=1)
            y = train_set[kolumna]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LinearRegression()
            model.fit(X_train, y_train)

            missing_data = data[data[kolumna].isnull()]
            missing_data_encoded = pd.get_dummies(missing_data.drop([kolumna], axis=1), drop_first=True)
            missing_data_encoded = missing_data_encoded.reindex(columns=X_train.columns, fill_value=0)

            imputer = SimpleImputer(strategy='median')
            missing_data_encoded_imputed = imputer.fit_transform(missing_data_encoded)

            data.loc[data[kolumna].isnull(), kolumna] = model.predict(missing_data_encoded_imputed)
            data.to_csv('p1.csv', index=False)
            print("Dane zostały zapisane do 'p1.csv'.")

            end()

        case 7:
            print("Do zobaczenia!")
            break
        case _:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
            end()