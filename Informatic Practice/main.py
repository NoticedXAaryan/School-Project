# Licensed under the Apache License, Version 2.0 (Just Kidding... But ask before copying... I'm bored...;~] )
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License from NOTICEDXAARYAN (NoticedXAaryan@Gmail.Com)

# Hey, If you have any questions just ask me.... cause as I said.. I'm Bored
# If you are here for evaluation "Sir/Madam...!!! Please go easy on me... :)"

import os
import pandas as pd
import random
import logging
from matplotlib import pyplot as plt

# Directory (Fancy word-choice) to save/load CSV files
FILE_LOCATION = "saved_projects"
os.makedirs(FILE_LOCATION, exist_ok=True)

# Configuring up logging
logging.basicConfig(filename='Activities.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s') # It's the most basic logging format

# As I'm a higher species of dev who has tasted the perks functions and error handling to the dev... I am definitely using it.

# Function for a lazy developer (To log information and display it... *if specified)
def log_and_print(message, displayText=False):# love torturing myself... that's why I have used True rather than None..
    if displayText:
        print(message)
    logging.info(message)

# Additional corrections applied throughout code.

# Collect user data for analysis (Definitely not the Facebook way)
def collect_data():
    log_and_print("Starting new analysis...\n",True)
    try:
        project_name = input("Enter Project Name: ")
        log_and_print(f"Project Name entered: {project_name}")
        
        people_count = int(input("Enter the number of people: "))
        log_and_print(f"Number of people entered: {people_count}")
        
        data = {}

        for i in range(people_count):
            name = input(f"Enter name for person {i + 1}: ")
            log_and_print(f"Name entered for person {i + 1}: {name}", "if the world was ending")
            
            categories = ["Food", "Transport", "Entertainment", "Clothes", "Miscellaneous"] # fancy, are we
            expenses = {}                                                                   # perks of having a degree in class 12
                                                                                            # perks of having an internship at the age of 16
            for category in categories:
                expense = float(input(f"Enter {name}'s spending on {category}: "))
                expenses[category] = expense
                log_and_print(f"{name}'s spending on {category}: {expense}" )
            
            data[name] = expenses

        save_data_to_csv(data, project_name)
    except ValueError as e:  
        log_and_print(f"Invalid input. Error: {e}" , True ) 

def save_data_to_csv(data, project_name):
    try:
        df = pd.DataFrame(data).T   # They say transpose is out of syllabus... But do I really care
        file_path = os.path.join(FILE_LOCATION, f"{project_name}.csv") # My main aim is to have a daring and fun life...
        df.to_csv(file_path)
        log_and_print(f"Data saved to {file_path}" , True )
        show_analysis_menu(df)
    except Exception as e:
        log_and_print(f"Error saving data: {e}" , True )

# Load existing data
def load_data():
    try:
        csv_files = [f for f in os.listdir(FILE_LOCATION) if f.endswith('.csv')] # NGL thank god it works
        if not csv_files:
            log_and_print("No previous analyses found." , True )
            return

        log_and_print("Previous analyses available:" , True )
        for idx, file_name in enumerate(csv_files, start=1):   # Btw idx is a fancy term for index
            log_and_print(f"{idx}. {file_name}" , True )

        file_choice = int(input("Select a file by number: ")) - 1  # -1... wondering why? It's Python, my brother)
        selected_file = os.path.join(FILE_LOCATION, csv_files[file_choice])
        df = pd.read_csv(selected_file, index_col=0)
        log_and_print(f"Data from {csv_files[file_choice]} loaded successfully." , True )
        show_analysis_menu(df)
    except (ValueError, IndexError) as e:
        log_and_print(f"Invalid input. Error: {e}" , True )
    except Exception as e:
        log_and_print(f"Error loading file: {e}" , True )

