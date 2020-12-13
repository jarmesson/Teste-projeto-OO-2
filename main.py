from secretaria import Secretaria
from sala1 import Sala
from dia import Dia
from reserva import Reserva
from socio import Socio

socio = Socio()
socio.nome = 'Mathias'

socio2 = Socio()
socio2.nome = 'Lucas'

func = Secretaria()
func.nome = 'Rita'
func.ramal = 6546543
func.cargo = 'Secretária'
func.socio = socio
func.socio2 = socio2

sala = Sala()
sala.nome = 'SALA 1 - Sala de Reuniões'
sala.situacao = 'Ocupada'
sala.func = func

sala2 = Sala()
sala2.nome = 'SALA 2 - Sala de Reuniões'
sala2.situacao = 'Ocupada'
sala2.func = func

sala3 = Sala()
sala3.nome = 'SALA 3 - Sala de Reuniões'
sala3.situacao = 'Ocupada'
sala3.func = func

sala4 = Sala()
sala4.nome = 'SALA 4 - Sala de Reuniões'
sala4.situacao = 'Ocupada'
sala4.func = func

teste = Dia()
teste.definir_hora = '8:00 às 9h00'
teste.definir_dia = 15
teste.definir_mes = 'Agosto'
teste.sala = sala

reserva = Reserva()
reserva.adicionar_reservas(sala.nome, teste.mostra_dia, teste.mostra_mes, teste.mostra_hora, teste.sala.func.socio.nome)
reserva.adicionar_reservas(sala2.nome, teste.mostra_dia, teste.mostra_mes, teste.mostra_hora, teste.sala.func.socio.nome)
reserva.adicionar_reservas(sala3.nome, teste.mostra_dia, teste.mostra_mes, teste.mostra_hora, teste.sala.func.socio2.nome)
reserva.remover_reserva(sala3.nome, teste.mostra_dia, teste.mostra_mes, teste.mostra_hora, teste.sala.func.socio2.nome)
reserva.adicionar_reservas(sala4.nome, teste.mostra_dia, teste.mostra_mes, teste.mostra_hora, teste.sala.func.socio2.nome)
# reserva.troca_horario_sala('SALA 4 - Sala de Reuniões')

# reserva.troca_sala_socio('Lucas','Pedro', 'SALA 4 - Sala de Reuniões')

reserva.exibir_reservas()