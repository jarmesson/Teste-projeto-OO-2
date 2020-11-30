class Sala4:
  def __init__(self, situacao: str = None):
    self.__situacao = situacao

  @property
  def mostra_situacao_sala4(self):
    return self.__situacao

  @mostra_situacao_sala4.setter
  def definir_situacao_sala4(self, situacao: str = None):
    self.__situacao = situacao