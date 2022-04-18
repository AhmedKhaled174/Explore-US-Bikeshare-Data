import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyorkcity': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("which city do you want to analyze(chicago, new york city, washington)???").replace(' ','').lower()
        if city not in CITY_DATA:
            print("please write a valid city (chicago, new york city, washington)")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True :
        month = input('which month do you want to display(january or february or march or april or may or june or all)??').replace(' ','').lower()
        months = ["all","january","february","march","april","may","june"]
        if month not in months:
            print("Please type a valid choice")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('choose a day of the week (saturday or sunday or monday or tuesday or wednesday or thursday or friday or all)??? ').replace(' ','').lower()
        week = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "all"]
        if day not in week:
            print("Please enter a valid choice ")
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != "all":
        months =  ["january","february","march","april","may","june"]
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != "all":
        df = df[df['day'] == day.title()]
    
    return df

def disp_rows(df):
    i = 0
    pd.set_option('display.max_columns', None)
    response = input("would you like to display the first 5 rows from the data??(yes or no)").replace(' ','').lower()
    while True:
        if response == 'yes':
            print(df[i:i+5])
            i += 5
            response = input("would you like to display the next 5 rows from the data??(yes or no)").replace(' ','').lower()
        else:
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is {}".format(calendar.month_name[common_month]))
    # display the most common day of week
    common_day = df['day'].mode()[0]
    print("The most common day is {}".format(common_day))
    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most common Start Station is {}".format(common_start))

    # display most commonly used end station

    common_end = df['End Station'].mode()[0]
    print("The most common End Station is {}".format(common_end))
    # display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + '-->' + df['End Station']).mode()[0]
    print('The most common combination is {}'.format(common_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is {} seonds / {} hours".format(total_time,total_time/3600))

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print("The avg travel time is {} seonds / {} hours".format(avg_time,avg_time/3600))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()
    print("The counts of user types is \n {}".format(user_count))

    # Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("The count of gender is \n {}".format(gender_count))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        print("The earliest birth year is {}".format(earliest_year))
        recent_year = int(df['Birth Year'].max())
        print("The most recent year is {}".format(recent_year))
        common_birth = int(df['Birth Year'].mode()[0])
        print("The most common birth year is {}".format(common_birth))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        disp_rows(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.replace(' ','').lower() != 'yes':
            break


if __name__ == "__main__":
	main()
