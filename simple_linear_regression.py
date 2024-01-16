# Standard operational packages.
import pandas as pd

# Modeling and evaluation packages.
import statsmodels.api as sm
from statsmodels.formula.api import ols

import joblib

# path = "../../../data/"
# df = pd.read_csv(path + "marketing_sales_data.csv")
df = pd.read_csv("marketing_sales_data.csv")

df.isna()

ols_data = df[["Radio", "Sales"]]
ols_formula = "Sales ~ Radio"

OLS = ols(data=ols_data, formula=ols_formula)
model = OLS.fit()

joblib.dump(model, "simple_linear_regression_model.pkl")
