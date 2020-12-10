from socio import Socio
from sala1 import Sala
from dia import Dia
from reserva import Reserva

func = Socio()
func.definir_nome = 'Jarmesson'
func.definir_cargo = 'Diretor'
func.definir_ramal = 5445654

print(func.definir_cargo, func.definir_nome)

sala = Sala()
sala.nome = 'SALA 1 - Sala de Reuniões'
sala.situacao = 'Ocupada'

print()

reserva = Reserva()

reserva.adicionar_reservas(func)