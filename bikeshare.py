import time
import pandas as pd
import numpy as np
#initializing fixed numbers for dashs to use it between lines
dash = 40
#dict for loading the csv files
CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wn': 'washington.csv' }
#array of months to get the input from users and check if it's here
months = ['jan','feb','mar','april','may','june','all']
#filters to ask the user what type of filter he\she wants
filters = ['month','day','both','none']
#array of days to check for it in case of user enters incorrect input
days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    #getting what city user wants its data
    city = input("Please enter the city you want its data, for Chicago type CH, for New York NY, for Washington WN: ").lower()
    #using while to ensure user enters correct city
    while city not in CITY_DATA.keys():
        city = input("that's invalid city,, type CH for chicago, NY for new york, or WN for washington: ").lower()
    #asking user for what type of filter he\her wants
    filter = input("\nWould you like to filter the data by month, day, both, none? ").lower()
    while filter not in filters:
        filter = input("\nThat's invalid input. Would you like to filter the data by month, day, both, none? ")
    #after getting the filter: if user wants data filtered by month, then day will be 'all' and ask him\her for what month
    #if user wants data filtered by day, then month will be 'all', and ask him\her for what day
    #if user wants data filtered  by both, then ask him\her for both month and day
    #if user wants data with no filter, then month and day will be 'all'
    if filter == 'month':
        month = input('Please enter one month: Jan,Feb,Mar,April,May,June: ').lower()
        #cheking if month is valid
        while month not in months:
            month = input("That's invalid month, please type one of these \nJan \nFeb \nMar \nApril \nMay \nJune:\n").lower()
        day = 'all'
    elif filter == 'day':
        day = input('Please enter one day: Saturday, Sunday, Monday, Tuesday, Wednesday, Tuesday, Friday: ').lower()
        #cheking if day is valid
        while day not in days:
            day = input("That's invalid day, please type one of these \nSaturday \nSunday \nMonday \nTuesday \nWednesday \nTuesday \nFriday:\n").lower()
        month = 'all'
    elif filter == 'both':
        month = input('Please enter one month: Jan,Feb,Mar,April,May,June: ').lower()
        #cheking if month is valid
        while month not in months:
            month = input("That's invalid month, please type one of these \nJan \nFeb \nMar \nApril \nMay \nJune:\n").lower()
        day = input('Please enter one day: Saturday, Sunday, Monday, Tuesday, Wednesday, Tuesday, Friday: ').lower()
        #cheking if day is valid
        while day not in days:
            day = input("That's invalid day, please type one of these \nSaturday \nSunday \nMonday \nTuesday \nWednesday \nTuesday \nFriday:\n").lower()
    elif filter == 'none':
        month = 'all'
        day = 'all'

    return city, month, day