# Visualization functions 
def show_analysis_menu(data_frame):
    log_and_print("Displaying analysis menu.")
    while True:
        print("\n" + "____________________________________________")
        print("| Press |               Menu                |")
        print("|_______|___________________________________|")
        print("|   1   | Comparative Bar Graph             |")
        print("|   2   | Individual Bar Graph              |")
        print("|   3   | Pie Chart                         |")
        print("|   4   | Descriptive Analysis              |") 
        print("|   5   | Exit to Main Menu                 |")
        print("|_______|___________________________________|")

        # Guess the song " Got music in you baby tell me why? " 

        try:
            choice = int(input("Enter choice: "))
            log_and_print(f"User selected analysis menu option: {choice}")
            if choice == 1:
                plot_comparative_bar(data_frame)
            elif choice == 2:
                plot_individual_bar(data_frame)
            elif choice == 3:
                plot_pie_chart(data_frame)
            elif choice == 4:
                descriptive_analysis(data_frame)  
            elif choice == 5:
                log_and_print("Exiting analysis menu.")
                break
            else:
                log_and_print("Invalid choice.")
        except ValueError as e:
            log_and_print(f"Invalid input. Error: {e}")

# Functions to make my life easier
def plot_comparative_bar(data_frame):
    try:
        log_and_print("Generating comparative bar graph.")
        data_frame.plot.bar(
            figsize=(10, 6), title="Spending Comparison Across People",
            ylabel="Amount Spent", xlabel="Category")
        plt.show()
    except Exception as e:
        log_and_print(f"Error plotting comparative bar graph: {e}")

def plot_individual_bar(data_frame):
    try:
        log_and_print("Generating individual bar graphs.")
        for person in data_frame.index:
            data_frame.loc[person].plot.bar(
                title=f"{person}'s Spending by Category", ylabel="Amount Spent")
            plt.show()
    except Exception as e:
        log_and_print(f"Error plotting individual bar graph: {e}")

def plot_pie_chart(data_frame):
    try:
        log_and_print("Generating pie charts.")
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
        log_and_print("Performing descriptive analysis.")
        
        summary_df = pd.DataFrame(index=data_frame.index)
        summary_df['Total Spent'] = data_frame.sum(axis=1)
        summary_df['Average Spent'] = data_frame.mean(axis=1)
        summary_df['Minimum Spent'] = data_frame.min(axis=1)
        summary_df['Maximum Spent'] = data_frame.max(axis=1)
        summary_df['Most Spent Field'] = data_frame.idxmax(axis=1)
        summary_df['Least Spent Field'] = data_frame.idxmin(axis=1)
        
        print("\nDescriptive Analysis Summary:\n")
        print("Total, average, minimum, and maximum spending for each person, along with fields where spending is highest and lowest.")
        print(summary_df)

        print("\nInsights:")
        avg_total = summary_df['Total Spent'].mean()
        max_spent = summary_df['Maximum Spent'].max()
        most_common = summary_df['Most Spent Field'].mode()[0]
        
        print(f"Average total spending across all people: {avg_total:.2f}")
        print(f"Overall maximum spending in a single category by an individual: {max_spent:.2f}")
        print(f"Most common category with highest spending: {most_common}")
        
        log_and_print(f"Descriptive analysis completed. Avg total spending: {avg_total}, Max spent: {max_spent}, Most common field: {most_common}")
    except Exception as e:
        log_and_print(f"Error in descriptive analysis: {e}" , True)

# Function for Quotes_Loader2000 
def Quotes_loader2000():
    try:
        quotes = pd.read_csv("Quotes/quotes.csv")
        random_index = random.randint(0, len(quotes) - 1)
        random_quote = quotes.loc[random_index, 'Quote']
        print(f"Quote of the Day: {random_quote}")
        log_and_print("Quote displayed successfully.")
    except Exception as e:
        log_and_print(f"Error loading or displaying quote: {e}", True)
        

# Main Menu Function
def main_menu():
    log_and_print("Starting program. Displaying main menu.")
    while True:
        print("\n" + "______________________________________________")
        print("| Press |             Main Menu              |")
        print("|_______|____________________________________|")
        print("|   1   | Collect New Data                   |")
        print("|   2   | Load Existing Data                 |")
        print("|   3   | Cure Depression                    |")
        print("|   4   | Exit                               |")
        print("|_______|____________________________________|")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                collect_data()
            elif choice == 2:
                load_data()
            elif choice == 3:
                Quotes_loader2000()
            elif choice == 4:
                log_and_print("Exiting program.", True )
                break
            else:
                print("Invalid choice.")
        except ValueError as e:
            log_and_print(f"Invalid input. Error: {e}", True)

# To run the program
main_menu()