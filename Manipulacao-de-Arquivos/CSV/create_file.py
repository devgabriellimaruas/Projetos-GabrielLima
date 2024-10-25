import csv
import os


data = [
    ["Name", "Age", "City"],
    ["Gabriel", 30, "São Paulo"],
    ["Arthur", 18, "São Caetano do Sul"],
    ["David", 25, "Mauá"],
    ["Geovanna", 63, "Osasco"]
]

path_file = os.path.join("./", "file_csv.csv")

with open(path_file, mode="w", newline="", encoding="utf-8") as file_csv:
    create = csv.writer(file_csv)
    create.writerows(data)
