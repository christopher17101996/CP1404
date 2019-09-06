"""
Name: Pyae Phyo Thiha Aung
GitHub URL: https://github.com/christopher17101996/CP1404/tree/master/Assignment%201
"""

from tempfile import NamedTemporaryFile
import csv
import shutil

csv_file = 'place.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')
MENU = "Menu:\nL - List places\nA - Add new places\nM - Mark a place as viewed\nQ - Quit"

def main():
    print("Travel Tracker 1.0 - by Pyae Phyo Thiha Aung")
    main_menu()

def main_menu():
    print(MENU)
    menu_choice = input(">>>").upper()
    choices = ["L", "A", "M", "Q"]
    while menu_choice not in choices:
        print("Menu choice is invalid.")
        menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice =="L":
            listPlace()
            main_menu()
        elif menu_choice =="A":
            addPlace()
            main_menu()
        elif menu_choice =="M":
            markVisit()
            main_menu()
    exit("Have a nice day :)")

def listPlace():
    places_file = open(csv_file, 'r')
    places_list_n = places_file.readlines()
    places_list = [i.replace("\n", '') for i in places_list_n]
    places_file.close()
    individual_places_list = []
    for i in range(len(places_list)):
        individual_places_list.append(places_list[i].split(','))
    to_visit_count = 0
    for i in range(len(individual_places_list)):
        if individual_places_list[i][3] == "n":
            to_visit_count += 1
            print("*{}. {:<8} in {:<11} priority {}.".format(i + 1, individual_places_list[i][0], individual_places_list[i][1], individual_places_list[i][2]))
        else:
            print(" {}. {:<8} in {:<11} priority {}.".format(i + 1, individual_places_list[i][0], individual_places_list[i][1], individual_places_list[i][2]))
    if to_visit_count > 0:
        print(" {} places in the list. But you still want to visit {} places.".format(len(individual_places_list), to_visit_count))
    else:
        print(" {} places. No places left to visit. Why not add some more?".format(len(individual_places_list)))
    return individual_places_list

def addPlace():
    new_place = input("Name: ")
    while new_place == "":
        print("Input cannot be blank.")
        new_place = input("Name: ")
    new_country = input("Country: ")
    while new_country == "":
        print("Input cannot be blank.")
        new_country = input("Country: ")
    new_priority = checkPriotiryNumber("Priority: ")
    print("{} in {} (priority {}) added to Travel Tracker".format(new_place, new_country, new_priority))
    add_place = [new_place, new_country, new_priority, "n"]
    with open('place.csv', 'a', newline='') as csvfile:
        writeCSV = csv.writer(csvfile)
        writeCSV.writerow(add_place)
    csvfile.close()

def checkPriotiryNumber(message):
    number = 0
    try:
        number = int(input(message))
        while number <= 0:
            print("Input number must be greater than ZERO")
            number = int(input(message))
    except ValueError:
        print("Please enter number that is greater than ZERO")
        checkPriotiryNumber(message)
    return number

def markVisit():
    individual_places_list = listPlace()
    non_visited_count = 0
    for i in range(len(individual_places_list)):
        if individual_places_list[i][3] == "n":
            non_visited_count += 1
    if non_visited_count == 0:
        print("No unvisited places.")
        main_menu()
    else:
        MSG = "Enter the number of the place to mark as visited."
        print("Enter the number of the place to mark as visited.")
        check_number = checkPriotiryNumber(">>>")
        mark_visit = check_number - 1
        while mark_visit > len(individual_places_list):
            print("There aren't that many places.")
            print(MSG)
            check_number = checkPriotiryNumber(">>>")
            mark_visit = check_number - 1
        while individual_places_list[mark_visit][3] == "v":
            print("You have already visited that place.")
            print(MSG)
            check_number = checkPriotiryNumber(">>>")
            mark_visit = check_number - 1
        else:
            c_name = "v"
            field = [individual_places_list[mark_visit][0], individual_places_list[mark_visit][1], individual_places_list[mark_visit][2], individual_places_list[mark_visit][3]]
            with open(csv_file,'r') as csvfile, tempfile:
                reader = csv.DictReader(csvfile, fieldnames=field)
                writer = csv.DictWriter(tempfile, fieldnames=field)
                for row in reader:
                    if row[individual_places_list[mark_visit][0]] == individual_places_list[mark_visit][0]:
                        row[individual_places_list[mark_visit][3]] = c_name
                    writer.writerow({individual_places_list[mark_visit][0]: row[individual_places_list[mark_visit][0]],
                                    individual_places_list[mark_visit][1]: row[individual_places_list[mark_visit][1]],
                                    individual_places_list[mark_visit][2]: row[individual_places_list[mark_visit][2]],
                                    individual_places_list[mark_visit][3]: row[individual_places_list[mark_visit][3]]})
            shutil.move(tempfile.name, csv_file)
            print("{} in {} is visited.".format(individual_places_list[mark_visit][0], individual_places_list[mark_visit][1]))
        main_menu()

if __name__ == '__main__':
    main()