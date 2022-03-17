import numpy as np
import pandas as pd

def donwcast_df(df, objet_to_category=False, verbose=1):
    '''
    This function takes a dataframe and gives another dataframe with the same information but with the column type combination that uses less memory. 

    Parameters:
    df (DataFrame): DataFrame to reduce the space it occupies.

    object_to_category (boolean): option to transform object columns to category ones.

    verbose (int): option to modify the amount of prints with information about the data transformation. It goes from 0 to 2.

    Returns:
    DataFrame: Dataframe with column type combination that uses less memory. 
    '''
    if verbose >= 1:
        # Print initial state
        start_mem_usg = df.memory_usage().sum() / 1024**2 
        print("Memory usage of properties dataframe is :",start_mem_usg," MB")

    if objet_to_category:
        for e in df.select_dtypes('object').columns:

            if verbose == 2:
                # Print current column type
                print("******************************")
                print("Column: ",e)
                print("dtype before: object")
        
            df[e]=df[e].astype('category')

            if verbose == 2:
            # Print new column type
                print("dtype after: ",df[e].dtype)
                print("******************************")

    for e in df.select_dtypes('integer').columns:

        if verbose == 2:
            # Print current column type
            print("******************************")
            print("Column: ",e)
            print("dtype before: category")

        df[e]=pd.to_numeric(df[e], downcast='integer')

        if verbose == 2:
            # Print new column type
            print("dtype after: ",df[e].dtype)
            print("******************************")

    for e in df.select_dtypes('float').columns:
        
        if verbose == 2:
            # Print current column type
            print("******************************")
            print("Column: ",e)
            print("dtype before: float")

        df[e]=pd.to_numeric(df[e], downcast='float')

        if verbose == 2:
            # Print new column type
            print("dtype after: ",df[e].dtype)
            print("******************************")

    if verbose >= 1:
        # Print final result
        print("___MEMORY USAGE AFTER COMPLETION:___")
        mem_usg = df.memory_usage().sum() / 1024**2 
        print("Memory usage is: ",mem_usg," MB")
        print("This is ",100*mem_usg/start_mem_usg,"% of the initial size")