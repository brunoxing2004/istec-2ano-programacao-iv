from produto import Produto

class Alimentacao(Produto):
  def __init__(self, descricao, preco):
    super().__init__(descricao, preco)