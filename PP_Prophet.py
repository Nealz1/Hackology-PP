def run_prophet():
    import pandas as pd
    from prophet import Prophet
    import app
    import matplotlib.pyplot as plt
    # Load your dataset
    df = pd.read_csv("GDS.csv")

    # Combine 'Rok' and 'Miesiac' to create a 'Date' column
    df['Date'] = pd.to_datetime(df['Rok'].astype(str) + '-' + df['Miesiac'].astype(str) + '-01')

    # Filter data for a specific product and region for forecasting
    ############################################################
    product = app.product_name  # Example product
    region = app.region  # Example region

    # Filter the dataset for the selected product and region
    filtered_df = df[(df['Nazwa produktu'] == product) & (df['Wojewodztwo'] == region)]

    # Prepare data for Prophet
    # Prophet requires columns to be named 'ds' for date and 'y' for the metric you want to predict (sales)
    prophet_df = filtered_df[['Date', 'Ilosc sprzedanych']].rename(columns={'Date': 'ds', 'Ilosc sprzedanych': 'y'})

    # Initialize and fit the Prophet model
    model = Prophet()
    model.fit(prophet_df)

    # Make future predictions
    future = model.make_future_dataframe(periods=12, freq='ME')  # Predicting for the next 12 months
    forecast = model.predict(future)

    # Visualize the forecast
    model.plot(forecast)
    plt.title(f'Demand Forecast for {product} in {region}')
    plt.show()
    print("PROPHET SIE WYJEBAL")
    text_output_file = './Output/results.txt'
    with open(text_output_file, 'a') as file:
        file.write("#MODEL Prophet#\n")

    forecast_tail = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12)
    forecast_tail.to_csv("./Output/results.txt", sep='\t', index=False, header=True, mode='a')
