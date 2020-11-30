class Sala2:
  def __init__(self, situacao: str = None):
    self.__situacao = situacao

  @property
  def mostra_situacao_sala2(self):
    return self.__situacao

  @mostra_situacao_sala2.setter
  def definir_situacao_sala2(self, situacao: str = None):
    self.__situacao = situacao