import pandas as pd 

df = pd.read_csv('../data/train.csv')

# length of protein_sequence
df['dim_seq'] = df['protein_sequence'].str.len()
result_max = df['dim_seq'].max()
result_min = df['dim_seq'].min()
result_mean = df['dim_seq'].mean()
print(f'Max Length of protein sequence: {result_max}')
print(f'Min Length of protein sequence: {result_min}')
print(f'Mean Length of protein sequence: {result_mean}')

df2 = pd.read_csv('../data/new_train.csv')
print(df2.head())