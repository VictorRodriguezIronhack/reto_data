def gas_type_sum(df, data_type, column2):
    sum_data = df[df['gas_type'] == data_type][column2].sum()
    print(f'Total {column2} with {data_type}: ' + str(sum_data))
    return sum_data

def gas_type_mean(df, data_type, column2):
    mean_data = df[df['gas_type'] == data_type][column2].mean()
    print(f'Mean of {column2} with {data_type}: ' + str(mean_data))
    return mean_data
    
def gas_type_std(df, data_type, column2):
    std_data = df[df['gas_type'] == data_type][column2].std()
    print(f'Std of {column2} with {data_type}: ' + str(std_data))
    return std_data





'''
km_e10 = df[df['gas_type'] == 'E10']['distance'].sum()
km_sp98 = df[df['gas_type'] == 'SP98']['distance'].sum()

avg_e10 = df[df['gas_type'] == 'E10']['distance'].mean()
avg_sp98 = df[df['gas_type'] == 'SP98']['distance'].mean()

std_e10 = df[df['gas_type'] == 'E10']['distance'].std()
std_sp98 = df[df['gas_type'] == 'SP98']['distance'].std()

print('DISTANCES:')
print('Kilometers with E10: ' + str(km_e10))
print('Kilometers with SP98: ' + str(km_sp98))
print('Average distance with E10: ' + str(avg_e10))
print('Average distance with SP98: ' + str(avg_sp98))
print('Deviation of the distances with E10: ' + str(std_e10))
print('Deviation of the distancees with SP98: ' + str(std_sp98))
print('\n')
print(100*'*')
print('\n')
print('SPEED:')
avg_sp_e10 = df[df['gas_type'] == 'E10']['speed'].mean()
avg_sp_sp98 = df[df['gas_type'] == 'SP98']['speed'].mean()

std_sp_e10 = df[df['gas_type'] == 'E10']['speed'].std()
std_sp_sp98 = df[df['gas_type'] == 'SP98']['speed'].std()

print('Average speed with E10: ' + str(avg_sp_e10))
print('Average speed with SP98: ' + str(avg_sp_sp98))
print('Deviation of the speed with E10: ' + str(std_sp_e10))
print('Deviation of the speed with SP98: ' + str(std_sp_sp98))
'''