import csv
from User import User


def append_on_csv(info):
    with open('HR-Staff.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7]])


def write_on_csv(info):
    with open('HR-Staff.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7]])


# Reads csv file and convert it to a list
def read_csv(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        csvreader.__next__()
        staff_list = [User(row) for row in csvreader]
        return staff_list
