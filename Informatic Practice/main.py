# Licensed under the Apache License, Version 2.0 (the "License")
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License from NOTICEDXAARYAN (NoticedXAaryan@Gmail.Com)

import os
import pandas as pd
import logging
from matplotlib import pyplot as plt

# Directory to save/load CSV files
FILE_LOCATION = "saved_projects"
os.makedirs(FILE_LOCATION, exist_ok=True)

# Setting up logging
logging.basicConfig(filename='Activities.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_and_print(message):
    print(message)
    logging.info(message)

# Collect user data for analysis
def collect_data():
    log_and_print("Starting new analysis...\n")
    try:
        project_name = input("Enter Project Name: ")
        people_count = int(input("Enter the number of people: "))
        data = {}

        for i in range(people_count):
            name = input(f"Enter name for person {i + 1}: ")
            categories = ["Food", "Transport", "Entertainment", "Clothes", "Miscellaneous"]
            expenses = {}
            for category in categories:
                expenses[category] = float(input(f"Enter {name}'s spending on {category}: "))
            data[name] = expenses

        save_data_to_csv(data, project_name)
    except ValueError as e:
        log_and_print(f"Invalid input. Error: {e}")

def save_data_to_csv(data, project_name):
    try:
        df = pd.DataFrame(data).T
        file_path = os.path.join(FILE_LOCATION, f"{project_name}.csv")
        df.to_csv(file_path)
        log_and_print(f"Data saved to {file_path}")
        show_analysis_menu(df)
    except Exception as e:
        log_and_print(f"Error saving data: {e}")

# Load existing data
def load_data():
    try:
        csv_files = [f for f in os.listdir(FILE_LOCATION) if f.endswith('.csv')]
        if not csv_files:
            log_and_print("No previous analyses found.")
            return

        print("Available analyses:")
        for idx, file_name in enumerate(csv_files, start=1):
            print(f"{idx}. {file_name}")

        file_choice = int(input("Select a file by number: ")) - 1
        selected_file = os.path.join(FILE_LOCATION, csv_files[file_choice])
        df = pd.read_csv(selected_file, index_col=0)
        log_and_print(f"Data from {csv_files[file_choice]} loaded successfully.")
        show_analysis_menu(df)
    except (ValueError, IndexError) as e:
        log_and_print(f"Invalid input. Error: {e}")
    except Exception as e:
        log_and_print(f"Error loading file: {e}")

# Visualization functions
def show_analysis_menu(data_frame):
    while True:
        print("\n" + "___________________________________________")
        print("| Press |               Menu                |")
        print("|_______|___________________________________|")
        print("|   1   | Comparative Bar Graph             |")
        print("|   2   | Individual Bar Graph              |")
        print("|   3   | Pie Chart                         |")
        print("|   4   | Descriptive Analysis              |") 
        print("|   5   | Exit to Main Menu                 |")
        print("|_______|___________________________________|")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                plot_comparative_bar(data_frame)
            elif choice == 2:
                plot_individual_bar(data_frame)
            elif choice == 3:
                plot_pie_chart(data_frame)
            elif choice == 4:
                descriptive_analysis(data_frame)  # Corrected the typo here
            elif choice == 5:
                break
            else:
                log_and_print("Invalid choice.")
        except ValueError as e:
            log_and_print(f"Invalid input. Error: {e}")

def plot_comparative_bar(data_frame):
    try:
        data_frame.plot.bar(
            figsize=(10, 6), title="Spending Comparison Across People",
            ylabel="Amount Spent", xlabel="Category")
        plt.show()
    except Exception as e:
        log_and_print(f"Error plotting comparative bar graph: {e}")

def plot_individual_bar(data_frame):
    try:
        for person in data_frame.index:
            data_frame.loc[person].plot.bar(
                title=f"{person}'s Spending by Category", ylabel="Amount Spent")
            plt.show()
    except Exception as e:
        log_and_print(f"Error plotting individual bar graph: {e}")

def plot_pie_chart(data_frame):
    try:
        for person in data_frame.index:
            data_frame.loc[person].plot.pie(
                autopct='%1.1f%%', startangle=90,
                title=f"{person}'s Spending Breakdown", figsize=(6, 6))
            plt.ylabel('')
            plt.show()
    except Exception as e:
        log_and_print(f"Error plotting pie chart: {e}")

def descriptive_analysis(data_frame):
    try:
        # Create a summary DataFrame for analysis
        summary_df = pd.DataFrame(index=data_frame.index)
        summary_df['Total Spent'] = data_frame.sum(axis=1)
        summary_df['Average Spent'] = data_frame.mean(axis=1)
        summary_df['Minimum Spent'] = data_frame.min(axis=1)
        summary_df['Maximum Spent'] = data_frame.max(axis=1)
        summary_df['Most Spent Field'] = data_frame.idxmax(axis=1)
        summary_df['Least Spent Field'] = data_frame.idxmin(axis=1)

        # Display the summary statistics for each individual
        print("\nDescriptive Analysis Summary:\n")
        print("Total, average, minimum, and maximum spending for each person, along with fields where spending is highest and lowest.")
        print(summary_df)

        # Print some additional insights if relevant
        print("\nInsights:")
        print(f"Average total spending across all people: {summary_df['Total Spent'].mean():.2f}")
        print(f"Overall maximum spending in a single category by an individual: {summary_df['Maximum Spent'].max():.2f}")
        print(f"Most common category with highest spending: {summary_df['Most Spent Field'].mode()[0]}")
    except Exception as e:
        log_and_print(f"Error in descriptive analysis: {e}")

# Main Menu Function
def main_menu():
    while True:
        print("\n" + "_____________________________________________")
        print("| Press |               Menu                |")
        print("|_______|___________________________________|")
        print("|   1   | New Project                       |")
        print("|   2   | Old Project                       |")
        print("|   3   | Exit                              |")
        print("|_______|___________________________________|")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                collect_data()
            elif choice == 2:
                load_data()
            elif choice == 3:
                log_and_print("Exiting program.")
                break
            else:
                log_and_print("Invalid choice.")
        except ValueError as e:
            log_and_print(f"Invalid input. Error: {e}")

# Run the main menu
main_menu()
