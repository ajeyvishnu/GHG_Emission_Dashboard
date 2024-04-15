#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 01:36:52 2024

@author: ajayvishnu
"""

import pandas as pd
import numpy as np

# Define company names
companies = ['Your Company', 'Company A', 'Company B', 'Company C', 'Company D']

# Define months and years
months_years = pd.date_range(start='2020-01', end='2024-01', freq='M')

# Define segments
segments = ['Manufacturing', 'Technology', 'Transportation']

# Define cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

# Define emission sources and scopes
sources_scopes = {
    'Fuel Combustion': 'Scope 1',
    'Facilities': 'Scope 1',
    'Electricity': 'Scope 2',
    'Inbound Transport': 'Scope 3',
    'Outbound Transport': 'Scope 3',
    'Waste Management': 'Scope 3',
    'Raw Materials': 'Scope 3',
    'Outsourced Processes': 'Scope 3'
}

# Create empty lists to store data
data = {'Company': [], 'Month and Year': [], 'Segment': [], 'City': [], 'Source': [], 'Scope': [],
        'CO2 Emissions': [], 'Methane Emissions': [], 'Nitrous Oxide Emissions': [], 'GHG Total Emissions': [],
        'Cost Spent due to GHG Emissions': [], 'Cost Savings': []}

# Generate data for each company, month, and segment
for company in companies:
    for month_year in months_years:
        for segment in segments:
            for city in cities:
                for source, scope in sources_scopes.items():
                    # Generate random emissions and costs with variations based on company
                    emission_factor = np.random.uniform(0.5, 1.0)  # Vary emissions by 50% to 100%
                    cost_factor = np.random.uniform(0.5, 1.0)  # Vary costs by 50% to 100%
                    
                    co2 = np.random.uniform(100, 1000) * emission_factor
                    methane = np.random.uniform(10, 100) * emission_factor
                    nitrous_oxide = np.random.uniform(5, 50) * emission_factor
                    ghg_total = co2 + methane + nitrous_oxide + np.random.uniform(50, 200) * emission_factor
                    cost_spent = np.random.uniform(1000, 5000) * cost_factor
                    cost_savings = np.random.uniform(200, 1000) * cost_factor
                    
                    # Append data to lists
                    data['Company'].append(company)
                    data['Month and Year'].append(month_year)
                    data['Segment'].append(segment)
                    data['City'].append(city)
                    data['Source'].append(source)
                    data['Scope'].append(scope)
                    data['CO2 Emissions'].append(co2)
                    data['Methane Emissions'].append(methane)
                    data['Nitrous Oxide Emissions'].append(nitrous_oxide)
                    data['GHG Total Emissions'].append(ghg_total)
                    data['Cost Spent due to GHG Emissions'].append(cost_spent)
                    data['Cost Savings'].append(cost_savings)

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv('/Users/ajayvishnu/Downloads/emissions_data.csv', index=False)

# Display first few rows of the dataset
print(df.head())

