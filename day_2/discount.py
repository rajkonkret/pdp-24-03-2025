from datetime import datetime, date, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2025-03-25
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2025-03-25 15:40:02.005203
print(type(time))  # <class 'datetime.datetime'>

print(time.year)  # 2025
print(today.day)  # 25

# tomorrow  = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2025-03-26

formates_data = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data:", formates_data)  # Sformatowana data: 25/03/2025

formated_time = datetime.now().strftime("%H:%M")
print("Sformatowany czas:", formated_time)  # Sformatowany czas: 15:45
print(type(formated_time))  # <class 'str'>

# 3:45 pm
formated_usa_time = datetime.now().strftime("%I:%M %p")
print("Czas USA:", formated_usa_time) # Czas USA: 03:47 PM
print("Czas USA:", formated_usa_time.removeprefix("0")) # Czas USA: 3:48 PM

date_datetime = datetime.now().strptime( "25/03/2025", "%d/%m/%Y")
print(date_datetime) # 2025-03-25 00:00:00