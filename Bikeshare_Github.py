import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Hello! Let\'s explore some US bikeshare data!''\n')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #assigns the variable 'n' to city, month, and day
city = 'n'
month = 'n'
day = 'n'

    #get user input for city (chicago, new york city, or washington)
while city != 'chicago' and city != 'new york city' and city != 'washington':
    try:
        city = str(input('Which city would you like to view? Chicago, New York City, or Washington?''\n').lower())
    except:
        print('Sorry, that was not a valid option. Please select either Chicago, New York City, or Washington.')
    print('You have selected {}. If this is not correct, please restart.''\n'.format(city.title()))

    #pause display of the data for 1 secs to give user time to review their selection
time.sleep(1)

    #get user input for month (january thru june, or all months). 
while month != 'january' and month != 'february' and month != 'march' and month != 'april'and month != 'may' and month != 'june' and month != 'all':
    try:
        month = str(input('Which month would you like to view data for? Please select a month between January and June, or enter "all"''\n').lower())
    except:
        print('Sorry, that was not a valid option. Please select either January, February, March, April, May, June, or "all".')
    print('You have selected {}. If this not correct, please restart.''\n'.format(month.title()))

    #pause display of the data for 1 secs to give user time to review their selection
time.sleep(1)

    #get user input for day of week (sunday thru saturday). 

while day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday' and day != 'all':
    try:
        day = str(input('Which day would you to view? Please select a day between Sunday and Saturday, or "all?"''\n').lower())
    except:
        print('Sorry, that was not a valid option. Please select either Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or "all".')
    print('You have selected {}. If this not correct, please restart.''\n'.format(day.title()))

    #pause display of the data for 1 secs to give user time to review their selection
time.sleep(1)

    #provides user with a final review of the data they wish to view
print("Great! Filtering data for the city of {}, for the month of {}, and the day of {}."'\n'.format(city.title(), month.title(), day.title()))

    #pause display of the data for 2 secs to give user time to review all of their selections
time.sleep(2)

print  ('Calculating Rental Stats...\n')
start_time = time.time()

    #loads data file into datafram and displays 5 lines of data based on user input    
df = pd.read_csv(CITY_DATA[city])

def rental_stats(df):
 """
    Displays pertinent rental statistics based on user input.

    Returns:
        (str) Start time - Displays most popular starting time.
        (str) Common month - Displays most popular rental month.
        (str) Common start - Displays most popular starting point
        (str) Common stop  - Displays most popular stopping point
        (str) Common route - Displays most popular riding route
        (str) Total time   - Displays total rental time
        (str) Average time - Displays average rental time
    """
    #convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

#extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

    # Find the most popular start time
popular_hour = df['hour'].mode()[0]
print('\nMost Popular Starting Time is:', popular_hour)

#displays most popular month
months = ['January', 'February', 'March', 'April', 'May', 'June']
popular_month = int(df['Start Time'].dt.month.mode())
popular_month = months[popular_month - 1]
print('\nThe most popular month is: {}'.format(popular_month))

#displays most popular starting station
popular_start = df['Start Station'].mode().to_string(index = False)
print('\nThe most popular start station is: {}'.format(popular_start))

#displays most popular ending station
popular_end = df["End Station"].mode().to_string(index = False)
print('\nThe most popular end station is: {}'.format(popular_end))

#displays most popular route
count_trips = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
stations_sorted = count_trips.sort_values(ascending=False)
total_trips = df['Start Station'].count()
print('\nThe Most popular route is: ' + 'Starts at ' + str(stations_sorted.index[0][0]) + ' and ends at ' + str(stations_sorted.index[0][0]))
print()

#displays total travel time
total_duration = df['Trip Duration'].sum()
mins, secs = divmod(total_duration, 60)
hrs, mins = divmod(mins, 60)
print('Total trip duration is (h:m:s): {}:{}:{}''\n'.format(hrs, mins, secs))

#displays mean travel time
average_duration = int(df['Trip Duration'].mean())
mins, secs = divmod(average_duration, 60)
if mins > 60:
    hrs, mins = divmod(mins, 60)
    print('Average trip duration is (h:m:s): {}::{}:{}''\n'.format(hrs, mins, secs))
else:
    print('The average trip duration is (m:s): {}:{}''\n'.format(mins, secs))

    #displays how long it took to retrieve rental data
print('\nThis took %s seconds.' % (time.time() - start_time))
print('-'*40)

    #pause display of the data for 1 secs to give user time to review rental stats
time.sleep(1)

print  ('Calculating User Stats...\n')
start_time = time.time()

def user_stats(df):
    '''Displays statistics on User Types, Gender, and Birth Year (Oldest, youngest, and most common)'''

#display and print counts of user types
print('Displaying stats on User Types:')
user_types = df['User Type'].value_counts()
print(user_types)
print()

    #pause display of the data for 1 secs to give user time to review rental stats
time.sleep(1)

#display counts of gender types
print('Displaying stats on Gender Types:')
try:
    gender_types = df['Gender'].value_counts()
    print(gender_types)
except:
    print('Gender type: Sorry, there is no gender data available for this city')
print()

#display earliest, most recent, and most common year of birth
print('Dsiplaying stats on Birth Years:')
try:
    oldest_year = int(df['Birth Year'].min())
    print('Oldest Year:', oldest_year)
except:
    print('\nOldest year: Sorry, there is no birth year data available for this city.')
try:
    youngest_year = int(df['Birth Year'].max())
    print('\nMost Recent Year:', youngest_year)
except:
    print('\nYoungest year: Sorry, there is no birth year data available for this city.')
try:
    most_common = int(df['Birth Year'].value_counts().idxmax())
    print('\nMost Common Year:', most_common)
except:
    print('\nMost common year: Sorry, there is no birth year data available for this city.')

        #pause display of the data for 1 secs to give user time to review user stats
time.sleep(1)

    #displays how long it took to retrieve their data
print('\nThis took %s seconds.' % (time.time() - start_time))
print('-'*40)

def raw_data():
    head = 0
    tail = 5
    while True:
        raw = (input('\nWould you like to see 5 lines of data for the city you have requested? Enter "yes" or "no".').lower())
        if raw == "yes":
            print(df.head(5))
        more_raw = (input('\nWould you like to see 5 more lines of data? Enter "yes" or "no"').lower())
        head += 5
        tail += 5
        if more_raw == "yes":
            print(df[df.columns[0:-1]].iloc[head:tail])
        if more_raw == "no":
            break
raw_data()

    #added for github project 4-1
    #added for github project 4-2