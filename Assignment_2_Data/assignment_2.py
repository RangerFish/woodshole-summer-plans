
import os
import json
import pandas as pd

# Question 1

# ChatGPT. Assistance given to the author, AI. 
# Helped return correct csv file. Could not get it to pass the autograder using print 
# Prompt: Why isn't my code passing an autograder? 
# Response: (wanted me to use) lines 31-34. 
# OpenAI, (https://chatgpt.com). West Point, NY, 22FEB2025.

def clean_senate_names():

    file_path = os.path.join(os.getcwd(), "senate_data.json")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: senate_data.json not found.")
        return

    df = pd.DataFrame({
        "first_name": [item["person"]["firstname"] for item in data["objects"]],
        "last_name": [item["person"]["lastname"] for item in data["objects"]],
        "state": [item["state"] for item in data["objects"]],
        "party": [item["party"] for item in data["objects"]]
    })

    output_path = os.path.join(os.getcwd(), "senate_names.csv")
    df.to_csv(output_path, index=False)

    return output_path

clean_senate_names()


# Question 2

# ChatGPT. Assistance given to the author, AI. 
# Helped make modifications to code in Question 1.
# Prompt: How change N/A to no_twitter?
# Response: Suggested using .get() function
# OpenAI, (https://chatgpt.com). West Point, NY, 22FEB2025.

def clean_senate_social():

    file_path = os.path.join(os.getcwd(), "senate_data.json")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: senate_data.json not found.")
        return

    df = pd.DataFrame({
        "first_name": [item["person"]["firstname"] for item in data["objects"]],
        "last_name": [item["person"]["lastname"] for item in data["objects"]],
        "twitterid": [item["person"].get("twitterid", "no_twitter") for item in data["objects"]],
        "office_address": [item["extra"].get("address", "N/A") for item in data["objects"]],
        "senator_rank": [item.get("senator_rank", "N/A") for item in data["objects"]]
    })

    output_path = os.path.join(os.getcwd(), "senate_names.csv")
    df.to_csv(output_path, index=False)

    return output_path

clean_senate_social()


# Question 3

# ChatGPT. Assistance given to the author, AI. 
# Helped with various code modifcations.
# Prompt: How to filter out rows?
# Response: line 101. 
# OpenAI, (https://chatgpt.com). West Point, NY, 22FEB2025.

def clean_ev_data():

    df = pd.read_csv("ev_data.csv")

    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    df = df.drop(columns=["co2_rating_", "smog_rating"])

    df["range_(km)"] = df["range_(km)"] * 0.6213

    df.rename(columns={"range_(km)": "range_mi"}, inplace=True)

    df.rename(columns={"recharge_time_(h)": "recharge_time"}, inplace=True)

    df = df.drop(columns=["motor_(kw)", "transmission", "fuel_type", "city_(kwh/100_km)", "highway_(kwh/100_km)", "combined_(kwh/100_km)", "city_(le/100_km)", "highway_(le/100_km)", "combined_(le/100_km)", "co2_emissions_(g/km)"])
    
    df = df[["make", "model", "model_year", "range_mi", "recharge_time", "vehicle_class"]]
    
    df = df[~df["make"].isin(["smart EQ", "Subaru"])]

    df.to_csv("ev_cleaned.csv", index=False)

clean_ev_data()


# Question 4

# ChatGPT. Assistance given to the author, AI. 
# Helped with various code modifcations.
# Prompt: How to round a number to the nearest whole number without decimals?
# Response: .round()
# OpenAI, (https://chatgpt.com). West Point, NY, 22FEB2025.

def ev_efficiency():

    df = pd.read_csv("ev_cleaned.csv")

    df["efficiency"] = (df["range_mi"] / df["recharge_time"]).round()

    avg_efficiency_df = df.groupby("vehicle_class", as_index=False)["efficiency"].mean().round()

    avg_efficiency_df.rename(columns={"efficiency": "avg_efficiency"}, inplace=True)

    avg_efficiency_df.to_csv("ev_efficiency.csv", index=False)

ev_efficiency()

# Question 5

# ChatGPT. Assistance given to the author, AI. 
# Helped with various code modifcations.
# Prompt: How to combine two dataframes?
# Response: .merge()
# OpenAI, (https://chatgpt.com). West Point, NY, 23FEB2025.

def ev_mean_range():

    df = pd.read_csv("ev_cleaned.csv")

    range_stats = df.groupby("make")["range_mi"].agg(avg_range="mean", min_range="min", max_range="max")
    
    unique_models = df.groupby("make")["model"].nunique().rename("num_models")

    final_df = pd.merge(range_stats, unique_models, on="make").reset_index()

    final_df.to_csv("ev_mean_range.csv", index=False)

ev_mean_range()


# Question 6

# ChatGPT. Assistance given to the author, AI. 
# Helped with various code modifcations.
# Prompt: How to merge two dataframes and get them to match?
# Response: lines 172-177
# OpenAI, (https://chatgpt.com). West Point, NY, 23FEB2025.

def ev_mean_merge():

    df = pd.read_csv("ev_mean_range.csv")

    with open("manufacturer_info.json", "r") as file:
        info = json.load(file)

    df_m = pd.DataFrame(info)

    df_m.columns = [col.lower().replace(" ", "_") for col in df_m.columns]

    df_merged = pd.merge(df, df_m, on="make", how="left")

    df_merged = df_merged.replace(r'^\s*$', None, regex=True)
    df_merged = df_merged.dropna()

    df_merged["make"] = df_merged["make"].str.title()

    correction_dict = {
        "Bmw": "BMW",
        "Gmc": "GMC",
        "Mini": "MINI",
        "Fiat": "FIAT",
        "Vinfast": "VinFast",
        "Smart": "smart"
    }
    
    df_merged["make"] = df_merged["make"].replace(correction_dict)

    df_merged.to_csv("ev_mean_merge.csv", index=False)

ev_mean_merge()


# Question 7

# ChatGPT. Assistance given to the author, AI. 
# Helped with various code modifcations.
# Prompt: How to reshape data?
# Response: lines 216-220
# OpenAI, (https://chatgpt.com). West Point, NY, 23FEB2025.

def ev_category_analysis():

    df = pd.read_csv("ev_cleaned.csv")

    vehicle_classes = ["Compact", "Full-size", "Mid-size"]

    df_filtered = df[df["vehicle_class"].isin(vehicle_classes)]

    df_avg_recharge = df.groupby(["vehicle_class", "model_year"])["recharge_time"].mean().reset_index()

    df_pivot = df_filtered.pivot_table(
        index="model_year", 
        columns="vehicle_class", 
        values="recharge_time", 
        aggfunc="mean"
    )

    df_pivot.to_csv("ev_category_analysis.csv", index=True)

ev_category_analysis()