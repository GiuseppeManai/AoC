import pandas as pd

# Read in the file,give a name to the column and include blank rows
input_data = pd.read_csv("puzzle1_input.txt", names=["calories"], skip_blank_lines=False)
# print(type(input_data))
# file is loaded as a DataFrame

# Determine the number of elves
count_elves = input_data["calories"].isna().sum() + 1
print("I expect to have in total", count_elves, "elves")

# Generate a unique identifier for each block of non-blank rows
block_ids = 1 + input_data['calories'].isna().cumsum()

# Add a new column called 'tot_calories'
input_data['tot_calories'] = input_data['calories'].fillna(0)

# Group data by block_ids and aggregate to find the sum of calories
grouped = input_data.groupby(block_ids)['tot_calories'].sum().reset_index()
grouped.rename(columns={'calories':'elf'},inplace=True)
# Check that you get the correct output. You should get 249 elves
# print(grouped.head())
# print(grouped.tail())

# Identify which is the row with the max total calories
max_row = grouped.loc[grouped['tot_calories']==grouped['tot_calories'].max()]
print('The elf with highest calories is', max_row['elf'].values, 'which has taken',max_row['tot_calories'].values,'calories.')