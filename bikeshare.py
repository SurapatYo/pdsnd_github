import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Would you like to see data for Chicago,New York City or Washington')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """
    Refactor Code delete unnecessary Code in a for Loop (The actual changes made don't matter for this project)
    """
    i = 1
    while i>=1 :
        city_input = input("Enter city name: ").title()
        if city_input == 'Chicago'or city_input == 'New York City' or city_input == 'Washington' :
            city = city_input
            i -=1
        else : print("Invalid input please try again")

    # get user input for month (all, january, february, ... , june)
    print('Which month? January, February, March, April, May, or June')
    print('Type "all" for select all months')
    i = 1
    while i>=1 :
        month_input = input().title()
        if month_input == 'All'or month_input == 'January'or month_input == 'February'or month_input == 'March'or month_input == 'April'or month_input == 'May'or month_input == 'June':
            month = month_input
            i -=1
        else : print("Invalid input please try again")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday')
    print('Type "all" for select all days')
    i = 1
    while i>=1 :
        day_input = input().title()
        if day_input == 'All'or day_input == 'Monday'or day_input == 'Tuesday'or day_input == 'Wednesday'or day_input == 'Thursday'or day_input == 'Friday'or day_input == 'Saturday'or day_input == 'Sunday':
            day = day_input
            i -=1
        else : print("Invalid input please try again")

    """
    Refactor Code Including print in input() (The actual changes made don't matter for this project)
    """
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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    """
    Refactor Code Change string formatting (The actual changes made don't matter for this project)
    """
    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week:', most_common_day_of_week)

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most popular start station:', most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most popular end station:', most_common_end_station)

    # display most frequent combination of start station and end station trip
    new = df["End Station"].copy()
    df["routh"]= df["Start Station"].str.cat(new, sep =",")
    most_common_routh = df['routh'].mode()[0]
    station = most_common_routh.split(',',2)
    print("Most popular routh start at {} stop at {}".format(station[0],station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Total_time'] = pd.to_datetime(df['End Time'])-pd.to_datetime(df['Start Time'])
    Total_time = df['Total_time'].sum()
    print('Total time:', Total_time)

    # display mean travel time
    Avg_time = df['Total_time'].mean()
    print('Avg travel time:', Avg_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    if city == 'Washington' :
        print("No gender data for Washington")
        print("No year of birth data for Washington")

    # Display counts of gender
    else :
        user_genders = df['Gender'].value_counts()
        print(user_genders)

    # Display earliest, most recent, and most common year of birth
        max_yob = int(df['Birth Year'].max())
        min_yob = int(df['Birth Year'].min())
        most_yob = int(df['Birth Year'].mode()[0])
        print('Youngest user born in',max_yob)
        print('Oldest user born in',min_yob)
        print('Most common year of birth:',most_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw_data(df):
    df.drop('routh',axis='columns', inplace=True)
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data=='yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue? Enter no to exit: ").lower()
        if view_display == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
