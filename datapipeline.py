import pandas as pd 
import numpy as np
dataframe = pd.DataFrame(
    np.random.randint(1, 100, size=(10, 4)),
    columns=["A", "B", "C", "D"]
)   

print(dataframe.head())