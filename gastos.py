def criar_gasto(descricao: str, valor_centavos: int, categoria: str) -> dict:
    if type(valor_centavos) is not int:
        raise ValueError("O valor deve ser um número inteiro (em centavos).")
    if valor_centavos <= 0:
        raise ValueError("O valor deve ser positivo.")
    if descricao.strip() == "":
        raise ValueError("A descrição não pode ser vazia.")
    if categoria.strip() == "":
        raise ValueError("A categoria não pode ser vazia.")

    return {
        "descricao": descricao.strip(),
        "valor_centavos": valor_centavos,
        "categoria": categoria.strip().lower(),
    }


def total_por_categoria(gastos: list) -> dict:
    totais = {}
    for gasto in gastos:
        categoria = gasto["categoria"]
        totais[categoria] = totais.get(categoria, 0) + gasto["valor_centavos"]
    return totais


def total_geral(gastos: list) -> int:
    total = 0
    for gasto in gastos:
        total += gasto["valor_centavos"]
    return total


def formatar_reais(centavos: int) -> str:
    reais = centavos // 100
    resto = centavos % 100
    return f"R$ {reais},{resto:02d}"


gastos = []

try:
    gastos.append(criar_gasto("Almoço", 3550, "Alimentação"))
    gastos.append(criar_gasto("Uber", 2290, "Transporte"))
    gastos.append(criar_gasto("Café", 800, "alimentação"))
    gastos.append(criar_gasto("Teste", -100, "Outros"))  # vai dar erro
except ValueError as erro:
    print(erro)

print(gastos)

totais = total_por_categoria(gastos)
for categoria in totais:
    print(f"{categoria}: {formatar_reais(totais[categoria])}")

print(f"Total geral: {formatar_reais(total_geral(gastos))}")
