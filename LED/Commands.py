
# LED - P2023
# pandas is a column-oriented data analysis API. It's a great tool for handling and analyzing input data.
# Many ML frameworks support pandas data structures as inputs.

# The intention of this session is to get to know the library and how it can be integrated within the LED course

# show how to import the pandas API
from pandas import Series, DataFrame
import pandas as pd

# The primary data structures in pandas are implemented as two classes:
#   DataFrame:  which you can imagine as a relational data table, with rows and named columns as part of its structure.
#   Series:     which is a single column.
# A DataFrame contains one or more Series and a name for each Series.
# The data frame is a commonly used abstraction for data manipulation. Similar implementations exist in Spark and R.

ser_1 = Series([1, 1, 2, -3, -5, 8, 13])
print(ser_1)
# Index objects are immutable and hold the axis labels and metadata such as names and axis names.

# Get the array representation of a Series:
print(ser_1.values)

# Get the index of the Series (secuencia iterable):
print(ser_1.index)

# Create a Series with a custom index:
ser_2 = Series([1, 1, 2, -3, -5], index=['a', 'b', 'c', 'd', 'e'])
print(ser_2)

# Get a value from a Series:
print(ser_2['e'])

# Get values great than 0:
print(ser_2[ser_2 > 0])

# Scalar multiply:
print(ser_2 * 2)

# Create a series by passing in a dict:
dict_1 = {'matematicas' : 100, 'quimica' : 200, 'logica' : 300}
ser_3 = Series(dict_1)
print(ser_3)

# DataFrame:
# A DataFrame is a tabular data structure containing an ordered collection of columns.
# Each column can have a different type.
# DataFrames have both row and column indices and which are analogous to a dict of Series.
# Row and column operations are treated roughly symmetrically

data_1 = {'estado' : ['JA', 'CO', 'MX', 'JA', 'LA'],
          'año' : [2012, 2013, 2014, 2014, 2015],
          'version' : [5.0, 5.1, 5.2, 4.0, 4.1]}
df_1 = DataFrame(data_1)
print(df_1)

# Create a DataFrame specifying a sequence of defined columns:
df_2 = DataFrame(data_1, columns=['año', 'estado', 'version'])
print(df_2)

# columns that are not present in the data are NaN (not a number):
df_3 = DataFrame(data_1, columns=['año', 'estado', 'version', 'newColumn'])
print(df_3)

df_4 = df_3.rename(columns={"newColumn": "rank"})
print(df_3)
print(df_4)

# Use inplace to do it in the actual Data Frame
df_3.rename(columns={"newColumn": "rank"}, inplace = True)
print(df_3)

# For multiple columns
# df_3.rename(columns={"unempl": "rank", "B": "c"}, inplace = True)

# Assign a Series to a column using a Series:
ranks_df3 = Series([1, 2, 3], index=[2, 3, 4])
df_3['rank'] = ranks_df3
print(df_3)

# Note: if assigning a list or array, the length must match the DataFrame, unlike a Series:
ranks_df4 = [1, 1, 2, 3, 4]
df_4['rank'] = ranks_df4
print(df_4)

# Retrieve a column by key, returning a Series:
print(df_3['estado'])

# Retrieve a row by position:
print(df_3.iloc[0])

# Retrieve a cell value:
print(df_4['estado'].iloc[1])
print(df_4.at[1,'estado'])

# .loc  - selects subsets of rows and columns by label only
# .iloc - selects subsets of rows and columns by integer location only
# .at selects a single scalar value in the DataFrame by label only

df_4.at[1,'estado']= 'NL'
print(df_4)

# Columns returned when indexing a DataFrame are views of the underlying data, not a copy.
# To obtain a copy, use the Series' copy method.


# NEW DATAFRAME
ser_nombre = Series(["María", "Lupe", "Omar", "Antonia", "Checo"])
ser_edad = Series([21, 20, 22, 19, 20])
ser_estado = Series(["Jalisco", "Michoacan", "Puebla", "Guanajuato", "Tabasco"])

# Creating Frame
frame = { 'Nombre': ser_nombre, 'Edad': ser_edad, 'Estado':ser_estado }
# Creating Dataframe
estudiantes_df = pd.DataFrame(frame)
print(estudiantes_df)

# Adding a new column
edad = [11, 9, 9, 8, 7]
estudiantes_df['Edad 2'] = edad
print(estudiantes_df)

# Drop rows from a Series or DataFrame:
estudiantes_df.drop(columns=['Edad 2'])
print(estudiantes_df)
estudiantes_df.drop(columns=['Edad 2'], inplace=True)
print(estudiantes_df)

# Select specified columns from a DataFrame:
print(estudiantes_df[['Nombre', 'Estado']])
print()

#iterate over a dataframe
for index, row in estudiantes_df.iterrows():
    print(type(row))

#iterate over a dataframe, column -> row
for index, row in estudiantes_df.iterrows():
    for column_name, value in row.iteritems():
        print(column_name)
        print(value)
        print()
        
# The iteritems() method generates an iterator object of the DataFrame, allowing us to iterate each column of the DataFrame. 
# Note: This method is the same as the items() method. Each iteration produces a label object and a column object. 
# The label is the column name.
