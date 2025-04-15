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

    return df_saved

clean_senate_names()

#Question 2

def clean_senate_social():

    file_path_2 = os.path.join(os.getcwd(), "senate_data.json")

    try:
        with open(file_path_2, "r") as file_2:
            data_2 = json.load(file_2)
    except FileNotFoundError:
        print("Error: senate_data.json not found.")
        return

    df_2 = pd.DataFrame({
        "first_name": [item["person"]["firstname"] for item in data["objects"]],
        "last_name": [item["person"]["lastname"] for item in data["objects"]],
        "twitterid": [item["person"].get("twitterid", "no_twitter") for item in data["objects"]],
        "office_address": [item["extra"].get("address", "N/A") for item in data["objects"]],
        "senator_rank": [item.get("senator_rank", "N/A") for item in data["objects"]]
    })

    output_path_2 = os.path.join(os.getcwd(), "senate_social.csv")
    df_2.to_csv(output_path_2, index=False)

    return output_path_2

clean_senate_social()