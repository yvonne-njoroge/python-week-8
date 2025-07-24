Project Overview
This project analyzes global COVID-19 data, including cases, deaths, recoveries, and vaccinations, across time and regions. The goal is to develop a clear and insightful report through data exploration, visualization, and narrative insights — all inside a Jupyter Notebook or exported as a PDF.


A cleaned and processed dataset

Time-series and comparative analyses

Visual charts and optional maps

A professional data report suitable for presentation or publishing

**🎯 Objectives**
✅ Import and clean COVID-19 global data
✅ Analyze time trends (cases, deaths, vaccinations)
✅ Compare metrics across countries/regions
✅ Visualize trends with charts and maps
✅ Communicate findings in a Jupyter Notebook or PDF report

**🧩 Project Structure**
1️⃣ Data Collection
Source: Our World in Data

File: owid-covid-data.csv

Download and save it in the working folder.

** Data Loading & Exploration**
Load the CSV using pandas.read_csv()

Explore with .head(), .columns, .isnull().sum()

Identify key features like:
date, location, total_cases, new_cases, total_deaths, total_vaccinations

**Data Cleaning**
Filter countries of interest (e.g., Kenya, USA, India)

Convert date to datetime format

Drop or fill missing values

Handle anomalies in numerical data

**Exploratory Data Analysis (EDA)**
Time-series plots of total cases and deaths

Compare daily new cases between countries

Calculate death rates: total_deaths / total_cases

Visualize with:

📈 Line charts

📊 Bar charts

🔥 Heatmaps (optional)

**Vaccination Analysis**
Visualize vaccination progress over time

Compare % vaccinated population

Charts:

Line charts for rollout trends

Optional pie charts for vax status


Insights & Reporting
Summarize 3–5 key findings

Highlight anomalies or standout trends

Write narrative insights using Markdown

**Final Deliverable:**
📓 Jupyter Notebook (.ipynb) with:

Clean code

Visualizations

Markdown commentary

Optional: Export to PDF or presentation format (e.g., PowerPoint)

**🛠️ Tools & Libraries**
Python 3.x

pandas

numpy

matplotlib

seaborn

plotly (optional)

geopandas (optional)

Jupyter Notebook