class Produto:
    def __init__(self, nomeproduto, valorUnitario, quantidade, setor):
        self.nomeproduto = nomeproduto
        self.valorUnitario = valorUnitario
        self.quantidade = quantidade
        self.setor = setor

    def calcular_valor_total_estoque(self):
        return self.quantidade * self.valorUnitario

    def apresentar_produto(self):
        print(f"Produto: {self.nomeproduto} | Quantidade: {self.quantidade} | "
              f"Valor unitário: R$ {self.valorUnitario:.2f} | Setor: {self.setor}")


produto1 = Produto("Arroz", 25.90, 10, "Alimentos")
produto2 = Produto("Feijão", 8.50, 20, "Alimentos")
produto3 = Produto("Detergente", 3.75, 15, "Limpeza")
produto4 = Produto("Caderno", 18.90, 8, "Papelaria")
produto5 = Produto("Caneta", 2.50, 30, "Papelaria")


produtos = [produto1, produto2, produto3, produto4, produto5]

for produto in produtos:
    produto.apresentar_produto()
    print(f"Valor total em estoque: R$ {produto.calcular_valor_total_estoque():.2f}")
    print("-" * 60)

