import csv
 
data = []

with open("archive_sorted.csv" , "r") as f:
    a = csv.reader(f)
    for row in a:
        data.append(row)


headers = data[0]
planet_data = data[1:]


for d in planet_data:
    d[2]=d[2].lower()


planet_data.sort(key=lambda planet_data : planet_data[2])


with open("archive_dataset_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

#remove blank lines
with open('archive_dataset_sorted.csv') as input, open('archive_dataset_sorted1.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)