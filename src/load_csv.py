# IMPORTING MODULE

import pandas as pd

# SETTING DATASET 

# url = "/Users/.../data/MUSIC - DATASET - Sheet1 (1).csv"

url = "/Users/.../data/onlinefoods.csv"

def creating_datframe(url = url):
      global df
      df = pd.read_csv(url)

      # Get the header to be in lowercase; if already in lower case do nothing
      df.columns = [col.lower() if col != col.lower() else col for col in df.columns]

      with open(url, "w") as file:
            df.to_csv(file, header=True,index = False)
      
      # df = df.drop(["spotify_url", "youtube_url"], axis = 1) # Removing URLs
