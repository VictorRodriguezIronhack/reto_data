from sklearn.preprocessing import quantile_transform
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression


from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import cross_validate
import xgboost as xgb



def training(X_train, y_train, cv):
    regression_models = [LinearRegression(), DecisionTreeRegressor(), RandomForestRegressor(), Ridge(), GradientBoostingRegressor(), xgb.XGBRegressor()]
    stdev = []
    rmse = []
    
    for model in regression_models:
        results = cross_validate(model, X_train, y_train, scoring=('neg_root_mean_squared_error', 'r2'), cv=cv)

        rmse.append(-results['test_neg_root_mean_squared_error'].mean())
        stdev.append(-results['test_neg_root_mean_squared_error'].std())

    df_models_trained = pd.DataFrame({'model': ['Linear Regression', 
                                        'Decission Tree', 
                                        'Random Forest Regressor', 
                                        'Ridge Regression', 
                                        'Gradient Boost Regression',
                                        'XGboost Regression'
                                        ],
                            'RMSE': rmse,
                            'standard_dev': stdev}
                        )
    return df_models_trained


def tr_test_split(df, n_quantiles):
    X = df.drop(['consume'], axis=1)
    y = df.consume
#as we need to normalize the variables which are a little skewed we use quantile transform:
#output_distribution{‘uniform’, ‘normal’}, default=’uniform’
#Marginal distribution for the transformed data. The choices are ‘uniform’ (default) or ‘normal’.
    X_norm = quantile_transform(X, n_quantiles=n_quantiles, output_distribution='normal')


    X_norm_df = pd.DataFrame(X_norm,
                        index=X.index, 
                        columns=X.columns)

    X_train, X_test, y_train, y_test = train_test_split(X_norm_df, y, test_size=0.2, random_state=42)
    return(X_train, X_test, y_train, y_test)