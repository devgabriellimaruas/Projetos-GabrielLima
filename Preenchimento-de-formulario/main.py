from src.services.fill_form import fill_form
from src.services.read_excel import read_excel

df = read_excel()

message = fill_form(df)
print(message)