def load_data(city, month, day):

    #loading data of city in df
    df = pd.read_csv(CITY_DATA[city])

    #Convering 'Start Time' cloumn into datetime formula
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Creating new columns for day week, hour, and month as names
    df['Month Name'] = df['Start Time'].dt.month_name()
    df['Day Name'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    #creating new column for tirp using end station and start station
    df['Trip'] = df['Start Station'] + '-TO-' + df['End Station']
    #Filterring the data by month, if month = all, there is no filter,,  otherwise filter by month
    if month != 'all':
        #Using .str.startswith method to ensure the name of month and days
        df = df[df['Month Name'].str.startswith(month.title())]
    #Filterring the data by day, if day = all, there is no filter,, otherwise filter by day
    if day != 'all':
        df = df[df['Day Name'].str.startswith(day.title())]
    return df

    print('-'*dash)
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Getting the common month
    common_month = df['Month Name'].mode()[0]
    #Getting the counts of this common month
    month_counts = df['Month Name'].value_counts()
    counts = month_counts[common_month]
    print('The most common month people use bikes is {}, and it counts {} time'.format(common_month , counts))
    #Getting the common day of week
    common_day = df['Day Name'].mode()[0]
    #Getting the counts of this common day
    day_counts = df['Day Name'].value_counts()
    counts = day_counts[common_day]
    print('The most common day people use bikes is {}, and it counts {} time'.format(common_day , counts))
    #Getting the common hour
    common_hour = df['Hour'].mode()[0]
    #Getting the counts of this Hour
    hour_counts = df['Hour'].value_counts()
    counts = hour_counts[common_hour]
    print('The most common hour people use bikes is {}, and it counts {} time'.format(common_hour , counts))
    #Displaying the time this process takes
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*dash)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Calulating the most common Start station
    common_start_station = df['Start Station'].mode()[0]
    #Calulating the counts of the most common Start station
    start_counts = df['Start Station'].value_counts()[common_start_station]
    print('The most common start station is {} and it counts {} time'.format(common_start_station, start_counts))

    #Calulating the most common End station
    common_end_station = df['End Station'].mode()[0]
    #Calulating the counts of the most common End station
    end_counts = df['End Station'].value_counts()[common_end_station]
    print('The most common end station is {} and it counts {} time'.format(common_end_station, end_counts))


    #Calulating the most common trip
    common_trip = df['Trip'].mode()[0]
    #Calulating the counts of the most common trip
    trip_counts = df['Trip'].value_counts()[common_trip]
    print('The most common trip is {}, and it counts {} time'.format(common_trip, trip_counts))

    #Calulating the time of this process
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*dash)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    #Convering time from seconds to minutes
    df['Trip Duration'] /= 60

    #Calulating the total time
    total_time_minutes = df['Trip Duration'].sum()

    #Converting it to hours to display it
    total_time_hours = total_time_minutes / 60
    print('The total travel time is {} hour'.format(total_time_hours))


    #Calulating the mean time by minutes
    mean = total_time_minutes / len(df)
    print('Average time per trip is {} minute'.format(mean))


    #Calulating the time of this process
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*dash)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Displaying counts of user types
    user_type = df['User Type'].value_counts().to_frame()
    print('User types and thier count:\n{}'.format(user_type))


    #Displaying counts of gender and statistics about birth year
    #,, I will use (try and except) as washington does not have gender and birth year.
    try:
            gender_type = df['Gender'].value_counts().to_frame()
            print('Gender types and thier count:\n{}'.format(gender_type))

            #statistics about birth year- using it as int to remove the decimal point
            earliest = int(df['Birth Year'].min())
            print('The oldest person was born in {}'.format(earliest))

            most_recent = int(df['Birth Year'].max())
            print('The youngest person was born in {}'.format(most_recent))

            common_birth_year = int(df['Birth Year'].mode())
            print('The most common birth year is {}'.format(common_birth_year))
    except KeyError:
        print('Washington has no data for gender and birth year')


    #Displaying the time this process takes
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*dash)
def display_raw_data(df):
    #Asking user if he\she wants to display raw data
    raw = input('Would you like to display raw data? ').lower()

    #Ensuring of the input(yes,no)
    while raw != 'yes' and raw != 'no':
        raw = input('Invalid input would you like to display raw data before statistics? enter yes or no: ').lower()
    if raw == 'yes':
        #Asking user if he\she wants to display all data or brief
        brief = input('Would you like to display all the data or just brief? type all or brief: ').lower()
        while brief != 'all' and brief != 'brief':
            brief = input('Invalid input enter all for display all data, or brief for brief of data: ').lower()
        if brief == 'all':
            print(df.to_string())
        else:
            #Initializing answer = yes to enter the while loop
            #Initializing start_loc = 0 before the loop
            answer = 'yes'
            start_loc = 0
            while answer == 'yes':
                #Printing the data: first iteration it will view the first 5 cloumns
                #,, second iteration will view the second 5 columns,,,3rd iteration the 3rd 5 columns
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                answer = input('Would you like to show more 5 columns? ').lower()

                #Ensuring the answer
                while answer != 'yes' and answer != 'no':
                    answer = input('Invalid input would you like to show more 5 columns? Please type yes or no: ').lower()

    print('-'*dash)
def main():
    while True:
        #Filterring the data
        city, month, day = get_filters()
        #Loading the data
        df = load_data(city, month, day)

        #First statistics
        time_stats(df)
        #Second statistics
        station_stats(df)

        #Third statistics
        trip_duration_stats(df)
        #forth statistics
        user_stats(df)
        #fifth statistics
        display_raw_data(df)

        print('_'*dash)


        #Asking if user wants to exit.
        restart = input('Would you like to exit? Enter yes or no: ').lower()
        #In case of user enters anything insted of yes or no
        while (restart != 'yes') and (restart != 'no'):
            restart = input('In valid input would you like to exit? Enter yes or no: ').lower()

        if restart == 'yes':
            break


if __name__ == "__main__":
	main()
