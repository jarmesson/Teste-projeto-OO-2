from sala1 import Sala
from dia import Dia

class Reserva:
  def __init__(self):
    self.__reserva = []

  def adicionar_reservas(self):
    for i in range (len(self.__reserva)):
      if self.mostra_hora == self.__reserva[i].hora:
        if self.mostra_dia == self.__reserva[i].dia:
          if self.mostra_mes == self.reserva[i].mes:
            print('Ja existe um agendamento ativo para essa sala neste dia.')
            return
    self.__reserva.append()
    
