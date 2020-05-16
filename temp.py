import pandas as pd
data_df = pd.read_csv("Resources/cities.csv")
#data_df.reset_index(drop=True, inplace=True)
data_df.drop('0', axis=1)

x = data_df.to_html()

print(x)
