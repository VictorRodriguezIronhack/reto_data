from scipy import stats
import pylab as pl
import pandas as pd
from sklearn.preprocessing import quantile_transform
from sklearn.model_selection import train_test_split

def normalizer(dframe, features, train_test=False):
    # Train-Test split
    X = dframe.drop(['consume'], axis=1)
    y = dframe.consume

    X_qtrans = quantile_transform(X, output_distribution='normal', random_state=0)

    X_scale = pd.DataFrame(X_qtrans,
                            index=X.index, 
                            columns=X.columns)

    if train_test == True:

        X_train, X_test, y_train, y_test = train_test_split(X_scale, y, test_size=.2, random_state=42)

        # Show the distributions after normalization
        X_train[features].hist(figsize=(12,5))
        pl.suptitle("Train set after normalization")
        X_test[features].hist(figsize=(12,5))
        pl.suptitle("Test set after normalization")

        return X_train, X_test, y_train, y_test

    elif train_test == False:

        # Show the distributions after normalization
        X_scale[features].hist(figsize=(12,5))
        pl.suptitle("X set after normalization")
        
        return X_scale, y
