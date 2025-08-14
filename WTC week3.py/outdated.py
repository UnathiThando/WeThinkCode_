from dateutil import parser
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def get_date():
    date = input("Enter the date: ").strip()
    try:
        date_object = parser.parse(date)
        if any(month in date for month in months) or '/' in date:
            print(date_object.strftime("%Y-%m-%d"))
        else:
            print("Invalid format: Month name or numeric month required.")
    except ValueError:
        print("Invalid date format.")
get_date()
