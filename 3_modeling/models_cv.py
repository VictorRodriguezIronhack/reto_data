import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.model_selection import cross_validate
import xgboost as xgb
from sklearn.neighbors import KNeighborsRegressor

def modeling(X, y, cv):
    
    r_models = [LinearRegression(), DecisionTreeRegressor(), RandomForestRegressor(), 
                SVR(kernel='rbf'), Ridge(), GradientBoostingRegressor(), xgb.XGBRegressor(), 
                KNeighborsRegressor()]

    stdev = []
    rmse = []
    
    for model in r_models:
        results = cross_validate(model, X, y, scoring=('neg_root_mean_squared_error', 'r2'), cv=cv)

        rmse.append(-results['test_neg_root_mean_squared_error'].mean())
        stdev.append(-results['test_neg_root_mean_squared_error'].std())
    
    df = pd.DataFrame({'model': ['Linear Regression', 
                                        'Decission Tree', 
                                        'Random Forest Regressor', 
                                        'Support Vector Machine', 
                                        'Ridge Regression', 
                                        'Gradient Boost Regression',
                                        'XGboost Regression',
                                        'K Nearest Neighbors'],
                            'RMSE': rmse,
                            'standard_dev': stdev}
                        )

    return df

