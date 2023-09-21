# Import essential libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load historical financial data for test stocks
df = pd.DataFrame()
stocks = ["AAPL", "GOOGL", "MSFT"]
for stock in stocks:
    df[stock] = pd.DataReader(stock, "yahoo")["Close"]

# Clean and preprocess data samples
df = df.dropna()
df = df.pct_change()

# Feature engineering
df["Volatility"] = df.rolling(window=20).std()
df["Correlation"] = df.corr()

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df.drop("Correlation", axis=1), df["Correlation"], test_size=0.25)

# Define a function to calculate the model's performance on a given dataset
def calculate_model_performance(X, y, model):
  """Calculates the model's performance on a given dataset.

  Args:
    X: Input data.
    y: Target data.
    model: The machine learning model.

  Returns:
    A tuple containing the R-squared score and mean squared error.
  """

  y_pred = model.predict(X)
  r2_score = r2_score(y, y_pred)
  mse = mean_squared_error(y, y_pred)
  return r2_score, mse

# Training for linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the model's performance on the test set
r2_score, mse = calculate_model_performance(X_test, y_test, model)

# Print the model's performance
print("Model R-squared score:", r2_score)
print("Model mean squared error:", mse)
