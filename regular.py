import csv
from pprint import pprint

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pprint(contacts_list)

merged_contacts = defaultdict(list)

for contact in contacts_list:
    name_parts = re.findall(r'\w+', contact[0] + ' ' + contact[1] + ' ' + contact[2])
    lastname, firstname, *surname = name_parts

    phone = re.sub(r'(\+7|8)\s*\(?(\d{3})\)?\s*-?(\d\2})\s*(?:\(?(\w+\.)\s*(\d+)\)?)?',
                   r'+7(\2)\3-\4-\5 \6\7', contact[5])

    key = (lastname, firstname, *surname)
    value = [organization, position, phone, email] = contact[3], contact[4], phone, contact[6]
    merged_contacts[key].append(value)

final_contacts = []
for name, values in merged_contacts.items():
    if len(values) > 1:
        organization, position, phone, email = "", "", "", ""
        for value in values:
            organization = organization or value[0]
            position = position or value[1]
            phone = phone or value[2]
            email = email or value[3]
        final_contacts.append([*name, organization, position, phone, email])
    else:
        final_contacts.append([*name, *values[0]])

pprint(final_contacts)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts)
