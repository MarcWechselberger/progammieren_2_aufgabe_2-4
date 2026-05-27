import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
from read_pandas import read_my_activity
from read_pandas import plot_hr_zone
from read_pandas import plot_pwr
from read_pandas import plot_hr_pwr
from read_pandas import add_hr_zones
from read_pandas import calculate_statistics


# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)

with tab2:
    st.header("Power-Data")

    hrmax = st.slider("Max. HR", 120, 220, 195)
    st.write("Selected max. heart rate is ", hrmax)

    df2 = read_my_activity()
    add_hr_zones(df2, hrmax)
    hrp = plot_hr_zone(df2)
    pwr = plot_pwr(df2)
    hrpwr = plot_hr_pwr(df2)
    
    tab3, tab4, tab5 = st.tabs(["Heart Rate", "Power", "Combined"])
    with tab3:
        st.plotly_chart(hrp)
    with tab4:
        st.plotly_chart(pwr)
    with tab5:
        st.plotly_chart(hrpwr)
    st.divider()
    st.dataframe(calculate_statistics(df2))
