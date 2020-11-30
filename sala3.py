class Sala3:
  def __init__(self, situacao: str = None):
    self.__situacao = situacao

  @property
  def mostra_situacao_sala3(self):
    return self.__situacao

  @mostra_situacao_sala3.setter
  def definir_situacao_sala3(self, situacao: str = None):
    self.__situacao = situacao