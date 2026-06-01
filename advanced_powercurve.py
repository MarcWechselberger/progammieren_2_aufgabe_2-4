import numpy as np
import pandas as pd
import plotly.express as px

def read_data(filepath):
    df = pd.read_csv(filepath)
    return df

def add_time(df):
    df["time_seconds"] = np.arange(len(df))
    return df

def find_best_effort(df, window_size, resolution=1):
    df2 = df["PowerOriginal"].rolling(window_size*resolution).mean()
    return df2.max()

def create_pc_df(df, window_list):
    list_a = []
    for window_size in window_list:
        list_a.append(find_best_effort(df, window_size))
    pc_df = pd.DataFrame(list_a, columns=["Max. Avg. Power"])
    pc_df["Intervall"] = window_list
    return pc_df


def plot_pc(pc_df):
    fig = px.line(pc_df, x= pc_df["Intervall"], y= pc_df["Max. Avg. Power"])
    return fig


def create_windows(df):
    window_list = np.arange(len(df))
    return window_list


if __name__ == "__main__":
    df_test = read_data("data/activities/activity.csv")
    df_test = add_time(df_test)
    #print(df_test.head())
    #window_list = [10, 20, 30, 60, 300, 600, 1200, 1800, 3600, 7200]
    #window_list = [10, 20, 30, 40, 60, 90, 120, 240, 300, 400, 450, 500, 550, 600, 650, 700, 800, 900, 1000, 1200]
    window_list = create_windows(df_test)
    pcdf2 = create_pc_df(df_test, window_list)
    #print(pcdf2.head())
    fig1 = plot_pc(pcdf2)
    fig1.update_layout(
    xaxis_title="Intervalls",
    yaxis_title="Max. avg. Power in W"
    )
    fig1.show()