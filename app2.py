import pandas as pd
import os
df=pd.DataFrame({"gender":["Male"],"class":[6]})


print(df)
k=df.to_csv(index=False)
print(k)


