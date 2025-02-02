import os
from src.models.estados import estados
from src.services.excel import excel
from botcity.web import WebBot, Browser, By
from botcity.maestro import *
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    bot.driver_path = r"C:\Users\User\Documents\GitHub\GitHubGabrielLima\Projetos-GabrielLima\WebScraping-BotCity\dados_ibge\chromedriver.exe"

    bot.browse("https://www.ibge.gov.br/cidades-e-estados/")
    bot.maximize_window()

    json_estados = []
    lista_estados = estados()
    lista_estados.sort()

    cont = 0
    for estado in lista_estados:
        if not bot.find( "pesquisar_estado", matching=0.97, waiting_time=10000):
            not_found("pesquisar_estado")
        bot.click_relative(308, 11)

        bot.paste(estado)
        bot.enter()

        bot.wait(2000)
        bot.scroll_down(2)

        # area territorial
        if not bot.find( "area", matching=0.80, waiting_time=10000):
            not_found("area")
        bot.double_click_relative(414, 16)
        bot.control_c()
        area = bot.get_clipboard()

        # populacao
        if not bot.find( "populacao", matching=0.80, waiting_time=10000):
            not_found("populacao")
        bot.double_click_relative(423, 13)
        bot.control_c()
        populacao = bot.get_clipboard()
        bot.scroll_down(2)

        # Governador
        if not bot.find( "governador", matching=0.80, waiting_time=10000):
            not_found("governador")
        bot.triple_click_relative(245, 7)
        bot.control_c()
        governador = bot.get_clipboard()

        # capital
        if not bot.find( "capital", matching=0.80, waiting_time=10000):
            not_found("capital")
        bot.triple_click_relative(196, 6)
        bot.control_c()
        capital = bot.get_clipboard()

        # gentilico
        if not bot.find( "gentilico", matching=0.80, waiting_time=10000):
            not_found("gentilico")
        bot.triple_click_relative(195, 7)
        bot.control_c()
        gentilico = bot.get_clipboard()

        json_estados.append({
            "Estado": estado,
            "Area": f"{area} km²",
            "Populacao": f"{populacao} pessoas",
            "Governador": governador,
            "Capital": capital,
            "Gentilico": gentilico
        })
        cont += 1
        print(f'{cont}/{len(lista_estados)} - Dados coletados: {estado}')
        
        bot.scroll_up(5)

    #Adicionar no excel
    planilha_excel = excel(json_estados)
    print(planilha_excel)
    
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

