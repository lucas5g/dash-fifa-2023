import streamlit as st

st.set_page_config(page_title="Players", layout="wide")

df = st.session_state["data"]

clubs = df["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubs)

df_filtered = df[(df["Club"] == club)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = [
    "Age",
    "Photo",
    "Flag",
    "Overall",
    "Value(£)",
    "Wage(£)",
    "Joined",
    "Height(cm.)",
    "Weight(lbs.)",
    "Contract Valid Until",
    "Release Clause(£)",
]

st.dataframe(
    df_filtered[columns],
    column_config={
        "Overall": st.column_config.ProgressColumn(
            "Overall", format="%d", min_value=0, max_value=100
        ),
        "Wage(£)": st._column_config.ProgressColumn(
            "Weekly Wage",
            format="£%f",
            min_value=0,
            max_value=df_filtered["Wage(£)"].max(),
        ),
        "Photo":st.column_config.ImageColumn(),
        "Flag": st.column_config.ImageColumn("Country")
    },
)
