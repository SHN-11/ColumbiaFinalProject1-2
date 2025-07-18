import pandas as pd
import matplotlib.pyplot as plt

covid_df = pd.read_csv('covidData.csv')

dictIncome = {#column 1: 2021, column 2: 2022, column 3: 2023
                "Manhattan": [93103,99531,101078,97904], 
                "Staten Island": [94796,96726,95543,95688], 
                "Queens": [80705,83637,81929,82090],
                "Brooklyn": [74431,76778,76912,76040],
                "Bronx": [47380,47257,46838,47158]
                }

#2021
covid_df['date_of_interest'] = pd.to_datetime(covid_df['date_of_interest'])
filtered_df_2021 = covid_df[covid_df['date_of_interest'].dt.year.isin([2021])]
#2022
covid_df['date_of_interest'] = pd.to_datetime(covid_df['date_of_interest'])
filtered_df_2022 = covid_df[covid_df['date_of_interest'].dt.year.isin([2022])]
#2023
covid_df['date_of_interest'] = pd.to_datetime(covid_df['date_of_interest'])
filtered_df_2023 = covid_df[covid_df['date_of_interest'].dt.year.isin([2023])]
#all
covid_df['date_of_interest'] = pd.to_datetime(covid_df['date_of_interest'])
filtered_df_all = covid_df[covid_df['date_of_interest'].dt.year.isin([2021, 2022, 2023])]

user_year = input("2021, 2022, 2023, or all? ")

if user_year == "2021":
    #extract month 
    filtered_df_2021['month'] = filtered_df_2021['date_of_interest'].dt.month

    #groups by borough
    manhattan_avg = filtered_df_2021.groupby('month')['MN_DEATH_COUNT'].mean()
    staten_avg = filtered_df_2021.groupby('month')['SI_DEATH_COUNT'].mean()
    queens_avg = filtered_df_2021.groupby('month')['QN_DEATH_COUNT'].mean()
    brooklyn_avg = filtered_df_2021.groupby('month')['BK_DEATH_COUNT'].mean()
    bronx_avg = filtered_df_2021.groupby('month')['BX_DEATH_COUNT'].mean()

    #x and y values
    x = bronx_avg.index
    y_manhattan = manhattan_avg.values
    y_staten = staten_avg.values
    y_queens = queens_avg.values
    y_bronx = bronx_avg.values
    y_brooklyn = brooklyn_avg.values

    #legend
    plt.plot(x, y_manhattan, label='Manhattan')
    plt.plot(x, y_staten, label='Staten Island')
    plt.plot(x, y_queens, label='Queens')
    plt.plot(x, y_brooklyn, label='Brooklyn')
    plt.plot(x, y_bronx, label='Bronx')

    #format
    plt.xlabel('Month')
    plt.ylabel('Average Death Count')
    plt.title('COVID-19 Death Count by Month in 2021')
    plt.xticks(ticks=range(1, 13))
    plt.legend()
    plt.grid(True)
    plt.show()

elif user_year == "2022":
    #extract month 
    filtered_df_2022['month'] = filtered_df_2022['date_of_interest'].dt.month

    #groups by borough
    manhattan_avg = filtered_df_2022.groupby('month')['MN_DEATH_COUNT'].mean()
    staten_avg = filtered_df_2022.groupby('month')['SI_DEATH_COUNT'].mean()
    queens_avg = filtered_df_2022.groupby('month')['QN_DEATH_COUNT'].mean()
    brooklyn_avg = filtered_df_2022.groupby('month')['BK_DEATH_COUNT'].mean()
    bronx_avg = filtered_df_2022.groupby('month')['BX_DEATH_COUNT'].mean()

    #x and y values
    x = bronx_avg.index
    y_manhattan = manhattan_avg.values
    y_staten = staten_avg.values
    y_queens = queens_avg.values
    y_bronx = bronx_avg.values
    y_brooklyn = brooklyn_avg.values

    #legend
    plt.plot(x, y_manhattan, label='Manhattan')
    plt.plot(x, y_staten, label='Staten Island')
    plt.plot(x, y_queens, label='Queens')
    plt.plot(x, y_brooklyn, label='Brooklyn')
    plt.plot(x, y_bronx, label='Bronx')

    #format
    plt.xlabel('Month')
    plt.ylabel('Average Death Count')
    plt.title('COVID-19 Death Count by Month in 2022')
    plt.xticks(ticks=range(1, 13))
    plt.legend()
    plt.grid(True)
    plt.show()

