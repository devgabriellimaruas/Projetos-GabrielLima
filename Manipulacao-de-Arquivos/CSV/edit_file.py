import csv


with open("file_csv.csv", mode="r", encoding="utf-8") as file_csv:
    reader = list(csv.reader(file_csv))
    
    for line in reader:
        print(line)

    print()
    
for line in reader:
    if line[0] == "Bob":
        line[1] = "26"

new_row = ["Daniel", "28", "Curitiba"]
reader.append(new_row)

with open("file_csv.csv", mode="w", newline="", encoding="utf-8") as file_csv:
    writer = csv.writer(file_csv)
    writer.writerows(reader)

    for line in reader:
        print(line)