import os
os.chdir('C:/Users/william.monahan/OneDrive - West Point/SE370/Assignment_2_Data')

import json
import pandas as pd

def clean_senate_names():

    with open("senate_data.json", "r") as file:
        data = json.load(file)

    df = pd.DataFrame({
        "first_name": [item["person"]["firstname"] for item in data["objects"]],
        "last_name": [item["person"]["lastname"] for item in data["objects"]],
        "state": [item["state"] for item in data["objects"]],
        "party": [item["party"] for item in data["objects"]]
    })

    df.to_csv("senate_names.csv", index=False, columns=["first_name", "last_name", "state", "party"])

    df_saved = pd.read_csv("senate_names.csv")

    print(df_saved)

clean_senate_names()