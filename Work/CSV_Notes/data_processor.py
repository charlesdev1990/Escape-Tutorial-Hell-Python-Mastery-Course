import csv
import pandas 

print("=== SALES SUMMARY REPORT===")
df = pandas.read_csv('sales_data.csv')

total = len(df)
print(f"Total Records: {total}")


print(f"Data Range: {df.iloc[0]}")



# for row in df:
#         print(row)    