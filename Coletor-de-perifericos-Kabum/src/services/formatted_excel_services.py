import pandas as pd


def formatted_excel_service(file_name, list_items):
    print("Começando o processo de formatar em excel os dados dos periféricos da Kabum")
    translated_data = [{
        "Categoria": item["classification"],
        "Título": item["title"],
        "Link da Imagem": item["link_image"],
        "Preço Antigo": item["old_price"],
        "Preço": item["price"],
        "Link do produto": item["link_product"]
    } for item in list_items]
    
    df = pd.DataFrame(translated_data)
    
    df.to_excel(f"{file_name}.xlsx", index=False)
    
    return "Arquivo Excel criado com sucesso"