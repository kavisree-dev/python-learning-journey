#data cleaning pipeline
import pandas as pd
import numpy as np
#first need to create df
df=pd.DataFrame({
    'id':[1,2,3],'temp':[23.9,45.6,67.5],
    'age':[np.nan,23,22],'salary':[67000,56000,78000]
})

#second function define
def clean_data(df, *drop_cols,**fill_values):
    df=df.drop(columns=list(drop_cols))
    for col,val in fill_values.items():
        df[col]=df[col].fillna(val)
    return df

#third call function   
df=clean_data(df,"id","temp",age=21,salary=45000)
print(df)
#df---dataframe -data table
#id,temp --- tuple ---drop_cols
#age=21,salary=45000 ---dict ----fill values

