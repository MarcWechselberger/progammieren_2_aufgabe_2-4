# Paket für Bearbeitung von Tabellen
import pandas as pd
import numpy as np

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df

def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig

####

def read_my_activity():
    df = pd.read_csv("data/activities/activity.csv")
    N = len(df["PowerOriginal"])
    df["time_seconds"] = np.arange(N)
    return df

def make_power_hr_plot(df):
    #erster Versuch mit 2 y-Werten
    fig = px.line(df["HeartRate"], x= df["time_seconds"], y=[df["HeartRate"], df["PowerOriginal"]])
    return fig


def plot_hr_zone(
    df,
    x_col="time_seconds",
    y_col="HeartRate",
    zone_cols=("Zone1", "Zone2", "Zone3", "Zone4", "Zone5"),
):
    df = df.copy()

    df["Zone"] = (
        df[list(zone_cols)]
        .idxmax(axis=1)
        .where(df[list(zone_cols)].any(axis=1), "Below")
    )

    farben = {
        "Zone1": "blue",
        "Zone2": "green",
        "Zone3": "yellow",
        "Zone4": "orange",
        "Zone5": "red",
        "Below": "gray",
    }

    fig = go.Figure()

    # fortlaufende Abschnitte gleicher Zone erkennen
    df["Abschnitt"] = (df["Zone"] != df["Zone"].shift()).cumsum()

    for _, abschnitt_df in df.groupby("Abschnitt"):
        zone = abschnitt_df["Zone"].iloc[0]

        fig.add_trace(go.Scatter(
            x=abschnitt_df[x_col],
            y=abschnitt_df[y_col],
            mode="lines",
            name=zone,
            line=dict(
                color=farben.get(zone, "black"),
                width=3
            ),
            showlegend=zone not in [
                trace.name for trace in fig.data
            ]
        ))

    fig.update_layout(
        xaxis_title="Time in Seconds",
        yaxis_title="Heart Rate",
        legend_title="HR-Zone"
    )

    return fig

# Erster Versuch Powerplot:
def make_pwr_plot(df):
    fig = px.line(df["PowerOriginal"])#, x= df["time_seconds"], y= df["PowerOriginal"])
    return fig

def plot_pwr(
    df,
    x_col="time_seconds",
    y_col="PowerOriginal"
):
    """
    Erstellt einen Plot Leistung über Zeit.

    Parameter:
    ----------
    df : pandas.DataFrame
        Eingabedaten
    x_col : str
        Spalte für Zeit
    y_col : str
        Spalte für Leistung

    Rückgabe:
    ----------
    plotly.graph_objects.Figure
    """

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df[x_col],
        y=df[y_col],
        mode="lines",
        name="Leistung"
    ))

    fig.update_layout(
        title="Power over Time",
        xaxis_title="Time in seconds",
        yaxis_title="Power in Watt",
        template="plotly_white"
    )

    return fig

def add_hr_zones(df, hr_max):
    
    z1_low = hr_max * 0.5
    z2_low = hr_max * 0.6
    z3_low = hr_max * 0.7
    z4_low = hr_max * 0.8
    z5_low = hr_max * 0.9

    df["Zone1"] = (df["HeartRate"] >= z1_low) & (df["HeartRate"] < z2_low)
    df["Zone2"] = (df["HeartRate"] >= z2_low) & (df["HeartRate"] < z3_low)
    df["Zone3"] = (df["HeartRate"] >= z3_low) & (df["HeartRate"] < z4_low)
    df["Zone4"] = (df["HeartRate"] >= z4_low) & (df["HeartRate"] < z5_low)
    df["Zone5"] = df["HeartRate"] >= z5_low

    return df

def calculate_statistics(df):
    
    zonen = ["Zone1", "Zone2", "Zone3", "Zone4", "Zone5"]
    df_stats = pd.DataFrame({
    "Time in s per Zone": [
        df[z].sum() for z in zonen
    ],
    "Average Power in W per Zone": [
        df.loc[df[z], "PowerOriginal"].mean() for z in zonen
    ]
    }, index=zonen)

    return df_stats

def plot_hr_pwr(
    df,
    x_col="time_seconds",
    hf_col="HeartRate",
    power_col="PowerOriginal"
):
    """
    Erstellt einen Plot mit:
    - Herzfrequenz auf linker Y-Achse
    - Leistung auf rechter Y-Achse
    """

    fig = make_subplots(
        specs=[[{"secondary_y": True}]]
    )

    # Herzfrequenz (linke Achse)
    fig.add_trace(
        go.Scatter(
            x=df[x_col],
            y=df[hf_col],
            mode="lines",
            name="Heart Rate"
        ),
        secondary_y=False
    )

    # Leistung (rechte Achse)
    fig.add_trace(
        go.Scatter(
            x=df[x_col],
            y=df[power_col],
            mode="lines",
            name="Power"
        ),
        secondary_y=True
    )

    # Achsenbeschriftungen
    fig.update_xaxes(
        title_text="Time in Seconds"
    )

    fig.update_yaxes(
        title_text="Heartrate in bpm",
        secondary_y=False
    )

    fig.update_yaxes(
        title_text="Power in Watt",
        secondary_y=True
    )

    fig.update_layout(
        title="Heart Rate and Power combined",
        template="plotly_white",
        hovermode="x unified"
    )

    return fig


if __name__ == "__main__":
    activity_df = read_my_activity()

    #print(activity_df)\
    
    my_fig = make_power_hr_plot(activity_df)

    #my_fig.show()

    add_hr_zones(activity_df, 195)

    print(calculate_statistics(activity_df))