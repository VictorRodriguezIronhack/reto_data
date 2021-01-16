import pandas as pd

def mean_consume(dframe, feature):
    mean_cons = {f'{feature} on / SP95': [round(dframe[(dframe[feature] == 1) & (dframe.gas_SP98 == 0)]['consume'].mean(), 2)],
                f'{feature} on / SP95 price': [round(dframe[(dframe[feature] == 1) & (dframe.gas_SP98 == 0)]['trip_price'].mean(), 2)],
                f'{feature} on / SP98': [round(dframe[(dframe[feature] == 1) & (dframe.gas_SP98 == 1)]['consume'].mean(), 2)],
                f'{feature} on / SP98 price': [round(dframe[(dframe[feature] == 1) & (dframe.gas_SP98 == 1)]['trip_price'].mean(), 2)],
                f'{feature} off / SP95': [round(dframe[(dframe[feature] == 0) & (dframe.gas_SP98 == 0)]['consume'].mean(), 2)],
                f'{feature} off / SP95 price': [round(dframe[(dframe[feature] == 0) & (dframe.gas_SP98 == 0)]['trip_price'].mean(), 2)],
                f'{feature} off / SP98': [round(dframe[(dframe[feature] == 0) & (dframe.gas_SP98 == 1)]['consume'].mean(), 2)],
                f'{feature} off / SP98 price': [round(dframe[(dframe[feature] == 0) & (dframe.gas_SP98 == 1)]['trip_price'].mean(), 2)]}

    return pd.DataFrame.from_dict(mean_cons)