
def run_gradient_boosting():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.metrics import mean_squared_error
    # Load data
    sales_data = pd.read_csv("GDS.csv")
    distance_matrix = pd.read_csv("Distances.csv")

    # Function to get distance between regions
    def get_distance_matrix(region_from, df_distance_matrix):
        distances = df_distance_matrix.loc[df_distance_matrix['Wojewodztwo'] == region_from]
        return distances.drop('Wojewodztwo', axis=1)

    # Merge sales data with distances from the given region
    def merge_distance(sales_data, region_from, df_distance_matrix):
        distance_from_region = get_distance_matrix(region_from, df_distance_matrix)
        distance_from_region = distance_from_region.T.reset_index()
        distance_from_region.columns = ['Wojewodztwo', 'Distance_from_given_region']
        merged_data = pd.merge(sales_data, distance_from_region, on='Wojewodztwo', how='left')
        return merged_data

    # Prepare the data for the model
    def prepare_data_for_model(merged_data):
        X = merged_data[['Miesiac', 'Cena detaliczna', 'Distance_from_given_region']]
        y = merged_data['Ilosc sprzedanych']
        return X, y

    # Train Gradient Boosting Machine model
    def train_gbm(X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Model Mean Squared Error: {mse}")
        return model

    # Function to calculate the transportation cost
    def calculate_transportation_cost(distance, cost_per_km=0.50):
        return distance * cost_per_km

    # Function to penalize saturation in current region
    def apply_saturation_penalty(predicted_sales, region, region_from):
        if region == region_from:
            return predicted_sales * 0.9  # Penalize by reducing sales by 10% due to saturation
        return predicted_sales

    # Updated predict function to include saturation penalty and transportation cost
    def predict_best_region_with_saturation(product, region_from, df_sales, df_distance_matrix, cost_per_km=0.50):
        filtered_sales = df_sales[df_sales['Nazwa produktu'] == product]
        merged_data = merge_distance(filtered_sales, region_from, df_distance_matrix)
        X, y = prepare_data_for_model(merged_data)
        model = train_gbm(X, y)

        # Predict for all regions
        regions_predictions = merged_data[['Wojewodztwo', 'Distance_from_given_region']].copy()
        regions_predictions['Predicted_Sales'] = model.predict(X)

        # Apply saturation penalty for the current region
        regions_predictions['Adjusted_Predicted_Sales'] = regions_predictions.apply(
            lambda row: apply_saturation_penalty(row['Predicted_Sales'], row['Wojewodztwo'], region_from), axis=1
        )

        # Calculate transportation cost and adjust predicted sales
        regions_predictions['Transportation_Cost'] = regions_predictions['Distance_from_given_region'].apply(
            lambda x: calculate_transportation_cost(x, cost_per_km)
        )
        regions_predictions['Net_Sales'] = regions_predictions['Adjusted_Predicted_Sales'] - regions_predictions[
            'Transportation_Cost']

        # Group by region to avoid duplicates (take mean of predictions)
        best_regions = regions_predictions.groupby('Wojewodztwo').mean().reset_index()

        # Sort by highest net sales after considering transportation cost and saturation
        best_regions = best_regions.sort_values(by='Net_Sales', ascending=False)
        return best_regions

    ################################################################################################################
    #TUTAJ MAREK TRZEBA ZMIENIC#
    product = "Piwo"
    region_from = "Mazowieckie"

    # Predict the best regions to sell the product with transportation cost and saturation penalty
    best_regions_with_saturation = predict_best_region_with_saturation(product, region_from, sales_data, distance_matrix)

    # Add this before printing the DataFrame to show all columns fully
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)

    output_file = "./Output/results.txt"
    # Save the best regions output to the text file
    best_regions_output = best_regions_with_saturation[['Wojewodztwo', 'Net_Sales', 'Adjusted_Predicted_Sales', 'Transportation_Cost']].head()

    # Append the output to the file without overwriting
    text_output_file = './Output/results.txt'
    with open(text_output_file, 'a') as file:
        file.write("#MODEL GBR#\n")

    best_regions_output.to_csv(output_file, sep='\t', index=False, header=False, mode='a')
