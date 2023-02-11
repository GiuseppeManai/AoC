import pandas as pd

# Read in the file and include blank rows
input_data = pd.read_csv("puzzle1_input.txt", names=["calories"], skip_blank_lines=False)

# Determine the number of elves
count_elves = input_data["calories"].isna().sum() + 1
print("I expect to have in total", count_elves, "elves")

# Generate unique identifier for each block of non-blank rows
block_ids = 1 + input_data['calories'].isna().cumsum()

# Add a new column called 'tot_calories'
input_data['tot_calories'] = input_data['calories'].fillna(0)


# Group data by unique identifiers and aggregate into separate columns
grouped = input_data.groupby(block_ids)['tot_calories'].sum().reset_index()
grouped.rename(columns={'calories':'elf'},inplace=True)

max_row = grouped.loc[grouped['tot_calories']==grouped['tot_calories'].max()]
print('The elf with highest calories is', max_row['elf'].values, 'which has taken',max_row['tot_calories'].values,'calories.')