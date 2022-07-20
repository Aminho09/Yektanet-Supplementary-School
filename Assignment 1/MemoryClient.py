from TablePrinter import create_table


def find_user_by_id(identity, staff_list):
    client_dictionary = {item.id: item for item in staff_list}
    return client_dictionary.get(identity)


def skill_user_finder(request, staff_list):
    flag = True
    result = []
    for item in staff_list:
        if request in item.skills:
            # print(item)
            result.append(item)
            flag = False
    if flag:
        print(f"There isn't any user having {request} skill")
        print('============================================================')
    else:
        print(create_table(result))
