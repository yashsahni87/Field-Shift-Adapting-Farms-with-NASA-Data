import streamlit as st
import requests
import pandas as pd
from datetime import date, timedelta

st.set_page_config(
    page_title="Field Shift",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Field Shift")
st.subheader("Farm Crop Rotation Decision Support")

st.write(
    "Explore crop-rotation strategies using NASA Earth observations "
    "and local farm information."
)

# -----------------------------
# FARMER INPUTS
# -----------------------------
st.sidebar.header("Farm Information")

lat = st.sidebar.number_input(
    "Latitude",
    value=28.6139,
    min_value=-90.0,
    max_value=90.0
)

lon = st.sidebar.number_input(
    "Longitude",
    value=77.2090,
    min_value=-180.0,
    max_value=180.0
)

current_crop = st.sidebar.selectbox(
    "Current Crop",
    ["Wheat", "Rice", "Maize", "Soybean", "Cotton", "Other"]
)

priority = st.sidebar.selectbox(
    "Main Priority",
    [
        "Water efficiency",
        "Drought resilience",
        "Soil health",
        "Yield stability"
    ]
)

# -----------------------------
# NASA POWER API
# -----------------------------
def get_nasa_power(lat, lon):

    start = (date.today() - timedelta(days=30)).strftime("%Y%m%d")
    end = date.today().strftime("%Y%m%d")

    url = "https://power.larc.nasa.gov/api/temporal/daily/point"

    params = {
        "parameters": "T2M,PRECTOTCORR,RH2M,ALLSKY_SFC_SW_DWN",
        "community": "AG",
        "longitude": lon,
        "latitude": lat,
        "start": start,
        "end": end,
        "format": "JSON"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    values = data["properties"]["parameter"]

    df = pd.DataFrame(values)
    df.index = pd.to_datetime(df.index)

    return df


# -----------------------------
# NASA DATA
# -----------------------------
if st.button("Analyze Field"):

    with st.spinner("Fetching NASA climate data..."):

        try:
            df = get_nasa_power(lat, lon)

            st.success("NASA POWER data loaded successfully.")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Avg Temperature",
                f"{df['T2M'].mean():.1f} °C"
            )

            col2.metric(
                "Rainfall",
                f"{df['PRECTOTCORR'].sum():.1f} mm"
            )

            col3.metric(
                "Avg Humidity",
                f"{df['RH2M'].mean():.1f}%"
            )

            col4.metric(
                "Solar Radiation",
                f"{df['ALLSKY_SFC_SW_DWN'].mean():.1f}"
            )

            st.subheader("NASA POWER Climate Data")

            st.line_chart(
                df[["T2M", "PRECTOTCORR", "RH2M"]]
            )

            # -----------------------------
            # SIMPLE ROTATION SCORING
            # -----------------------------
            st.subheader("🌾 Rotation Suggestions")

            rainfall = df["PRECTOTCORR"].sum()
            temperature = df["T2M"].mean()

            crops = {
                "Millet": {
                    "water": 5,
                    "drought": 9,
                    "soil": 8
                },
                "Maize": {
                    "water": 7,
                    "drought": 6,
                    "soil": 6
                },
                "Soybean": {
                    "water": 7,
                    "drought": 5,
                    "soil": 8
                },
                "Wheat": {
                    "water": 6,
                    "drought": 6,
                    "soil": 7
                }
            }

            results = []

            for crop, score in crops.items():

                if priority == "Water efficiency":
                    final_score = score["water"]

                elif priority == "Drought resilience":
                    final_score = score["drought"]

                elif priority == "Soil health":
                    final_score = score["soil"]

                else:
                    final_score = (
                        score["water"]
                        + score["drought"]
                        + score["soil"]
                    ) / 3

                # Environmental adjustment
                if rainfall < 100:
                    final_score += score["drought"] * 0.2

                if temperature > 30:
                    final_score += score["drought"] * 0.1

                results.append({
                    "Crop": crop,
                    "Score": round(final_score, 2)
                })

            results = pd.DataFrame(results)
            results = results.sort_values(
                "Score",
                ascending=False
            )

            st.dataframe(
                results,
                use_container_width=True,
                hide_index=True
            )

            best_crop = results.iloc[0]["Crop"]

            st.success(
                f"Recommended rotation option: **{best_crop}**"
            )

            st.info(
                "This is a prototype decision-support score, "
                "not an agronomic prescription."
            )

        except Exception as e:
            st.error(f"NASA data request failed: {e}")

else:
    st.info("Enter your farm information and click **Analyze Field**.")
