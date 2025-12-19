import pandas as pd
df=pd.read_csv("C:\\Users\\STUDENT\\Desktop\\NewCompanyDetails.csv")
df=df.drop_duplicates()
df=df.dropna()
df['revenue']= df['revenue'].replace(r'[^0-9]','',regex=True).astype(int)
df['total workers']= df['workers']+df['previous_workers']
df.to_csv("newdetails.csv")
print(df)

























