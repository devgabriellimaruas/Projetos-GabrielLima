from openpyxl.styles import Font, Alignment


def estilo_celulas(planilha):
    largura_titulos = {
        'A': (21, 'Estado'),
        'B': (12, 'Sigla'),
        'C': (21, 'Região')
    }

    for coluna, (largura, titulo) in largura_titulos.items():
        planilha.column_dimensions[coluna].width = largura
        celula_largura_titulo = planilha[f'{coluna}1']
        celula_largura_titulo.value = titulo

    estilo_titulo = Font(bold=True, size=14)
    alignment_titulo = Alignment(horizontal='center', vertical='center')

    celula_titulo = ['A1', 'B1', 'C1']

    for estilos in celula_titulo:
        celula_titulo_estilo = planilha[estilos]
        celula_titulo_estilo.font = estilo_titulo
        celula_titulo_estilo.alignment = alignment_titulo
