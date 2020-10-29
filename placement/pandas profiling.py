import pandas as pd 
from pandas_profiling import ProfileReport

df=pd.read_csv('placement.csv')

report=ProfileReport(df,title='pandas profiling report')
report.to_file('placement.html')