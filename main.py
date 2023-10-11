#  #Python Loops (ciklai)
# Python has two primitive loop commands:

# while loops
# for loops

# # While loop
# With the while loop we can execute a set of statements as long as a condition is true.

# i = 0
# while i < 10:   # kol
#   print(i)
#   i += 1    # sutrumpinta i = i + 1

# Note: remember to increment i, or else the loop will continue forever.

# # endless loops
# This loop will not allow user to pass empty space as argument, will always wait until something is typed.

# while True:
#     user_input = input("Enter your name: ")
#     if len(user_input) != 0:
#         break
# print(f"You entered {user_input }")

# ----------------

# [18:48] Mindaugas Rudzevičius      
# Task nr.1
# Create a program witch takes 5 different (minmum)  variables containing strings for username and password. 
# The string should look like : "username='', password=''; username='',password='';....etc" 
# Start Endless loop allowing to enter username and password and check ff credentials are correct stop endless loop and print greeting message, 
# otherwise print 'wrong credentials' and ask to enter password and username again. The program should show numbers of times you tried to enter both credentials.

# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, names 'improved password'

username_password = input("Enter 5 usernames: ")
base = {}
patikrinti

