import datetime


def my_age():
    birth_day = 9
    birth_month = "September"
    birth_year = 2020

    my_months = {"January": 31, 
            "February": 28, 
            "March": 31, 
            "April": 30, 
            "May": 31, 
            "June": 30, 
            "July": 31,
            "August": 31, 
            "September": 30, 
            "October": 31,
            "November": 30, 
            "December": 31}

    if birth_year % 4 == 0:
        my_months["February"] = 29

    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
  
    year = 0
    months = 0
    while birth_year < current_year:
        year += 1
        birth_year += 1
    print("You are " + str(year) + " years old")

    
    if birth_month == "January":
        months += 1

    if birth_month == "February":
        months += 2

    if birth_month == "March":
        months += 3

    if birth_month == "April":
        months += 4

    if birth_month == "May":
        months += 5

    if birth_month == "June":
        months += 6

    if birth_month == "July":
        months += 7

    if birth_month == "August":
        months += 8

    if birth_month == "September":
        months += 9

    if birth_month == "October":
        months += 10

    if birth_month == "November": 
        months += 11       

    if birth_month == "December":
        months += 12
    
    print("You are " + str(months) + " months old")
my_age()