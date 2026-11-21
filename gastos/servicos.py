from gastos.modelos import Gasto


def total_geral(gastos: list[Gasto]) -> int:
    total = 0
    for gasto in gastos:
        total += gasto.valor_centavos
    return total


def total_por_categoria(gastos: list[Gasto]) -> dict[str, int]:
    totais: dict[str, int] = {}
    for gasto in gastos:
        totais[gasto.categoria] = totais.get(gasto.categoria, 0) + gasto.valor_centavos
    return totais


def filtrar_por_categoria(gastos: list[Gasto], categoria: str) -> list[Gasto]:
    return [gasto for gasto in gastos if gasto.categoria == categoria]


def filtrar_por_mes(gastos: list[Gasto], ano: int, mes: int) -> list[Gasto]:
    return [gasto for gasto in gastos if gasto.data.year == ano and gasto.data.month == mes]


