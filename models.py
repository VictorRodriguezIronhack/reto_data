import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

def modeling(X, y):
    # Train - Test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

    # Linear Regression
    lreg = LinearRegression().fit(X_train, y_train)
    lreg_pred = lreg.predict(X_test)

    lreg_r2 = r2_score(y_test, lreg_pred)
    lreg_rmse = np.sqrt(mean_squared_error(y_test, lreg_pred))

    # Decission Tree
    dtreg = DecisionTreeRegressor().fit(X_train, y_train)
    dtree_pred = dtreg.predict(X_test)

    dtree_r2 = r2_score(y_test, dtree_pred)
    dtree_rmse = np.sqrt(mean_squared_error(y_test, dtree_pred))

    # Random Forest Regressor
    rfreg = RandomForestRegressor().fit(X_train, y_train)
    rfor_pred = rfreg.predict(X_test)

    rfor_r2 = r2_score(y_test, rfor_pred)
    rfor_rmse = np.sqrt(mean_squared_error(y_test, rfor_pred))

    # Support Vector Machine
    svm_reg = SVR(kernel='rbf').fit(X_train, y_train)
    svm_pred = svm_reg.predict(X_test)

    svm_r2 = r2_score(y_test, svm_pred)
    svm_rmse = np.sqrt(mean_squared_error(y_test, svm_pred))

    # Ridge Regression
    ridge_reg = Ridge().fit(X_train, y_train)
    ridge_pred = ridge_reg.predict(X_test)

    ridge_r2 = r2_score(y_test, ridge_pred)
    ridge_rmse = np.sqrt(mean_squared_error(y_test, ridge_pred))

    # Gradient Boost Regression
    gbr_reg = GradientBoostingRegressor().fit(X_train, y_train)
    gbr_pred = gbr_reg.predict(X_test)

    gbr_r2 = r2_score(y_test, gbr_pred)
    gbr_rmse = np.sqrt(mean_squared_error(y_test, gbr_pred))

    results = pd.DataFrame({'model': ['Linear Regression', 'Decission Tree', 'Random Forest Regressor', 'Support Vector Machine', 'Ridge Regression', 'Gradient Boost Regression'],
                            'R^2_score': [lreg_r2,dtree_r2,rfor_r2,svm_r2,ridge_r2,gbr_r2],
                            'RMSE': [lreg_rmse,dtree_rmse,rfor_rmse,svm_rmse,ridge_rmse,gbr_rmse]}
                        )

    return results

