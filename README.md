# 🌍 Country Dashboard

[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Visualization-Plotly-3F4F75?logo=plotly)](https://plotly.com/)

An interactive country analytics platform focused on large-scale **data ingestion**, **data preprocessing**, **section-wise aggregation**, and **interactive visualizations**.

The project transforms raw country-level datasets into structured dashboard-ready artifacts through a modular preprocessing pipeline and visualizes them using Streamlit and Plotly.

---

# 🚀 Features

## 📥 Data Ingestion

* API-driven dataset ingestion
* Raw dataset storage
* Cached responses
* Metadata generation
* Config-based pipeline architecture

---

# 🧹 Data Processing & Preprocessing

The main focus of this project is the preprocessing and processing pipeline.

### Processing Features

* Missing value handling
* Country standardization
* Year normalization
* Dataset cleaning
* Metric preprocessing
* Registry-driven dataset processing
* Reusable processing utilities
* Section-wise aggregation pipeline

### Processed Sections

* 💰 Economy
* 👥 Demographics
* 🌐 Trade
* 💻 Technology
* 🌱 Environment
* 🏭 Industry
* 🛡️ Military

---

# ⚡ Data Pipeline Flow

```text id="wxx8h0"
🌍 External APIs / Datasets
              │
              ▼
📥 Data Ingestion Pipeline
              │
              ▼
📂 Raw Dataset Artifacts
              │
              ▼
🧹 Dataset Processing Pipeline
              │
              ▼
🏛️ Section-wise Aggregation
              │
              ▼
📦 Processed CSV Artifacts
              │
              ▼
📑 Registry-based Dataset Loading
              │
              ▼
🌍 Interactive Streamlit Dashboard
```

---

# 🌍 Dashboard Features

## 📊 Interactive Analytics

* Time-series visualizations
* Interactive Plotly charts
* Unified hover analytics
* Dynamic filtering system
* Responsive dashboard layout

---

## 🔄 Compare Mode

Compare up to 3 countries simultaneously with:

* Shared filters
* Synchronized visualizations
* Comparative analytics
* Unified hover interactions

---

## 📌 KPI Cards

Dynamic KPI cards with:

* Formatted numerical scaling
* Trend indicators
* Delta calculations
* Semantic color indicators

---

## 🌎 Interactive World Map

* Choropleth world visualization
* ISO3 country mapping
* Dynamic metric selection
* Year-based filtering
* Interactive hover analytics

---

# 🧩 Dashboard Sections

| Section         | Metrics                                  |
| --------------- | ---------------------------------------- |
| 💰 Economy      | GDP, Inflation, Unemployment, GDP Growth |
| 👥 Demographics | Population, Birth Rate, Life Expectancy  |
| 🌐 Trade        | Imports, Exports, Trade Balance          |
| 💻 Technology   | Internet & Connectivity Metrics          |
| 🌱 Environment  | Environmental Indicators                 |
| 🏭 Industry     | Industrial Metrics                       |
| 🛡️ Military    | Defense & Military Spending              |

---

# 🛠️ Tech Stack

### Data Engineering

* Python
* Pandas
* NumPy

### Visualization

* Streamlit
* Plotly

### Architecture

* Modular artifact pipeline
* Registry-driven processing
* Config-based workflow

---

# 🚀 Run Locally

## Clone Repository

```bash id="3clnh5"
git clone https://github.com/aadityaa-raai/Country-Dashboard
cd Country-Dashboard
```

## Install Dependencies

```bash id="o67l2u"
pip install -r requirements.txt
```

## Run Dashboard

```bash id="9x1brw"
streamlit run Dashboard/app.py
```

---

# 👨‍💻 Author

Aditya Rai

---

# ⭐ Support

If you liked this project, consider giving it a star ⭐
