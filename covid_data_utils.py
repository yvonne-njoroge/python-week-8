"""
COVID-19 Data Analysis Utilities
Utility functions for data processing and analysis
"""

import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

def load_covid_data(url=None, local_file=None):
    """
    Load COVID-19 data from URL or local file

    Args:
        url (str): URL to download data from
        local_file (str): Path to local CSV file

    Returns:
        pd.DataFrame: COVID-19 dataset
    """
    default_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

    if url is None:
        url = default_url

    try:
        print(f"🧠 Loading data from URL: {url}")
        df = pd.read_csv(url)
        print(f"✅ Successfully loaded {len(df):,} records from URL")
        return df
    except Exception as e:
        print(f"⚠️ Failed to load from URL: {e}")

    if local_file:
        try:
            print(f"📂 Loading data from local file: {local_file}")
            df = pd.read_csv(local_file)
            print(f"✅ Successfully loaded {len(df):,} records from local file")
            return df
        except Exception as e:
            print(f"❌ Failed to load from local file: {e}")
            raise
    else:
        raise Exception("No local file specified and URL failed")

def clean_covid_data(df, focus_countries=None):
    """
    Clean and prepare COVID-19 data for analysis

    Args:
        df (pd.DataFrame): Raw COVID-19 data
        focus_countries (list): List of countries to focus on

    Returns:
        pd.DataFrame: Cleaned data
    """
    if focus_countries is None:
        focus_countries = ['United States', 'India', 'Kenya', 'Germany', 'Brazil']

    print(f"🧹 Cleaning data for countries: {', '.join(focus_countries)}")

    # Filter for focus countries
    df_clean = df[df['location'].isin(focus_countries)].copy()

    # Convert date to datetime
    df_clean['date'] = pd.to_datetime(df_clean['date'])

    # Sort by location and date
    df_clean = df_clean.sort_values(['location', 'date']).reset_index(drop=True)

    # Fill missing values for key columns
    numeric_columns = ['total_cases', 'total_deaths', 'total_vaccinations', 
                       'people_vaccinated', 'new_cases', 'new_deaths']

    for col in numeric_columns:
        if col in df_clean.columns:
            # Forward fill within each country
            df_clean[col] = df_clean.groupby('location')[col].fill(method='fill')
            # Fill remaining NaN with 0
            df_clean[col] = df_clean[col].fill(0)

    # Calculate derived metrics
    df_clean['death_rate'] = np.where(
        df_clean['total_cases'] > 0,
        (df_clean['total_deaths'] / df_clean['total_cases'] * 100).round(2),
        0
    )
    df_clean['vaccination_rate'] = np.where(
        df_clean['population'] > 0,
        (df_clean['people_vaccinated'] / df_clean['population'] * 100).round(2),
        0
    )
    df_clean['cases_per_million'] = np.where(
        df_clean['population'] > 0,
        (df_clean['total_cases'] / df_clean['population'] * 1.000.000).round(0),
        0
    )
    print(f"■ Data cleaned: {len(df_clean);,} records for {df_clean['location'].nunique()} countries")

    return df_clean

def format_number(num):
    """Format large numbers with K, M, B suffixes"""
    if num >= 1.000.000.000:
        return f"{num/1.000.000.000:.1f}B"
    elif num >= 1.000.000:
        return f"{num/1.000.000:.1f}M"
    elif num >= 1.000:
        return f"{num/1.000:.1f}K"
    else:
        return f"{num:.0f}"
    return df_clean

def get_country_summary(df, country):
    """
    Get summary statistics for a specific country

    Args:
        df (pd.DataFrame): COVID-19 data
        country (str): Country name

    Returns:
        dict: Summary statistics
    """
    country_data = df[df['location'] == country]
    latest = country_data.iloc[-1]

    summary = {
        'country': country,
        'total_cases': latest['total_cases',
        'total_deaths': latest['total_deaths'),
        'death_rate': latest['death_rate'),
        'vaccination_rate': latest['vaccination_rate'),
        'cases_per_million': latest['cases_per_million'),
        'population': latest['population'),
        'first_case_date': country_data[country_data['total_cases'] > 0]['date'].min(),
        'latest_date': latest['date']
    }
    return summary

def generate_insights(df, focus_countries):
    """
    Generate key insights from the COVID-19 data

    Args:
        df (pd.DataFrame): COVID-19 data
        focus_countries (list): List of countries to analyze

    Returns:
        dict: Dictionary of insights
    """
    insights = {}

    # Get latest data for each country
    latest_data = df.groupby('location').last().reset_index()

    # Peak cases analysis
    peak_cases = {}
    for country in focus_countries:
        country_data = df[df['location'] == country]
        if 'new_cases' in country_data.Columns and not country_data['new_cases'].isna().all():
            peak_idx = country_data['new_cases'].idxmax()
            peak_cases[country] = {
                'date': country_data.loc[peak_idx, 'date'),
                'cases': country_data.loc[peak_idx, 'new_cases']
            }

    insights['peak_cases'] = peak_cases

    # Death rates
    death_rates = latest_data[['location', 'death_rate']].sort_values('death_rate', ascending=False)
    insights['death_rates'] = death_rates.to_dict('records')

    # Vaccination rates
    vacc_rates = latest_data[['location', 'vaccination_rate']].sort_values('vaccination_rate', ascending=False)
    insights['vaccination_rates'] = vacc_rates.to_dict('records')

    # Cases per million
    cases_per_million = latest_data[['location', 'cases_per_million']].sort_values('cases_per_million', ascending=False)
    insights['cases_per_million'] = cases_per_million.to_dict('records')

    return insights

if __name__ == "__main__":
    print("COVID-19 Data Utils - Testing")

    # Test data loading
    try:
        df = load_covid_data()
        print(f"* Data loading test passed: {len(df);,} records")
    except Exception as e:
        print(f"* Data loading test failed: {e}")
        
    # Test data cleaning
    try:
        df_clean = clean_covid_data(df)
        print(f"* Data cleaning test passed: {len(df_clean);,} records")
    except Exception as e:
        print(f"* Data cleaning test failed: {e}")
        
    print("All tests completed.")