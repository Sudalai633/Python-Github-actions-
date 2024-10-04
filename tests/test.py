import openpyxl

import pandas as pd

url = "http://www.fdic.gov/bank/individual/failed/banklist.html"  
dfs = pd.read_html(url)
print(dfs.head(10))
print(dfs.descirbe())
print(dfs.info())