elif user_year == "2023":
    #extract month 
    filtered_df_2023['month'] = filtered_df_2023['date_of_interest'].dt.month

    #groups by borough
    manhattan_avg = filtered_df_2023.groupby('month')['MN_DEATH_COUNT'].mean()
    staten_avg = filtered_df_2023.groupby('month')['SI_DEATH_COUNT'].mean()
    queens_avg = filtered_df_2023.groupby('month')['QN_DEATH_COUNT'].mean()
    brooklyn_avg = filtered_df_2023.groupby('month')['BK_DEATH_COUNT'].mean()
    bronx_avg = filtered_df_2023.groupby('month')['BX_DEATH_COUNT'].mean()

    #x and y values
    x = bronx_avg.index
    y_manhattan = manhattan_avg.values
    y_staten = staten_avg.values
    y_queens = queens_avg.values
    y_bronx = bronx_avg.values
    y_brooklyn = brooklyn_avg.values

    #legend
    plt.plot(x, y_manhattan, label='Manhattan')
    plt.plot(x, y_staten, label='Staten Island')
    plt.plot(x, y_queens, label='Queens')
    plt.plot(x, y_brooklyn, label='Brooklyn')
    plt.plot(x, y_bronx, label='Bronx')

    #format
    plt.xlabel('Month')
    plt.ylabel('Average Death Count')
    plt.title('COVID-19 Death Count by Month in 2023')
    plt.xticks(ticks=range(1, 13))
    plt.legend()
    plt.grid(True)
    plt.show()

elif user_year == "all":
    #extract month 
    filtered_df_all['month'] = filtered_df_all['date_of_interest'].dt.month

    #groups by borough
    manhattan_avg = filtered_df_all.groupby('month')['MN_DEATH_COUNT'].mean()
    staten_avg = filtered_df_all.groupby('month')['SI_DEATH_COUNT'].mean()
    queens_avg = filtered_df_all.groupby('month')['QN_DEATH_COUNT'].mean()
    brooklyn_avg = filtered_df_all.groupby('month')['BK_DEATH_COUNT'].mean()
    bronx_avg = filtered_df_all.groupby('month')['BX_DEATH_COUNT'].mean()

    #x and y values
    x = bronx_avg.index
    y_manhattan = manhattan_avg.values
    y_staten = staten_avg.values
    y_queens = queens_avg.values
    y_bronx = bronx_avg.values
    y_brooklyn = brooklyn_avg.values

    #legend
    plt.plot(x, y_manhattan, label='Manhattan')
    plt.plot(x, y_staten, label='Staten Island')
    plt.plot(x, y_queens, label='Queens')
    plt.plot(x, y_brooklyn, label='Brooklyn')
    plt.plot(x, y_bronx, label='Bronx')

    #format
    plt.xlabel('Month')
    plt.ylabel('Average Death Count')
    plt.title('COVID-19 Death Count by Month in 2021, 2022, and 2023')
    plt.xticks(ticks=range(1, 13))
    plt.legend()
    plt.grid(True)
    plt.show()

user_income = input("do you want to see the income data? (yes/no) ")
if user_income.lower() == "yes":
    #create dataframe for income
    incomeDF = pd.DataFrame(dictIncome)
    incomeDF.index = ['2021', '2022', '2023', 'Average']
    #display the income data
    print(incomeDF)
    input("would you like to see the average income data visualized? (yes/no) ")
    if user_income.lower() == "yes":
        #visulaizing the average income data
        incomeDF.loc['Average'] = incomeDF.mean()
        incomeDF.plot()
        plt.title('Average Income by Borough (2021-2023)')
        plt.xlabel('Borough')
        plt.ylabel('Income')
        plt.xticks(rotation=45)
        plt.legend(title='Year')
        plt.tight_layout()
        plt.show()



#analysis
'''
The purpose of this code is to analyze COVID-19 death counts in New York City by borough and year to find a corralation between income and death counts.
From the graph we can generalize that Brooklyn and Queens have the highest death counts with Brooklyn being the fourth ranked borough in terms of income
and Queens being the third. As for the Bronx, it maybe viewed as an outlier, its low death counts can be attributed to its population levels being the second to last
only behind Staten Island. This makes it so that its death count is viewed not from an economic lens but from a population one, so the Bronx's average income plays little
to no effects when it comes to its effect on the Bronx's death count number. Manhattan and Staten Island abides by our hypothesis that the higher the income; 
the lower the death count. Furthermore, with the fact that almost all of the hosptials are located in Manhattan, it is no surprise that the borough with 
the most amount of hospitals has the lowest death count. Staten Island, on the other hand, falls into a catagory similar the Bronx, where its low population 
levels skews the death count number to be lower than the other boroughs. In conclusion, the data and subsequent analysis shows that there is a 
correlation between income and death counts, but it would be an oversimplification to say that income is the only factor at play. As mentioned prior, 
the Bronx and Staten Island's death count is a reflection not of income but of population. Additionally, one cannot deny that Manhattan has the greatest 
acceccibility when it comes to healthcare. 
'''