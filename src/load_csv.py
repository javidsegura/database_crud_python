# IMPORTING MODULE

import pandas as pd

# SETTING DATASET 

url = "/Users/javierdominguezsegura/Programming/Python/Side projects/Database Management System/data/MUSIC - DATASET - Sheet1 (1).csv"

def creating_datframe(url = url):
      global df
      df = pd.read_csv(url)
      # df = df.drop(["spotify_url", "youtube_url"], axis = 1) # Removing URLs

