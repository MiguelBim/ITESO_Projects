from tabulate import tabulate
import pandas as pd

df = pd.DataFrame({'Nombre' : ["María", "Lupe", "Omar", "Antonia", "Checo"],
                   'Edad' : [21, 20, 22, 19, 20],
                   'Código' : ["c23","c24","c25","c26","c27",]})

print(tabulate(df, headers='keys', tablefmt='psql'))