data = {

    "Name":['Amit',"Ram","Hari"],
    "Age":[20,21,22],
    "Branch":["CS","EEE","ECE"]

}

import pandas as pd

df = pd.DataFrame(data)

df.to_csv("data/sample_data.csv")

