#!/usr/bin/env python3
"""
Mini Data Analysis Project

This script demonstrates basic data analysis operations using pandas and matplotlib.
It loads a CSV dataset, performs grouping and summarization, and generates visualizations.

Author: Your Name
Date: 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """
    Load CSV data into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded dataset
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Data loaded successfully from {file_path}")
        print(f"   Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"   Columns: {list(df.columns)}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def explore_data(df):
    """
    Perform basic data exploration.

    Args:
        df (pd.DataFrame): Input dataset
    """
    print("\n📊 DATA EXPLORATION")
    print("=" * 50)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nSummary statistics:")
    print(df.describe())

    print("\nMissing values:")
    print(df.isnull().sum())

def group_and_summarize(df, group_column, value_column):
    """
    Group data by a column and compute summary statistics.

    Args:
        df (pd.DataFrame): Input dataset
        group_column (str): Column to group by
        value_column (str): Column to aggregate

    Returns:
        pd.DataFrame: Grouped summary
    """
    print(f"\n📈 GROUPING AND SUMMARIZATION ({group_column} -> {value_column})")
    print("=" * 70)

    # Group and compute aggregations
    grouped = df.groupby(group_column)[value_column].agg(['count', 'sum', 'mean', 'min', 'max'])

    print("Summary by group:")
    print(grouped)

    return grouped

def create_visualization(df, group_column, value_column, output_path):
    """
    Create a bar chart visualization and save it as PNG.

    Args:
        df (pd.DataFrame): Input dataset
        group_column (str): Column for x-axis
        value_column (str): Column for y-axis
        output_path (str): Path to save the chart
    """
    print(f"\n📊 CREATING VISUALIZATION")
    print("=" * 30)

    # Prepare data for plotting
    plot_data = df.groupby(group_column)[value_column].mean().sort_values(ascending=False)

    # Create the plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(range(len(plot_data)), plot_data.values, color='skyblue', edgecolor='navy', linewidth=1.5)

    # Customize the plot
    plt.title(f'Average {value_column} by {group_column}', fontsize=16, fontweight='bold')
    plt.xlabel(group_column, fontsize=12)
    plt.ylabel(f'Average {value_column}', fontsize=12)
    plt.xticks(range(len(plot_data)), plot_data.index, rotation=45, ha='right')

    # Add value labels on bars
    for bar, value in zip(bars, plot_data.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(plot_data.values)*0.01,
                f'{value:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()

    # Save the plot
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Chart saved as '{output_path}'")

    # Show the plot (optional, comment out if running in headless environment)
    # plt.show()

def main():
    """
    Main function to run the data analysis workflow.
    """
    print("🚀 MINI DATA ANALYSIS PROJECT")
    print("=" * 40)

    # File paths
    data_file = 'sample_data.csv'
    output_chart = 'analysis_chart.png'

    # Load data
    df = load_data(data_file)
    if df is None:
        return

    # Explore data
    explore_data(df)

    # Assuming the CSV has columns like 'category' and 'value'
    # You can modify these based on your actual data
    group_col = 'category' if 'category' in df.columns else df.columns[0]
    value_col = 'value' if 'value' in df.columns else df.select_dtypes(include=['number']).columns[0]

    print(f"\nUsing '{group_col}' as grouping column and '{value_col}' as value column")

    # Group and summarize
    summary = group_and_summarize(df, group_col, value_col)

    # Create visualization
    create_visualization(df, group_col, value_col, output_chart)

    print("\n🎉 ANALYSIS COMPLETE!")
    print("=" * 20)
    print("Summary of operations performed:")
    print("• Loaded CSV data")
    print("• Explored data structure and statistics")
    print("• Grouped data and computed aggregations")
    print("• Generated bar chart visualization")
    print(f"• Saved chart as '{output_chart}'")

if __name__ == "__main__":
    main()
