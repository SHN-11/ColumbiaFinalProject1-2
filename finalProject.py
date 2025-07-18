import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import time
#https://datacommons.org/place/geoId/3604710022?utm_medium=explore&mprop=income&popt=Person&cpv=age,Years15Onwards&hl=en

#Link to join liveshare:https://prod.liveshare.vsengsaas.visualstudio.com/join?C373CBA7BE95F6259706F9A0CA7651093F04 
#Unpacking data and tranforming it into sentences 
covid_df = pd.read_csv('covid19finalproject.csv')
#a dictionary for the income of the 5 bouroughs
dictIncome = {#column 1: 2021, column 2: 2022, column 3: 2023
                "Manhattan": [93103,99531,101078], 
                "Staten Island": [94796,96726,95543], 
                "Queens": [80705,83637,81929],
                "Brooklyn": [74431,76778,76912],
                "Bronx": [47380,47257,46838]
                }
#a dictionary for the population for all five boroughs from the years 2021,2022, and 2023
populationDict = {
                    "Brooklyn": 2596093,
                    "Queens": 2286587,
                    "Manhattan": 1590016,
                    "Bronx": 1387456,
                    "Staten Island": 491864
                    }   
               



# Show the graph
plt.show()
#takes the index/ column from covid_df and uses a function called to_datetime and then uses another function called isin for each of the years
covid_df['date_of_interest'] = pd.to_datetime(covid_df['date_of_interest'])
filtered_df_2021 = covid_df[covid_df['date_of_interest'].dt.year.isin([2021])]
#year 2022
covid_df['date_of_interest'] = pd.to_datetime(covid_df['date_of_interest'])
filtered_df_2022 = covid_df[covid_df['date_of_interest'].dt.year.isin([2022])]
#year 2023
covid_df['date_of_interest'] = pd.to_datetime(covid_df['date_of_interest'])
filtered_df_2023 = covid_df[covid_df['date_of_interest'].dt.year.isin([2023])]
#all 3 of the years
covid_df['date_of_interest'] = pd.to_datetime(covid_df['date_of_interest'])
filtered_df_all = covid_df[covid_df['date_of_interest'].dt.year.isin([2021, 2022, 2023])]
#asks the input of the user and what year they want data from. gives 4 options, 2021,2022,2023 and all
user_input_year = input("What year do you want data from(2021, 2022, 2023 or all)?")
#if statement for the input function above to check if the user inputed 2021
if user_input_year == "2021":

    time.sleep(.5)
    
    print("")
    print("THIS DATASET IS COVID-19 IN THE YEAR: 2021")
    time.sleep(.5)
    print(f"")
    print("_____________________________________________________________")
    print(f"") 
    print("CASE COUNT FOR EACH BOUROGUH:")
    time.sleep(.5)
    print(f"") 
    #says the samething 5 times but for the each of the bouroughs and using the dataframe: filtered_df_2021
    print(f"The average Manhattan case count for COVID-19 is {filtered_df_2021['MN_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    #same thing as above but for staten island
    print(f"The average Staten Island case count for COVID-19 is {filtered_df_2021['SI_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    #same thing as above but for queens
    print(f"The average Queen case count for COVID-19 is {filtered_df_2021['QN_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    #same thing as above but for brooklyn
    print(f"The average Brooklyn case count for COVID-19 is {filtered_df_2021['BK_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    #same thing as above but for bronx
    print(f"The average Bronx case count for COVID-19 is {filtered_df_2021['BX_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"") 
    print("___________________________________________________________")
    print("                                                             ")
    #now is saying the deathrate 
    print("DEATHRATE AND INCOME RANKED:")
    #In order of income and showing the deathrate for each bouroguh per day
    time.sleep(.5)
    print(f"") 
    print(f"Manhattan comes first in income. Deathrate: {filtered_df_2021['MN_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    #same thing as above but for staten island
    print(f"Staten island comes second in income. Deathrate: {filtered_df_2021['SI_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    #same thing as above but for queens
    print(f"Queens comes third in income. Deathrate: {filtered_df_2021['QN_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    #same thing as above but for brooklyn
    print(f"Brooklyn comes fourth  in income. Deathrate: {filtered_df_2021['BK_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    #same thing as above but for bronx
    print(f"Bronx comes last in income. Deathrate: {filtered_df_2021['BX_DEATH_COUNT'].mean():.2f}")
    #print(covid_df.dtypes)
    #purpose: to find the corralation between income and death between boroughs
    #
    #comparing population to death count
#same thing as above but for the year 2022
elif user_input_year == "2022":
#covid_df['date_of_interest'] = dt.date(covid_df['date_of_interest'])
#Iterate over the column and convert all to datetimes
# #Conditional filtering for 2023 or 2022 or 2021
    time.sleep(.5)
    print("")
    print("THIS DATASET IS COVID-19 IN THE YEAR: 2022")
    time.sleep(.5)
    print(f"")
    print("_____________________________________________________________")
    print(f"") 
    print("CASE COUNT FOR EACH BOUROGUH:")
    time.sleep(.5)
    print(f"") 
    print(f"The average Manhattan case count for COVID-19 is {filtered_df_2022['MN_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"The average Staten Island case count for COVID-19 is {filtered_df_2022['SI_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"The average Queen case count for COVID-19 is {filtered_df_2022['QN_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"The average Brooklyn case count for COVID-19 is {filtered_df_2022['BK_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"The average Bronx case count for COVID-19 is {filtered_df_2022['BX_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"") 
    print("___________________________________________________________")
    print("                                                             ")
    print("DEATHRATE AND INCOME RANKED:")
    #In order of income
    time.sleep(.5)
    print(f"") 
    print(f"Manhattan comes first in income. Deathrate: {filtered_df_2022['MN_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Staten island comes second in income. Deathrate: {filtered_df_2022['SI_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Queens comes third in income. Deathrate: {filtered_df_2022['QN_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Brooklyn comes fourth  in income. Deathrate: {filtered_df_2022['BK_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Bronx comes last in income. Deathrate: {filtered_df_2022['BX_DEATH_COUNT'].mean():.2f}")
    #print(covid_df.dtypes)
    #purpose: to find the corralation between income and death between boroughs
    #
    #comparing population to death count
#same thing as above but for the year 2023
elif user_input_year == "2023":
#covid_df['date_of_interest'] = dt.date(covid_df['date_of_interest'])
#Iterate over the column and convert all to datetimes
# #Conditional filtering for 2023 or 2022 or 2021
    print("")
    time.sleep(.5)
    print("THIS DATASET IS COVID-19 IN THE YEAR: 2023")
    print(f"")
    print("_____________________________________________________________")
    print(f"") 
    print("CASE COUNT FOR EACH BOUROGUH:")
    print(f"") 
    time.sleep(.5)
    print(f"The average Manhattan case count for COVID-19 is {filtered_df_2023['MN_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"The average Staten Island case count for COVID-19 is {filtered_df_2023['SI_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"The average Queen case count for COVID-19 is {filtered_df_2023['QN_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"The average Brooklyn case count for COVID-19 is {filtered_df_2023['BK_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)
    print(f"The average Bronx case count for COVID-19 is {filtered_df_2023['BX_CASE_COUNT'].mean():.2f} each day")
    time.sleep(.5)

    print(f"") 
    print("___________________________________________________________")
    print("                                                             ")
    print("DEATHRATE AND INCOME RANKED:")
    #In order of income
    time.sleep(.5)
    print(f"") 
    print(f"Manhattan comes first in income. Deathrate: {filtered_df_2023['MN_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Staten island comes second in income. Deathrate: {filtered_df_2023['SI_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Queens comes third in income. Deathrate: {filtered_df_2023['QN_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Brooklyn comes fourth  in income. Deathrate: {filtered_df_2023['BK_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Bronx comes last in income. Deathrate: {filtered_df_2023['BX_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    #print(covid_df.dtypes)
    #purpose: to find the corralation between income and death between boroughs
    #
    #comparing population to death count
    print("")
    print("___________________________________________________")
    print("")
    #print(covid_df.iterrows)
#same thing as above but for all three years
elif user_input_year == "all":
    #covid_df['date_of_interest'] = dt.date(covid_df['date_of_interest'])
#Iterate over the column and convert all to datetimes
# #Conditional filtering for 2023 or 2022 or 2021
    print("")
    time.sleep(.5)
    print("THIS DATASET IS COVID-19 IN THE YEARS: 2021, 2022, and 2023")
    time.sleep(.5)
    print(f"")
    print("_____________________________________________________________")
    print(f"") 
    print("CASE COUNT FOR EACH BOUROGUH:")
    time.sleep(.5)
    print(f"") 
    print(f"The average Manhattan case count for COVID-19 is {filtered_df_all['MN_CASE_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"The average Staten Island case count for COVID-19 is {filtered_df_all['SI_CASE_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"The average Queen case count for COVID-19 is {filtered_df_all['QN_CASE_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"The average Brooklyn case count for COVID-19 is {filtered_df_all['BK_CASE_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"The average Bronx case count for COVID-19 is {filtered_df_all['BX_CASE_COUNT'].mean():.2f}")
    time.sleep(.5)

    print(f"") 
    print("___________________________________________________________")
    print("                                                             ")
    print("DEATHRATE AND INCOME RANKED:")
    time.sleep(.5)
    #In order of income
    
    print(f"") 
    print(f"Manhattan comes first in income. Deathrate: {filtered_df_all['MN_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Staten island comes second in income. Deathrate: {filtered_df_all['SI_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Queens comes third in income. Deathrate: {filtered_df_all['QN_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Brooklyn comes fourth  in income. Deathrate: {filtered_df_all['BK_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    print(f"Bronx comes last in income. Deathrate: {filtered_df_all['BX_DEATH_COUNT'].mean():.2f}")
    time.sleep(.5)
    #print(covid_df.dtypes)
    #purpose: to find the corralation between income and death between boroughs
    #
    #comparing population to death count

print("")
time.sleep(1.5)
#asking for user input to see one of two graphs
user_input_graph = input("Which graph would you like to see? Type 'B' for borough vs. case count, 'Y' for year vs. case count, or 'Q' to quit: ").upper()
#saying that if they input q then it quits this loop and goes on to the other input
if user_input_graph == "q":
    print("")
#Then load one of the graphs which says the year vs. case count
if user_input_graph == "Y":
    print("Loading Graph Now......")
    time.sleep(2.5)
    # Data for the graph
    x = [2021, 2022, 2023] # X-axis values
    y = [filtered_df_2021['CASE_COUNT'].mean(), 
         filtered_df_2022['CASE_COUNT'].mean(), 
         filtered_df_2023['CASE_COUNT'].mean()]  # Y-axis values


    # Create the line plot
    plt.plot(x, y, label='', color='red', marker='o')

    # Add labels and title
    plt.xlabel('Years')
    plt.ylabel('Case Count for that year')
    plt.title('Line Graph For Years and Case Count')

    # Add a legend
    plt.legend()

    # Show the graph
    plt.show()
#same as above but for borough vs. case count
if user_input_graph == "B":
    print("Loading Graph Now......")
    time.sleep(2.5)
    # Data for the graph
    x = ['Manhattan',"Brooklyn","Bronx", "Staten Island", "Queens"] # X-axis values
    y = [filtered_df_all['MN_CASE_COUNT'].mean(), filtered_df_all['BK_CASE_COUNT'].mean(), filtered_df_all['BX_CASE_COUNT'].mean(), filtered_df_all['SI_CASE_COUNT'].mean(), filtered_df_all['QN_CASE_COUNT'].mean()]  # Y-axis values


    # Create the line plot
    plt.plot(x, y, label='', color='green', marker='o')

    # Add labels and title
    plt.xlabel('Boroughs')
    plt.ylabel('Case Count for each borough')
    plt.title('Line Graph For Borough and Case Count for each')



    # Show the graph
    plt.show()
#the third user_input asking for t
user_input_3 = input("Which comparison graph would you like to see? Type 'DC' for population vs. case count, 'BD' for income per person vs. case count, or 'Q' to quit: ").upper()
if user_input_3 == "BD":
    print("Loading Graph Now......")
    time.sleep(2.5)
    # Data for the graphcl
    x = dictIncome.keys() # X-axis values
    y = [filtered_df_all['MN_CASE_COUNT'].mean(), 
         filtered_df_all['SI_CASE_COUNT'].mean(), 
         filtered_df_all['QN_CASE_COUNT'].mean(),
         filtered_df_all['BK_CASE_COUNT'].mean(),
         filtered_df_all['BX_CASE_COUNT'].mean()]  # Y-axis values


    # Create the line plot
    plt.plot(x, y, label='', color='purple', marker='o')

    # Add labels and title
    plt.xlabel('Borough Case ')
    plt.ylabel('Case Count for that year')
    plt.title('Line Graph For Years and Case Count')

    # Show the graph
    plt.show()

if user_input_3 == "DC":
    print("Loading Graph Now......")
    time.sleep(2.5)
    # Data for the graph
    x = filtered_df_all['7'] # X-axis values
    y = [filtered_df_all['MN_CASE_COUNT'].mean(), 
         filtered_df_all['SI_CASE_COUNT'].mean(), 
         filtered_df_all['QN_CASE_COUNT'].mean(),
         filtered_df_all['BK_CASE_COUNT'].mean(),
         filtered_df_all['BX_CASE_COUNT'].mean()]  # Y-axis values


    # Create the line plot
    plt.plot(x, y, label='', color='red', marker='o')

    # Add labels and title
    plt.xlabel('Population for borough in population size ranked order')
    plt.ylabel('Case Count for that year')
    plt.title('Line Graph For Years and Case Count')

    

    # Show the graph
    plt.show()
"""
if user_input_3 == "TWO":
    print("Loading Graph Now......")
    time.sleep(2.5)
    # Data for the graph
    x = filtered_df_all['CASE_COUNT_7DAY_AVG'] # X-axis values
    y = [ filtered_df_2021['CASE_COUNT'].mean(), 
            filtered_df_2022['CASE_COUNT'].mean(), 
            filtered_df_2023['CASE_COUNT'].mean()]  # Y-axis values


    # Create the line plot
    plt.plot(x, y, label='', color='red', marker='o')

    # Add labels and title
    plt.xlabel('Population for borough in population size ranked order')
    plt.ylabel('Case Count for that year')
    plt.title('Line Graph For Years and Case Count')

"""