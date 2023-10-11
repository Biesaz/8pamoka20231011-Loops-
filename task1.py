# [18:48] Mindaugas Rudzevičius      
# Task nr.1
# Create a program witch takes 5 different (minmum)  variables containing strings for username and password. 
# The string should look like : "username='', password=''; username='',password='';....etc" 
# Start Endless loop allowing to enter username and password and check ff credentials are correct stop endless loop and print greeting message, 
# otherwise print 'wrong credentials' and ask to enter password and username again. The program should show numbers of times you tried to enter both credentials.

# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, names 'improved password'

username_password = input("Enter 5 username= , password= ")
base = []
username = "baba"
password = 123
base.append(password)
base.append(username)

for data in base:
    username, password = data.split('=')
    base[username.strip()] = password.strip()
attempts = 0

while True:
    username_password = input("Enter 5 username= , password= ")
    if username_password in base and base[username_password] == password:
        print("Welcome! Access granted.")
        break
    else:
        print("Wrong credentials. Please try again.")
        attempts += 1

print(f"Number of attempts: {attempts}")
