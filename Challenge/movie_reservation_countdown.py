# The movie theater has implemented online reservations through their website. Customers on the seat selection page only have a limited time to finalize their choice.
# Write a Python program that simulates this countdown.
# When mins == 5: Print "Place your reservation soon! 5 minutes remaining.
# When mins == 2: Print "Don't lose your seats! 2 minutes remaining."
# When mins == 0: Print "User timed out."
# Otherwise: Print the number of minutes remaining.


from time import sleep
# Countdown from 10 minutes

mins = 10
while mins >= 0:
    if mins == 5:
        print("Place your reservation soon! 5 minutes remaining.")
    elif mins == 2:
        print("Don't lose your seats! 2 minutes remaining.")
    elif mins == 0:
        print("User timed out.")
    else:
        print(mins)
    mins -= 1   # decrement minutes
    sleep(1)    # pause for 1 second


# 💡 Answer:
# 10
# 9
# 8
# 7
# 6
# Place your reservation soon! 5 minutes remaining.
# 4
# 3
# Don't lose your seats! 2 minutes remaining.
# 1
# User timed out.



