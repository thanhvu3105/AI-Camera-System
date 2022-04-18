import pandas as pd
import numpy as np
import os.path

f_name = "train.csv"

def write(name, data):
  
    if os.path.isfile(f_name):
        df = pd.read_csv(f_name, index_col = 0)
        latest = pd.DataFrame(data, columns = map(str, range(50176)))
        latest["name"] = name
        df = pd.concat((df, latest), ignore_index = True, sort = False)
  
    else:
      
        df = pd.DataFrame(data, columns = map(str, range(50176)))
        df["name"] = name
  
    df.to_csv(f_name)