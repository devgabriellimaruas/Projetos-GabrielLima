import pyautogui, time

def fill_form(df):
    print("Início da automação")
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    # print("Olá")
    time.sleep(1)
    # print(pyautogui.position())
    
    pyautogui.click(x=574, y=838)
    time.sleep(2)
    pyautogui.hotkey('win', 'up')
    pyautogui.click(x=720, y=63)
    pyautogui.write("https://projetos-devgabriellimaruas-yyd3jf.flutterflow.app/formulario")
    pyautogui.press("enter")
    time.sleep(3)
    
    for index, row in df.head().iterrows():
        time.sleep(1)
        #Nome
        pyautogui.click(x=754, y=439)
        pyautogui.write(row["Nome"])

        #Sobrenome
        pyautogui.click(x=998, y=440)
        pyautogui.write(row["Sobrenome"])

        #Email
        pyautogui.click(x=946, y=529)
        pyautogui.write(row["Email"])

        #Endereço
        pyautogui.click(x=769, y=619)
        pyautogui.write(row["Endereço"])

        #Cidade
        pyautogui.click(x=721, y=700)
        pyautogui.write(row["Cidade"])

        #CEP
        pyautogui.click(x=1008, y=696)
        pyautogui.write(row["CEP"])

        #Salvar
        pyautogui.click(x=1010, y=771)

    #Histórico
    pyautogui.click(x=862, y=769)

    time.sleep(10)
    
    #Fechar
    pyautogui.click(x=1888, y=18)
    return "Fim da automação"