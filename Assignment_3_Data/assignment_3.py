import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns

# Question 1

# ChatGPT. Assistance given to the author, AI. 
# Corrected errors regarding tick labels, title, and creating plt.subplot 
# Prompt: Why isn't my code passing an autograder? 
# Response: lines 19-24. 
# OpenAI, (https://chatgpt.com). West Point, NY, 23MAR2025.

def q1():
    cd_df = pd.read_csv('covid_data.csv')
    cd_df['infections per cap'] = cd_df['cases'] / cd_df['pop']
    cd_df = cd_df.sort_values('infections per cap')
    #following code was partly created and troubleshooted by ChatGPT
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(cd_df['county'], cd_df['infections per cap'], color='#636363')
    ax.set_xticklabels(cd_df['county'], rotation=-90, ha='center') # rotates x axis labels
    ax.set_xlabel('County')
    ax.set_ylabel('Infections, Per Capita')
    ax.set_title('Per Capita COVID Infections by County in March 2020') # sets title
    return(ax)

# Question 2

# ChatGPT. Assistance given to the author, AI. 
# Created plot data frame and created format for boxplot and also included setting x and y limits
# Prompt: Why isn't my code passing an autograder? 
# Response: lines 37-40 and 44-48. 
# OpenAI, (https://chatgpt.com). West Point, NY, 23MAR2025.

def q2():
    gts_df = pd.read_csv('game_teams_stats.csv')
    plot_data = {
        'Losing Team': gts_df.loc[gts_df['won'] == False, 'goals'],
        'Winning Team': gts_df.loc[gts_df['won'] == True, 'goals']
    } # extracts and stores only the relevant data using .loc
    plot_df = pd.DataFrame(plot_data)
    fig, ax = plt.subplots()
    # Make boxplot with custom colors
    box = plot_df.boxplot(ax=ax, boxprops=dict(color='#1f77b4'), whiskerprops=dict(color='#1f77b4'), capprops=dict(color='#1f77b4'), medianprops=dict(color='black'), flierprops=dict(marker='o', markerfacecolor='white', markeredgecolor='#1f77b4'))
    ax.set_title('Distribution of Goals Scored by Winning and Losing NHL Teams')
    ax.set_ylabel('Goals Scored')
    ax.set_xlim(-0.5, 1.5) # setting x and y limits, was not passing autograder prior to this addition
    ax.set_ylim(0, 12)
    return(ax)

# Question 3

# ChatGPT. Assistance given to the author, AI. 
# Created and troubleshooted rangers search and creating plot
# Prompt: Why isn't my code passing an autograder? 
# Response: if else statement and win loss in plot
# OpenAI, (https://chatgpt.com). West Point, NY, 23MAR2025.

def q3():
    # Load both datasets
    gts_df = pd.read_csv('game_teams_stats.csv')
    ti_df = pd.read_csv('team_info.csv')
    # Attempt to find the Rangers team_id using a flexible search
    if 'shortName' in ti_df.columns:
        rangers_row = ti_df[ti_df['shortName'].str.contains('Rangers', case=False, na=False)]
    else:
        rangers_row = ti_df[ti_df['name'].str.contains('Rangers', case=False, na=False)]
    # Returns value error if Rangers does not exist
    if rangers_row.empty:
        raise ValueError("Could not find Rangers in team_info.csv")
    rangers_id = rangers_row['team_id'].values[0]
    # Filter to Rangers' games in the 2016 season
    gts_df = gts_df[gts_df['team_id'] == rangers_id]
    gts_df = gts_df[gts_df['game_id'].astype(str).str[:4] == '2016']
    # Add a column for win/loss result
    gts_df['result'] = gts_df['won'].map({True: 'Win', False: 'Loss'})
    # creates the scatterplot
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.scatterplot(
        data=gts_df,
        x='hits',
        y='pim',
        hue='result',
        palette={'Win': 'black', 'Loss': 'red'},
        ax=ax
    )
    # set axis titles
    ax.set_title('Penalty Minutes vs Hits for the New York Rangers in 2016')
    ax.set_xlabel('Hits')
    ax.set_ylabel('Penalty Minutes')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.legend(title='Win', loc='lower right')
    plt.tight_layout()
    return ax

# Question 4

