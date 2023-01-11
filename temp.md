# Code

```
import pandas as pd
df = pd.read_clipboard() #Copied the MORTGAGE30US weekly data to clipboard
df['DATE']=pd.to_datetime(df['DATE']) #Converted 'DATE' column to pandas datetime
df['DATE'] = pd.to_datetime(df['DATE']).dt.to_period('M') #Stripped out the day from date time column to get monthly granularity
df =df.groupby(['DATE']).mean() #Grouped by mean
df.to_clipboard(excel=True) #Copied to clipboard to paste in excel
```