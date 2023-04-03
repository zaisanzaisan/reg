import csv
import re
from prettytable import PrettyTable

x = PrettyTable()

def make_unique(list_, num1, num2):
    list_.append([i or j for i, j in zip(list_[num1], list_[num2])])
    del list_[num1]
    del list_[num2 - 1]
    return list_

def sort_data(cont_list):
    lst = []
    for column in cont_list[1:]:
        if " " in column[0]:
            fullname = column[0].split()
            for word in range(len(fullname)):
                column[word] = fullname[word]
        elif " " in column[1]:
            fullname = column[1].split()
            for word in range(len(fullname)):
                column[word + 1] = fullname[word]
        lst.append(column)

    lst = make_unique(lst, 1, 3)
    lst = make_unique(lst, 4, 5)
    pattern_phone = r"(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)"
    substitution = r'+7(\4)\8-\11-\14\15\17\18\19\20'

    for el in lst:
        el[5] = re.sub(pattern_phone, substitution, f" {el[5]} ")
    x.field_names = title
    x.add_rows(lst)
    print(x)
    return lst

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        title = contacts_list[0]

    lst_ = sort_data(cont_list=contacts_list)

    with open("phonebook_res.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(lst_)