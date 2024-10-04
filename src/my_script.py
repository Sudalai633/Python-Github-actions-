
import openpyxl

import pandas as pd

url = "http://www.fdic.gov/bank/individual/failed/banklist.html"  
dfs = pd.read_html(url)

