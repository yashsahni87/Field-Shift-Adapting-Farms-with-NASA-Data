# 🌱 Field Shift — Adapting Farms with NASA Data

A decision-support prototype that helps farmers explore crop-rotation strategies using NASA Earth observation and climate data.

## 🚀 Overview

Farmers face changing temperatures, rainfall patterns, water availability, extreme weather, and soil-health challenges. **Field Shift** combines environmental data with farmer priorities to help compare potential crop-rotation options.

The project currently uses **NASA POWER** climate data and is designed to be extended with datasets such as SMAP, GPM/IMERG, and Landsat.

## ✨ Features

- 📍 Select a farm location using latitude and longitude
- 🌡️ Retrieve recent NASA POWER climate data
- 🌧️ Analyze rainfall conditions
- 💧 Consider water-efficiency and drought-resilience priorities
- 🌱 Compare potential rotation crops
- 📊 Display environmental indicators and crop scores
- 💡 Provide an easy-to-understand rotation recommendation

## 🛰️ Data Sources

### NASA POWER

Used for:

- Temperature
- Precipitation
- Relative humidity
- Solar radiation

Official source:

https://power.larc.nasa.gov/

### Planned / Extendable NASA Sources

- **SMAP** — soil moisture and drought-related indicators
- **GPM / IMERG** — precipitation and rainfall patterns
- **Landsat** — vegetation indices and crop/vegetation stress

The challenge resources also identify these datasets as useful for evaluating agricultural conditions and crop-rotation strategies.

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Requests
- NASA POWER API

## 📂 Project Structure

```text
field-shift/
│
├── app.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd field-shift
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
streamlit run app.py
```

The application will open in your browser.

## 📦 requirements.txt

```text
streamlit
requests
pandas
```

## 🧠 How It Works

```text
Farm Location
      ↓
NASA POWER API
      ↓
Temperature / Rainfall / Humidity / Radiation
      ↓
Environmental Analysis
      ↓
Crop Rotation Scoring
      ↓
Recommended Rotation
```

The prototype converts environmental observations and farmer-selected priorities into a comparative crop score.

## ⚠️ Current Limitations

This is a **prototype decision-support tool**, not a professional agronomic prescription.

The current version uses simplified crop-scoring rules. The next version should replace these illustrative scores with a more scientifically grounded model using:

- SMAP soil-moisture information
- GPM/IMERG precipitation data
- Landsat vegetation indicators
- Local soil characteristics
- Crop water requirements
- Historical climate conditions
- Farmer-specific constraints and priorities

## 🔮 Future Improvements

- Integrate real SMAP soil-moisture data
- Add GPM/IMERG rainfall analysis
- Calculate NDVI from Landsat imagery
- Add field-level soil information
- Add historical climate trends
- Support multiple fields
- Display risk levels for each rotation
- Add map-based field selection
- Include crop-market considerations
- Improve the recommendation model with agronomic research

## 🌍 NASA Space Apps Challenge

This project was developed for the **NASA Space Apps Challenge** challenge:

**Field Shift: Adapting Farms with NASA Data**

The challenge asks participants to create a decision-support tool using NASA Earth observations together with local soil information, crop characteristics, and farmer priorities to explore crop-rotation strategies.

## 📜 License

This project is intended for educational and hackathon purposes.

---

**Field Shift — Turning Earth observation data into practical farming insights.**
