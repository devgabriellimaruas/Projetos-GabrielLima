import csv
import os

path_file = "file_csv.csv"

with open(path_file, mode="r", encoding="utf-8") as file_csv:
    reader = list(csv.reader(file_csv))
    
if reader:
    deleted_line = reader.pop()
    
    with open(path_file, mode="w", newline="", encoding="utf-8") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(reader)
    
    print("Linha excluída:", deleted_line)
    
    if not reader:
        os.remove(path_file)
        print(f"O arquivo {path_file} foi excluído porque não há mais linhas.")
else:
    os.remove(path_file)
    print(f"O arquivo {path_file} foi excluído porque não há mais linhas.")