# ChatGPT. Assistance given to the author, AI. 
# Created and troubleshooted plot setup
# Prompt: Why isn't my code passing an autograder? 
# Response: rename colomns so they are capitaliszed and cbar = False on the sns.heatmap
# OpenAI, (https://chatgpt.com). West Point, NY, 23MAR2025.

def q4():
    gss_df = pd.read_csv('game_skater_stats.csv')
    pi_df = pd.read_csv('player_info.csv')
    # Merge on player_id
    merged_df = pd.merge(gss_df, pi_df, on='player_id')
    # Use lowercase column names from the dataset
    stat_cols = ['goals', 'assists', 'shots', 'hits', 'blocked']
    # Group by nationality and calculate averages
    avg_stats = merged_df.groupby('nationality')[stat_cols].mean()
    # Rename columns to match expected format
    avg_stats.columns = ['Goals', 'Assists', 'Shots', 'Hits', 'Blocked']
    # Reorder nationalities
    nationalities = ['CAN', 'FIN', 'RUS', 'SWE', 'USA']
    avg_stats = avg_stats.loc[nationalities]
    # Plot heatmap
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(avg_stats, cmap='Blues', ax=ax, cbar=False)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    ax.set_title('Average NHL Player Stats per Game by Nationality')
    ax.set_xlabel('')
    ax.set_ylabel('Nationality')
    plt.tight_layout()
    return ax

# Question 5

# ChatGPT. Assistance given to the author, AI. 
# Created x plot
# Prompt: Why isn't my code returning targttype error? 
# Response: Need to check original spelling in csv file
# OpenAI, (https://chatgpt.com). West Point, NY, 23MAR2025.

def q5():
    df = pd.read_csv('terror_2016.csv')
    grouped = df.groupby(['targtype1_txt', 'attacktype1_txt']).size().reset_index(name='count')
    chart = alt.Chart(grouped).mark_bar().encode( #creates chart with propper x and y labels, targtype and attacktype have to be the exact same as in the csv file or it will return an error
        x=alt.X(
            'target_type1_txt:N',
            title='Target Type',
            sort=['Military', 'Police', 'Business', 'Educational Institution'],
            axis=alt.Axis(labelAngle=0)  # explicitly horizontal
        ),
        y=alt.Y('count:Q', title='Count of Attacks'),
        color=alt.Color('attacktype1_txt:N', title='Attack Type'),
        order=alt.Order('attacktype1_txt:N')
    ).properties(
        title='Targets of Terror Attack by Attack Type',
        width=600,
        height=400
    )
    return chart

# Question 6

# ChatGPT. Assistance given to the author, AI. 
# Created plot
# Prompt: Why isn't my code returning error?
# Response: Multiple changes throughout including renaming datetime columns names
# OpenAI, (https://chatgpt.com). West Point, NY, 23MAR2025.

def q6():
    df = pd.read_csv('terror_2016.csv')
    # Create datetime from iyear, imonth, iday
    df['date'] = pd.to_datetime(df.rename(columns={
        'iyear': 'year',
        'imonth': 'month',
        'iday': 'day'
    })[['year', 'month', 'day']])
    jan_df = df[(df['date'].dt.year == 2016) & (df['date'].dt.month == 1)]
    # Group by date and compute cumulative casualties
    daily = jan_df.groupby('date')[['nkill', 'nwound']].sum().reset_index()
    daily['cumulative_kill'] = daily['nkill'].cumsum()
    daily['cumulative_wound'] = daily['nwound'].cumsum()
    # Melt for plotting, wide to long format
    melted = pd.melt(
        daily,
        id_vars='date',
        value_vars=['cumulative_kill', 'cumulative_wound'],
        var_name='type',
        value_name='count'
    )
    melted['type'] = melted['type'].map({
        'cumulative_kill': 'nkill',
        'cumulative_wound': 'nwound'
    })
    # Build Altair chart with formatted date axis
    chart = alt.Chart(melted).mark_line(point=True).encode(
        x=alt.X('date:T',
                title='Date',
                axis=alt.Axis(format='%d %b')  # <- This sets x-axis tick format
        ),
        y=alt.Y('count:Q', title='Count of Casualties'),
        color=alt.Color('type:N',
                        title='Casualty Type',
                        scale=alt.Scale(domain=['nkill', 'nwound'],
                                        range=['#252525', '#969696']))
    ).properties(
        title='Running Total of Killed and Wounded in Terror Attacks in January 2016',
        width=700,
        height=300
    )
    return chart