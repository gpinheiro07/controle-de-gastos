from dataclasses import dataclass
from datetime import date


def formatar_reais(valor_centavos: int) -> str:
    reais, centavos = divmod(valor_centavos, 100)
    return f"R$ {reais},{centavos:02d}"


@dataclass
class Gasto:
    descricao: str
    valor_centavos: int
    categoria: str
    data: date
    
    def __post_init__(self) -> None:
        if self.descricao.strip() == "":
            raise ValueError("A descrição não pode ser vazia.")
        if not isinstance(self.valor_centavos, int) or self.valor_centavos <= 0:
            raise ValueError(f"Valor inválido: {self.valor_centavos}. Informe um número inteiro positivo, em centavos.")
        if self.categoria.strip() == "":
            raise ValueError("A categoria não pode ser vazia.")
        if not isinstance(self.data, date):
            raise ValueError(f"Data inválida: {self.data}. Informe um objeto date.")
    
    def valor_formatado(self) -> str:
        return formatar_reais(self.valor_centavos)
