i = 1
while i>=1 :
    city_input = input("Enter city name: ").title()
    if city_input == 'Chicago'or city_input == 'New York City' or city_input == 'Washington' :
        city = city_input
        i -=1
    else : print("noo")


i = 1
while i>=1 :
    month_input = input("Enter month name: ").title()
    if month_input == 'All'or month_input == 'January'or month_input == 'February'or month_input == 'March'or month_input == 'April'or month_input == 'May'or month_input == 'June':
        month = month_input
        i -=1
    else : print("nooooooooo")

# get user input for day of week (all, monday, tuesday, ... sunday)
i = 1
while i>=1 :
    day_input = input("Enter day name: ").title()
    if day_input == 'All'or day_input == 'Monday'or day_input == 'Tuesday'or day_input == 'Wednesday'or day_input == 'Thursday'or day_input == 'Friday'or day_input == 'Saturday'or day_input == 'Sunday':
        day = day_input
        i -=1
    else : print("nooooooooo")

print(city)
print(month)
print(day)
