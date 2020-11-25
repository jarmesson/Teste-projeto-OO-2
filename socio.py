class Socio:
  def __init__(self, nome: str = None, cargo: str = None, ramal: int = None):
    self.__nome = nome
    self.__cargo = cargo
    self.__ramal = ramal

  #getters
  @property
  def mostra_nome(self):
    return self.__nome

  @property
  def mostra_cargo(self):
    return self.__cargo

  @property
  def mostra_ramal(self):
    return self.__ramal

  #setters
  @mostra_nome.setter
  def definir_nome(self, nome: str = None):
    self.__nome = nome

  @mostra_cargo.setter
  def definir_cargo(self, cargo: str = None):
    self.__cargo = cargo

  @mostra_ramal.setter
  def definir_ramal(self, ramal: str = None):
    self.__ramal = ramal


