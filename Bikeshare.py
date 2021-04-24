import pandas as pd
import numpy as np
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
        
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input = input('Write down your choosen city name: chicago, new york city, or washington. \n')
        
    while city_input not in CITY_DATA.keys(): 
        print('Please write the city name again from the given list:')
        city_input = input('Type here:')
    else:
        city = city_input
        print('-'*60)
        print("Now we are exploring the data of {}.".format(city).title())
        print('-'*60)
        
    # get user filter preference by month, day, both, no filter
    print('Please choose your filter preferences!')
    month = "all"
    day = "all"
    month_ls = ['January', 'February', 'March', 'April', 'May', 'June']
    day_ls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    mth_d_in = input('Please type the filter letter as below:\n (m:month, d:day, b:both, or q:no filter) \n')
    
    while mth_d_in not in ['m','d','b','q']:
        print('Please enter the correct filter letter again:')
        mth_d_in = input('Type here:').lower()
    else:
    # get user input for month (january, february, ... , june)
        if mth_d_in == "m" or mth_d_in == "b":
            mth_in = input('which mounth?\n Please enter your target month/s from this list:\n (January, February, March, April, May, June) \n').title()
            while mth_in not in month_ls:
                print('Please choose from the month list again:')
                mth_in = input('Type here:').title()
            else:
                month = mth_in
                print('-'*40)
                print("You have chosen to filter by {}.".format(month))
                print('-'*40)
                
    # get user input for day (monday, tuesday,...) 
        if mth_d_in == "d" or mth_d_in == "b":
            dy_in = input('which day?\n Please enter your target day from this list:\n (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) \n').title()
            while dy_in not in day_ls:
                print('Please choose from the day list again:')
                dy_in = input('Type here:').title()
            else:
                day = dy_in
                print("You have chosen to filter by {}.".format(day))
                print('-'*40)
                
    # get user input for the case of no month or day filters       
        elif mth_d_in == "q":
            month = "all"
            day = "all"
            print("You have chosen no filter.")
            print('-'*40)

    print('You have filtered your data by;\n city:{}, month:{}, day:{}\n'.format(city, month, day))        
    return (city, month, day)
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
    df= pd.read_csv(CITY_DATA[city])
    
    #create column for month, day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()    
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #get the filtered data frame
    if month != 'all':
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    #if month == 'all':
    common_month = df['Month'].value_counts().idxmax()  
    print('The most common month is:', common_month, '\n')

    # display the most common day of week
    #if day == 'all':
    print("The most common day of the week is:", df['day_of_week'].value_counts().idxmax(), '\n')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('most common start hour is:' , df['hour'].value_counts().idxmax())
    
    print('-' *40)
    print("\nThis took %s seconds."  % (time.time() - start_time))
    print('-' *40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common used start station is:", df['Start Station'].value_counts().idxmax(), '\n')

    # display most commonly used end station
    print("The most common used end station is:", df['End Station'].value_counts().idxmax(), '\n')

    # display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + df['End Station']
    print("The most frequent combination trip is:", df['start_end_station'].value_counts().idxmax(), '\n')
    
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is:", df['Trip Duration'].sum() ,'min \n')

    # display mean travel time
    print("The mean travel time is:", df['Trip Duration'].mean(),'min \n')
    
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if "User Type" in df:
        print("User Types are:\n", df["User Type"].value_counts() ,'\n')
    else:
        print ("No Information available for User's types.\n")
        
    # Display counts of gender
    if "Gender" in df:
        print("User's Gender are as following:\n", df["Gender"].value_counts() ,'\n')
    else:
        print ( "No Information available for User's gender.\n")
        
    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("User's most common year of birth is:\n", int(df["Birth Year"].value_counts().idxmax()) ,'\n')
        print('The oldest user birth date:\n', int(df["Birth Year"].min()) ,'\n')
        print('The youngest user birth date:\n', int(df["Birth Year"].max()),'\n')
    else:
        print ( "No Information available for User's birth Year.\n")
    
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(): #check raw data for the three cities option
    city = input('Write down your choosen city name: chicago, new york city, washington.\n')    
    while city not in CITY_DATA.keys(): 
        print('Please write the city name again from the given list:')
        city = input('Type here:')
    else:
        df = pd.read_csv(CITY_DATA[city])
        while True:
            print(df.head())
            print('\nWould you like to explore more rows?')
            check = input("Please Enter:\n y: Yes or n: No\n")
            if check.lower() == "n":
                break     
def action(): #check user's next action after performing data descriptive analysis   
    while True:
        print('\n What would you like to do next?')
        action = (input('\n Please enter the action number:\n 1:Restart\n 2:Explore Raw Data\n 3:Exit\n'))
        if action == "1":
            main()
        elif action == "2":
            print("Let's explore our Raw Data!")
            raw_data()
        else:
            break                        
def main():
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        action()           
if __name__ == "__main__":
	main()


