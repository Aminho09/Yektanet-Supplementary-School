import math


def data_to_string(data, table_length: list):
    address_is_more80 = False
    split_address = []
    res = '|'
    for i in range(math.floor((table_length[0] - len(str(data.id))) / 2)):
        res += ' '
    res += str(data.id)
    for i in range(math.ceil((table_length[0] - len(str(data.id))) / 2)):
        res += ' '
    res += '|'
    for i in range(math.floor((table_length[1] - len(data.first_name)) / 2)):
        res += ' '
    res += str(data.first_name)
    for i in range(math.ceil((table_length[1] - len(data.first_name)) / 2)):
        res += ' '
    res += '|'
    for i in range(math.floor((table_length[2] - len(data.last_name)) / 2)):
        res += ' '
    res += str(data.last_name)
    for i in range(math.ceil((table_length[2] - len(data.last_name)) / 2)):
        res += ' '
    res += '|'
    address_length = len(data.address)
    if address_length > 80:
        address_is_more80 = True
        split_address = split_by_comma(data.address)
        data.address = split_address[0]
    for i in range(math.floor((table_length[3] - len(data.address)) / 2)):
        res += ' '
    res += str(data.address)
    for i in range(math.ceil((table_length[3] - len(data.address)) / 2)):
        res += ' '
    res += '|'
    for i in range(math.floor((table_length[4] - len(data.phone_number)) / 2)):
        res += ' '
    res += str(data.phone_number)
    for i in range(math.ceil((table_length[4] - len(data.phone_number)) / 2)):
        res += ' '
    res += '|'
    for i in range(math.floor((table_length[5] - len(data.country)) / 2)):
        res += ' '
    res += str(data.country)
    for i in range(math.ceil((table_length[5] - len(data.country)) / 2)):
        res += ' '
    res += '|'
    for i in range(math.floor((table_length[6] - len(str(data.age))) / 2)):
        res += ' '
    res += str(data.age)
    for i in range(math.ceil((table_length[6] - len(str(data.age))) / 2)):
        res += ' '
    res += '|'
    for i in range(math.floor((table_length[7] - len('-'.join(data.skills))) / 2)):
        res += ' '
    res += str('-'.join(data.skills))
    for i in range(math.ceil((table_length[7] - len('-'.join(data.skills))) / 2)):
        res += ' '
    res += '|'
    if address_is_more80:
        res += '\n' + more_80(split_address[1], table_length)
    return res


def split_by_comma(string: str):
    temp = string.split()
    result = ['', '']
    flag = True
    for item in temp:
        if len(result[0] + ' ' + item) <= 80 and flag:
            result[0] += ' ' + item
        else:
            result[1] += ' ' + item
            flag = False

    return result


def more_80(address, table_length: list):
    address_is_more80 = False
    split_address = []
    res = '|'
    for i in range(table_length[0]):
        res += ' '
    res += '|'
    for i in range(table_length[1]):
        res += ' '
    res += '|'
    for i in range(table_length[2]):
        res += ' '
    res += '|'
    if len(address) > 80:
        address_is_more80 = True
        split_address = split_by_comma(address)
        address = split_address[0]
    for i in range(math.floor((table_length[3] - len(address)) / 2)):
        res += ' '
    res += str(address)
    for i in range(math.ceil((table_length[3] - len(address)) / 2)):
        res += ' '
    res += '|'
    for i in range(table_length[4]):
        res += ' '
    res += '|'
    for i in range(table_length[5]):
        res += ' '
    res += '|'
    for i in range(table_length[6]):
        res += ' '
    res += '|'
    for i in range(table_length[7]):
        res += ' '
    res += '|'
    if address_is_more80:
        res += '\n' + more_80(split_address[1], table_length)
    return res


def create_table(data, title=True):
    result = ''
    table_length = [8, 10, 10, 7, 20, 7, 7, 6]
    is80 = False
    for i in range(len(data)):
        address_length = len(data[i].address)
        if address_length > 80:
            table_length[3] = 80
            is80 = True
        if len(data[i].first_name) > table_length[1]:
            table_length[1] = len(data[i].first_name)
        if len(data[i].last_name) > table_length[2]:
            table_length[2] = len(data[i].last_name)
        if len(data[i].address) > table_length[3] and not is80:
            table_length[3] = len(data[i].address)
        if len(data[i].country) > table_length[5]:
            table_length[5] = len(data[i].country)
        string_skills = '-'.join(data[i].skills)
        if len(string_skills) > table_length[7]:
            table_length[7] = len(string_skills)
    table_length[1] += 4
    table_length[2] += 4
    table_length[3] += 4
    table_length[5] += 4
    table_length[7] += 4
    row_separator = ''
    for i in range(
            table_length[0] + table_length[1] + table_length[2] + table_length[3] + table_length[4] + table_length[5] +
            table_length[6] + table_length[7] + 9):
        row_separator += '-'
    if title:
        result += row_separator + '\n'
        first_row = '|'
        for i in range(math.floor((table_length[0] - len('ID')) / 2)):
            first_row += ' '
        first_row += 'ID'
        for i in range(math.ceil((table_length[0] - len('ID')) / 2)):
            first_row += ' '
        first_row += '|'
        for i in range(math.floor((table_length[1] - len('First Name')) / 2)):
            first_row += ' '
        first_row += 'First Name'
        for i in range(math.ceil((table_length[1] - len('First Name')) / 2)):
            first_row += ' '
        first_row += '|'
        for i in range(math.floor((table_length[2] - len('Last Name')) / 2)):
            first_row += ' '
        first_row += 'Last Name'
        for i in range(math.ceil((table_length[2] - len('Last Name')) / 2)):
            first_row += ' '
        first_row += '|'
        for i in range(math.floor((table_length[3] - len('Address')) / 2)):
            first_row += ' '
        first_row += 'Address'
        for i in range(math.ceil((table_length[3] - len('Address')) / 2)):
            first_row += ' '
        first_row += '|'
        for i in range(math.floor((table_length[4] - len('Phone Number')) / 2)):
            first_row += ' '
        first_row += 'Phone Number'
        for i in range(math.ceil((table_length[4] - len('Phone Number')) / 2)):
            first_row += ' '
        first_row += '|'
        for i in range(math.floor((table_length[5] - len('Country')) / 2)):
            first_row += ' '
        first_row += 'Country'
        for i in range(math.ceil((table_length[5] - len('Country')) / 2)):
            first_row += ' '
        first_row += '|'
        for i in range(math.floor((table_length[6] - len(str('Age'))) / 2)):
            first_row += ' '
        first_row += 'Age'
        for i in range(math.ceil((table_length[6] - len('Age')) / 2)):
            first_row += ' '
        first_row += '|'
        for i in range(math.floor((table_length[7] - len('Skills')) / 2)):
            first_row += ' '
        first_row += 'Skills'
        for i in range(math.ceil((table_length[7] - len('Skills')) / 2)):
            first_row += ' '
        first_row += '|'
        result += first_row + '\n'
    for i in range(len(data)):
        result += row_separator + '\n' + data_to_string(data[i], table_length) + '\n'
    result += row_separator
    return result
