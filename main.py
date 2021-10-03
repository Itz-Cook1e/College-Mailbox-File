# Assignment:
# Write a program to prompt the user to provide a file name
# (use the file that is provided, mbox-short.txt) read through the file, and print the first 50 characters of each line that begins with 'Subject' 
# (line by line). Lastly, provide a count of the number of these lines.
# Your program should include error handling in case the file is not found.

# Get file name
file_name = input('Enter the file name: ')

# Make sure file can be opened
try:
    file_opened = open(file_name)
# Let user know file couldnt be opened
except FileNotFoundError:
    print(f"File '{file_name}' cannot be opened!")
    raise SystemExit

# Line number starter
n = 0

# For loop to print lines starting with 'Subject' and only the first 50 characters of said line
for line in file_opened:
    if line.startswith("Subject"):
        n = n + 1
        print(f'{line[0:49]}')

# Print the ammount of lines that started with 'Subject'
print(f"Lines begin with 'Subject' {n} times.")

# Comment with name, date, and assignment name redacted
