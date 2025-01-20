from src.services.data_collect_services import data_collect_service
from src.services.formatted_excel_services import formatted_excel_service

list_items = data_collect_service()
file_name = "Perifericos_da_Kabum"
excel = formatted_excel_service(file_name, list_items)

print(excel)