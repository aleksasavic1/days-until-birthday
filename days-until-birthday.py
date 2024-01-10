import time
import datetime


current_time = time.localtime()

current_time1 = f"{current_time.tm_mday}-{current_time.tm_mon}-{current_time.tm_year} \
{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}"
current_time_obj = datetime.datetime.strptime(current_time1, \
                                                "%d-%m-%Y %H:%M:%S")

while True:
    while True:
        try:
            birth_day = int(input("Enter your birth day: "))
            birth_month = int(input("Enter your birth month: "))
            break

        except ValueError:
            print("\nPlease enter a number!")
    try:
        if current_time.tm_mday >= birth_day and current_time.tm_mon >= birth_month:
            if current_time.tm_mday == birth_day and current_time.tm_mon == birth_month:
                print("\nHAPPY BIRTHDAY!!!")
                next_year = current_time.tm_year + 1
                birthday = f"{birth_day}-{birth_month}-{next_year} 00:00:00"
                print(f"\nDate of your next birthday: {birth_day}-{birth_month}-{next_year}")
                    
                birthday_obj = datetime.datetime.strptime(birthday, "%d-%m-%Y %H:%M:%S")

                result = birthday_obj - current_time_obj

                print(f"Your next birthday is in {result.days+1} days!")
                break
            else:
                    
                next_year = current_time.tm_year + 1
                birthday = f"{birth_day}-{birth_month}-{next_year} 00:00:00"
                print(f"\nDate of your next birthday: {birth_day}-{birth_month}-{next_year}")
                    
                birthday = datetime.datetime.strptime(birthday, "%d-%m-%Y %H:%M:%S")

                result = birthday - current_time_obj
                print(f"Your birthday is in {result.days+1} days!")
                break
        else:
            birthday = f"{birth_day}-{birth_month}-{current_time.tm_year} 00:00:00"
            print(f"\nDate of your next birthday: {birth_day}-{birth_month}-{current_time.tm_year}")

            birthday_obj = datetime.datetime.strptime(birthday, "%d-%m-%Y %H:%M:%S")

            result = birthday_obj - current_time_obj
            if result.days + 1 == 1:
                print(f"Your next birthday is in {result.days+1} day!")
                break
            else:
                print(f"Your next birthday is in {result.days+1} days!")
                break
    except Exception:
        print("\nPlease enter a valid date!")

input("\nPress Enter to exit..")
exit()
