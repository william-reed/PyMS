import csv

"""
Read the CSV files generated from MySQL and create a dict from them
Run with `python csv_to_dict.py >> dict.txt`
"""

with open('us_gateways.csv') as csvfile:
    reader = csv.reader(csvfile)

    carriers = {}
    # 0 is CARRIER
    # 1 is SMS_EMAIL
    # 2 is MMS_EMAIL

    # skip the first header line
    reader.__next__()
    for row in reader:
        name = ''
        if ' (' in row:
            name = row[0].split(' (')[0]
        name = row[0].replace(' ', '_') \
            .replace('(', '') \
            .replace(')', '') \
            .upper()

        carriers[name] = {
            'NAME': row[0],
            'SMS_EMAIL': row[1],
            'MMS_EMAIL': row[2]
        }

    print(carriers)
