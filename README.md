# 🌍 Country Intelligence Dashboard

[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Visualization-Plotly-3F4F75?logo=plotly)](https://plotly.com/)

## 🚀 Live Demo

👉 https://your-streamlit-app-url.streamlit.app

---

# 📌 Project Overview

Country Intelligence Dashboard is a modular end-to-end data analytics platform designed for large-scale country-level data ingestion, preprocessing, transformation, and interactive visualization.

The project was built with a strong focus on:

* Data Engineering
* Data Preprocessing
* Scalable Architecture
* Modular Pipelines
* Interactive Analytics
* Dashboard Engineering

Unlike traditional dashboards, this project implements a complete data pipeline architecture including ingestion, preprocessing, section aggregation, metadata management, artifact handling, and dynamic visualization rendering.

---

# 🏗️ System Architecture

The project follows a preprocessing-first modular pipeline architecture.

```text
Raw APIs / Datasets
        ↓
Data Ingestion Pipeline
        ↓
Raw Artifacts Storage
        ↓
Dataset Processing Pipeline
        ↓
Preprocessing & Cleaning
        ↓
Section Aggregation Pipeline
        ↓
Processed Artifacts
        ↓
Data Registry System
        ↓
Visualization Layer
        ↓
Interactive Dashboard
```

---

# ⚙️ Core Engineering Components

## 1️⃣ Configuration Management

Centralized configuration system using:

* `config.yaml`
* Entity config classes
* Artifact configuration classes

This architecture allows:

* scalable path management
* modular pipeline control
* reproducible workflows

---

## 2️⃣ Artifact-Based Pipeline Architecture

The project uses a structured artifact pipeline:

```text
artifacts/
│
├── data_ingestion/
│
├── data_processing/
│
├── section_processing/
│
└── data/
```

Each stage generates reusable artifacts for downstream pipeline stages.

---

## 3️⃣ Data Ingestion Pipeline

The ingestion layer dynamically fetches country-level indicators from external sources.

### Features

* API-based ingestion
* Dataset caching
* Metadata generation
* Registry-driven ingestion
* Modular source handling

---

## 4️⃣ Dataset Processing Pipeline

The processing layer performs:

* missing value handling
* schema standardization
* year normalization
* country cleaning
* preprocessing
* metric transformations

Each dataset is processed independently before aggregation.

---

## 5️⃣ Section Aggregation Pipeline

Processed datasets are merged into domain-specific section datasets:

* Economy
* Demographics
* Trade
* Technology
* Environment
* Industry
* Military

The section processor dynamically merges datasets using reusable utilities and generates dashboard-ready CSV artifacts.

---

## 6️⃣ Dynamic Data Registry System

A centralized registry system dynamically maps:

```text
section → processed dataset path
```

This enables:

* scalable dashboard rendering
* modular loading
* easy dataset expansion

---

# 🌍 Dashboard Features

## 📊 Dashboard Sections

### Economy

* GDP
* GDP Growth
* Inflation
* Unemployment
* GDP Per Capita

### Demographics

* Population
* Life Expectancy
* Birth Rate

### Trade

* Exports
* Imports
* Trade Balance

### Technology

* Internet Usage
* Mobile Connectivity

### Environment

* CO₂ Emissions
* Renewable Energy Metrics

### Industry

* Industrial Indicators

### Military

* Military Spending
* Defense Metrics

---

# 🌎 Interactive World Map

The dashboard includes an interactive choropleth world map visualization.

### Features

* ISO3 country mapping
* Dynamic metric selection
* Year-based filtering
* Interactive hover analytics
* Global comparative analysis

Built using:

* Plotly Choropleth
* PyCountry ISO3 mapping

---

# 📈 Interactive Analytics Features

## Compare Mode

Compare up to 3 countries simultaneously with:

* shared filters
* synchronized visualizations
* unified hover analytics

## KPI Cards

Dynamic KPI cards with:

* formatted numerical scaling
* delta calculations
* semantic color indicators

## Interactive Charts

* Plotly visualizations
* responsive layouts
* unified hover mode
* time-series analytics

---

# 🧩 Modular Visualization Architecture

The dashboard visualization layer is fully modular:

```text
Dashboard/
│
├── components/
│   ├── charts
│   ├── KPI cards
│   └── world map
│
├── visualizations/
│   ├── economy dashboard
│   ├── trade dashboard
│   ├── environment dashboard
│   └── world map dashboard
```

This architecture enables:

* reusable components
* scalable dashboard expansion
* maintainable visualization logic

---

# 🛠️ Tech Stack

## Data Engineering

* Python
* Pandas
* NumPy

## Visualization

* Streamlit
* Plotly

## Pipeline Architecture

* Modular artifact system
* Registry-driven processing
* Config-based pipeline design

## Additional Libraries

* PyCountry
* Requests
* JSON

---

# 📂 Project Structure

```text
Country-Dashboard/
│
├── Dashboard/
│
├── src/
│   ├── Ingestion/
│   ├── Processing/
│   ├── Section_Processing/
│   ├── Entity/
│   └── Utils/
│
├── artifacts/
│
├── requirements.txt
├── README.md
└── config.yaml
```

---

# 🚀 Run Locally

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/country-dashboard.git
cd country-dashboard
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Dashboard

```bash
streamlit run Dashboard/app.py
```

---

# 🔮 Future Improvements

* Animated world map timelines
* AI-generated insights
* Forecasting models
* Trade flow visualizations
* Regional clustering
* News & sentiment integration
* Interactive drill-down analytics

---

# 👨‍💻 Author

Aditya Rai

---

# ⭐ If you liked this project

Consider giving the repository a star ⭐
