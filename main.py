#aaronleishman.com
# This script saves data to a file without "\n" character at the end of the line
# if the file has already been created the file will be overriden!!

filename = input('Enter the file name you would like to create: ')

data = input('Enter the data you would like to save in ' + filename + ' ')

with open(filename, "w") as f:
    f.write(data)

print('Finished!')
