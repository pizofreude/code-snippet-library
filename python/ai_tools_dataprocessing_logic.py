# Brainstorm Session 1 for AI Investment Analyzer
# Data collection and preprocessing logic

# Import necessary libraries
import numpy as np
import pandas as pd

# Collect historical financial data for test stocks
stocks = ["AAPL", "GOOGL", "MSFT"]
df = pd.DataFrame()
for stock in stocks:
    df[stock] = pd.DataReader(stock, "yahoo")["Close"]

# Clean and preprocess big data
df = df.dropna()
df = df.pct_change()

# Feature engineering
df["Volatility"] = df.rolling(window=20).std()
df["Correlation"] = df.corr()

# Split data into training & test sets
X_train, X_test, y_train, y_test = train_test_split(df.drop("Correlation", axis=1), df["Correlation"], test_size=0.25)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model's performance on the test set
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)
print("Model R-squared score:", score)

