import pandas as pd
import easygui

file = easygui.fileopenbox("Select a file", "AIB to YNAB CSV Convertor", filetypes = ["*.csv"])

print(file)

# create pandas dataframe by reading in the file input.csv
df=pd.read_csv(file)

cols_to_keep = [' Posted Transactions Date',' Description1',' Debit Amount',' Credit Amount']

# Create a new pandas dataframe with on the columns we want to keep
df_new = df[cols_to_keep]

# rename the columns
df_new.columns = ['Date','Payee','Outflow','Inflow']

# fill in the blanks with a zero
df_new = df_new.fillna(0)

# add a column to the new dataframe with a value of empty string for all rows
# column needed for import to work
df_new.loc[:,'Memo'] = ""

# write new dataframe to csv file called output.csv
df_new.to_csv("output.csv", index=False)
