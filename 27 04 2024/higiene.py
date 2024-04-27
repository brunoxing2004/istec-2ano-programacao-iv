class Produto():
  def __init__(self, descricao, preco):
    self.descricao = descricao
    self.preco = preco
    

class Alimentacao(Produto):
  def __init__(self, descricao, preco):
    super().__init__(descricao, preco)
