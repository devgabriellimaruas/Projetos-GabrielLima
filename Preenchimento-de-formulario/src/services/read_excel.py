import pandas as pd
import os

def read_excel():

    file_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'datas.xlsx')

    df = pd.read_excel(file_path)

    return df