"""
Replace the contents of this module docstring with your own details
Name:Xing Jiale
Date started:08/08/2020
GitHub URL:https://github.com/JialeXing/Assignment1/tree/master
"""


def main():
    print("Travel Tracker 1.0 - by <Xing Jiale>")

    username=input("The name of the user")
    if username.isalpha() :
        print("Welcome",username)
    elif username==" ":
        print("The input allow alpha only and cant be blank")
        username = input("The name of the user").upper()
    else:
        print("The input allow alpha only and cant be blank")
        username = input("The name of the user").upper()
    in_file = open('places.csv', 'r+')
    places = in_file.readlines()
    print('{} places loaded'.format(len(places)))

    while True:
        print("Menu:")
        print("L - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n")
        menu=input(">>>").upper()
        if menu == "L" or menu == "l":
            list_place(places)

        elif menu=="A" or menu=="a":
            add_place(places)

        elif menu=="M" or menu=="m":
            mark_place(places)

        elif menu=="Q" or menu=="q":
            exit()

        else:
            print("Invaild choice")

def list_place(places):



    import csv
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        data = sorted(reader, key=lambda row: (row[3], (int(row[2]))))
        count = 0
        visit = sum(1 for row in data)
        want = 0
        for row in data:
            if row[3] == 'n':
                want = want + 1
            count = count + 1
            unvisit = row[3].replace('n', '*').replace('v', ' ')
            print(unvisit, '{:>1}'.format(count), '{:>0}'.format('.'), '{:<10}'.format(row[0]), "in",
                  '{:<20}'.format(row[1]), "Priority", '{:<10}'.format(row[2]))
        if want  == 0:
            print(visit , "Places you want to visit, No places left to visit. ")
        else:
            print(visit , "Places you want to visit, you still have",want, "places never visit")

    csvFile.close()


def add_place(places):
    import csv
    place_name=input("Input a name of place: ")

    if place_name.isalpha():
        print("You want to visit ", place_name)
    elif place_name==" ":
        print("The input allow alpha only and cant be blank")
        place_name = input("Input a name of place: ").upper()
    else:
        print("The input allow alpha only and cant be blank")
        place_name = input("Input a name of place: ").upper()

    country=input("This place in whitch country: ")
    if country.isalpha():
        print(place_name," is in ",country)
    elif country==" ":
        print("The input allow alpha only and cant be blank")
        country = input("This place in whitch country: ").upper()
    else:
        print("The input allow alpha only and cant be blank")
        country=input("This place in whitch country: ").upper()

    while True:
        priority=input("Priority: ")
        try:
            number= int(priority)
            if number<=0:
                raise Exception
            break
        except ValueError:
            print("Invalid input! Please enter a number")
        except Exception:
            print('Number must be >0')

    n="n"
    newplace=[place_name ,country,priority ,n]
    with open('places.csv','a',newline='') as csvFile:
        writer=csv.writer(csvFile)
        writer.writerow(newplace)
    print(place_name, " in ", country, " Priority ", priority, "Automatically classified as n ")
    csvFile .close()


def mark_place(places):
    import csv
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        data = sorted(reader, key=lambda row: (row[3], (int(row[2]))))

    while True:
        try:
            placenum = int(input("Please choose place to mark"))
            if placenum > sum(1 for row in data):
                print("Invaild! Enter a correct number")
                continue
            elif placenum<=0:
                print('Number must be >0')
                continue
        except ValueError:
                print("Invalid input! Please enter a number")
                continue
        else:
            break

    with open('places.csv', 'w', newline='') as csvFile1:
        writer = csv.writer(csvFile1)
        num = 0
        for row in data:
            num = num + 1
            if num == placenum:
                if row[3] == "v":
                    print("Place is already visited")
                else:
                    row[3] = "v"
                    print(row[0], "in", row[1], "is visited")

            writer.writerow(row)

    csvFile.close()
    csvFile1.close()



main()




