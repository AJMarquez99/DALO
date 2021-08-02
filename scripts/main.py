import sys
import data_management as dm
import data_parser as dp
import data_import as di

def get_list():
    the_list = []

    n = int(input("Enter how many items you are inputting : "))

    for i in range(0, n):
        item = input("Enter Company 2-5 letter symbol: ")
        the_list.append(item.upper())

    answer = str(input("Is the list correct? (Y or N) : "))

    if answer == "N" or answer == "n":
        print("Run the script again an start over then!")
        sys.exit()
    else:
        return the_list

mylist = get_list()
print(mylist)
