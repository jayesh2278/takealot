import pandas as pd

# Load the CSV files into pandas DataFrames
df_a = pd.read_csv('remain_products.csv')
df_b = pd.read_csv('main_search_result.csv')
df_c = pd.read_csv('jayesh.csv')
print(df_c['ManufacturerID'].nunique())
# print(df_c['ManufacturerName'].unique())
# # print(df_b.drop_duplicates)

# # # # Assuming the common column is named 'common_column', replace it with the actual column name
# # # # common_column_name = 'common_column'

# # # Find rows in A.csv that are not present in B.csv
# result_df = df_a[~df_a['ManufacturerItemCode'].isin(df_b['ManufacturerID'])]

# # # Save the result to a new CSV file, if needed
# result_df.to_csv('final_remain.csv',index=False)

# # # Display the result DataFrame, if needed
# print(result_df)


