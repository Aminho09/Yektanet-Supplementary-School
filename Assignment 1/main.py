from csv_reader_writer import *
from MemoryClient import *

staff_list = read_csv('HR-Staff.csv')

while True:
    command = input('(P)rint all users, (ID) search, (Sk)ill search, (S)et a new data, (M)erge another csv file,'
                    ' (E)xit the program\nEnter your command: ')
    command = command.upper()

    if command == 'P':
        print(create_table(staff_list))

    elif command == 'ID':
        input_id = input('Enter the ID ((Cancel) any time): ')
        if input_id == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        found_user = find_user_by_id(int(input_id), staff_list)
        if found_user is None:
            print(f"There isn't a user with the Id {int(input_id)}")
            print('============================================================')
        else:
            print(found_user)

    elif command == 'SK':
        input_skill = input('Enter the skill ((Cancel) any time): ')
        if input_skill == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        skill_user_finder(input_skill, staff_list)

    elif command == 'S':
        user_info = []
        print('(Cancel) any time')
        ID = input('ID: ')
        if ID == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        ID_is_exist = find_user_by_id(int(ID), staff_list)
        replace_or_skip = None
        if ID_is_exist is not None:
            replace_or_skip = input(f'This ID already exists:\n{ID_is_exist}\nDo want to (R)eplace or (S)kip?: ')
            replace_or_skip = replace_or_skip.upper()
            while replace_or_skip != 'S' and replace_or_skip != 'R':
                print("The command doesn't exist!")
                replace_or_skip = input(f'This ID already exists:\n{ID_is_exist}\nDo want to (R)eplace or (S)kip?: ')
                replace_or_skip = replace_or_skip.upper()
            if replace_or_skip == 'S':
                print('Data Skipped')
                print('============================================================')
                continue
        user_info.append(ID)
        first_name = input('First Name: ')
        if first_name == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        else:
            user_info.append(first_name)
        last_name = input('Last Name: ')
        if last_name == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        else:
            user_info.append(last_name)
        address = input('Address: ')
        if address == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        else:
            user_info.append(address)
        phone_number = input('Phone Number: ')
        if phone_number == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        else:
            user_info.append(phone_number)
        country = input('Country: ')
        if country == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        else:
            user_info.append(country)
        age = input('Age: ')
        if age == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        else:
            user_info.append(age)
        skills = input('Skills (Separate skills with "-") : ')
        if skills == 'Cancel':
            print('Operation canceled')
            print('============================================================')
            continue
        else:
            user_info.append(skills)
        if replace_or_skip == 'R':
            write_on_csv(['ID', 'First Name', 'Last Name', 'Address', 'Phone Number', 'Country', 'Age', 'Skills'])
            for i in range(len(staff_list)):
                if staff_list[i].id == int(ID):
                    append_on_csv(user_info)
                    staff_list[i] = User(user_info)
                else:
                    append_on_csv(staff_list[i].to_list())
        else:
            append_on_csv(user_info)
            staff_list.append(User(user_info))
        print('The data set successfully')
        print('============================================================')

    elif command == 'M':
        filename = input('Enter the name of the .csv file: ') + '.csv'
        new_staffs = read_csv(filename)
        skip_or_replace_all = 0
        for item in new_staffs:
            ID_is_exist = find_user_by_id(item.id, staff_list)
            if ID_is_exist is not None:
                if skip_or_replace_all == 0:
                    replace_or_skip = input(f'This ID already exists:\n{ID_is_exist}\n'
                                            f'Do want to (R)eplace or (S)kip or (Replace all) or (Skip all)?: ')
                    replace_or_skip = replace_or_skip.upper()
                    while replace_or_skip != 'S' and replace_or_skip != 'R' and replace_or_skip != 'REPLACE ALL' \
                            and replace_or_skip != 'SKIP ALL':
                        print("The command doesn't exist!")
                        replace_or_skip = input(f'This ID already exists:\n{ID_is_exist}\n'
                                                f'Do want to (R)eplace or (S)kip? or (Replace all) or (Skip all): ')
                        replace_or_skip = replace_or_skip.upper()
                    if replace_or_skip == 'REPLACE ALL':
                        skip_or_replace_all = 2
                    elif replace_or_skip == 'SKIP ALL':
                        skip_or_replace_all = 1
                    elif replace_or_skip == 'S':
                        print('Data Skipped')
                        print('============================================================')
                        continue
                    else:
                        write_on_csv(
                            ['ID', 'First Name', 'Last Name', 'Address', 'Phone Number', 'Country', 'Age', 'Skills'])
                        for i in range(len(staff_list)):
                            if staff_list[i].id == item.id:
                                append_on_csv(item.to_list())
                                staff_list[i] = item
                            else:
                                append_on_csv(staff_list[i].to_list())
                if skip_or_replace_all == 1:
                    break
                if skip_or_replace_all == 2:
                    write_on_csv(
                        ['ID', 'First Name', 'Last Name', 'Address', 'Phone Number', 'Country', 'Age', 'Skills'])
                    for i in range(len(staff_list)):
                        if staff_list[i].id == item.id:
                            append_on_csv(item.to_list())
                            staff_list[i] = item
                        else:
                            append_on_csv(staff_list[i].to_list())
            else:
                append_on_csv(item.to_list())
                staff_list.append(item)
        print('Merging successfully done!')
        print('============================================================')

    elif command == 'E':
        break
    else:
        print('Invalid Command !')
        print('============================================================')
