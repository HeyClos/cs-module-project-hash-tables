import csv
cities_per_state = {}

def read_csv_data():
    with open("cities.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            state_id = row['state_id']
            city = row['city']

            if sta