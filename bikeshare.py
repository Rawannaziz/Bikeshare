import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Name of City?\n').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input (" please choose between chicago, new york city or washington: ").lower()
   
      
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input('Name of month you would like to filter by?\n').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Please choose a month: january, february, march, april, may, june or all?\n').lower()
     

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input('Name of day?\n').lower()
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednsday', 'thursday', 'friday', 'saturday']:
        day = input('Input invalid. please choose a day?\n').lower()


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
    #load file 
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of week from Start Time to creat new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
    
       #filter by month 
       df = df[df['month'] == month]

    #filter by day of week 
    if day != 'all':

      df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    print('The Most Common Month:', common_month)


    # TO DO: display the most common day of week
    
    common_day = df['day_of_week'].mode()[0]
    print('The Most Common Day of Week:', common_day)
    
    


    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    start_station = df['Start Station'].value_counts().idxmax()
    print('The Most Commonly Used Start Station:', start_station)


    # TO DO: display most commonly used end station
    
    end_station = df['End Station'].value_counts().idxmax()
    print('\nThe Most Commonly Used End Station:', end_station)


    # TO DO: display most frequent combination of start station and end station trip
    
    comb_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe Most Commonly Used Combination of Start Station and End Station Trip:', start_station, " & ", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = sum(df['Trip Duration'])
    print('Total Travel Time:', total_travel_time/86400, "Days")


    # TO DO: display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time/60, "Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('Types of User:\n', user_types)


    # TO DO: Display counts of gender
    
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    except KeyError:
        print("\nGender Types: \nNo data..")


    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:', earliest_year)
    except KeyError:
        print("\nEarliest Year: \nNo data.")
    
    try:
        most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year:', most_recent_year)
    except KeyError:
        print("\nMost Recent Year: \nNo data.")
        
    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', most_common_year)
    except KeyError:
        print("\nMost Common Year: \nNo data.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    """Displays data of filteration. 5 rows will be added in each press"""
    print('press enter to see row data, press no to skip')
    x = 0
    while (input() != 'no'):
        x = x+5
        print(df.head(x))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
