month_list = [
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

insert = 0
while insert == 0:
    date = input("Date: ")
    if "," in date:
        month, day, year = date.split(" ")
        day = day.replace(",","")
        try:
            day = int(day)
        except ValueError:
            insert = 0
        else:
            if day <= 31 and month in month_list:
                insert = 1
                for i in month_list:
                    if i == month:
                        month = month_list.index(i)+1

    elif "/" in date:
        month, day, year = date.split("/")
        try:
            month = int(month)
            day = int(day)
        except ValueError:
            insert = 0
        else:
            if month <= 12:
                insert = 1

year = year.strip()
if month < 10: month = "0"+str(month)
if day < 10: day = "0"+str(day)

print(year,month,day,sep="-")