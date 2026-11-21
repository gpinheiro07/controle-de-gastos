from datetime import date
from gastos.modelos import Gasto, formatar_reais
from gastos.servicos import filtrar_por_mes, total_geral, total_por_categoria


gastos = [
    Gasto("Almoço", 3550, "alimentação", date(2026, 3, 2)),
    Gasto("Ônibus", 1200, "transporte", date(2026, 3, 2)),
    Gasto("Mercado", 25890, "alimentação", date(2026, 2, 27)),
]

print(f"Total geral: {formatar_reais(total_geral(gastos))}")

for categoria, total in total_por_categoria(gastos).items():
    print(f"{categoria}: {formatar_reais(total)}")

marco = filtrar_por_mes(gastos, 2026, 3)

print(f"Março de 2026: {formatar_reais(total_geral(marco))}")
