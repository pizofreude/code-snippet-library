import unittest
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

class TestInvestmentAnalyzer(unittest.TestCase):
    def setUp(self):
        # Collect historical financial data for test stocks
        stocks = ["AAPL", "GOOGL", "MSFT"]
        self.df = pd.DataFrame()
        for stock in stocks:
            self.df[stock] = pd.DataReader(stock, "yahoo")["Close"]

        # Clean and preprocess big data
        self.df = self.df.dropna()
        self.df = self.df.pct_change()

        # Feature engineering
        self.df["Volatility"] = self.df.rolling(window=20).std()
        self.df["Correlation"] = self.df.corr()

        # Split data into training & test sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df.drop("Correlation", axis=1), self.df["Correlation"], test_size=0.25)

        # Train a simple linear regression model
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

    def test_model_performance(self):
        # Evaluate the model's performance on the test set
        y_pred = self.model.predict(self.X_test)
        score = r2_score(self.y_test, y_pred)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

if __name__ == '__main__':
    unittest.main()