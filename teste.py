from datetime import datetime

class Relogio:
    def obter_posicao_ponteiro_hora(self, hora, minuto):
        if hora == 12:
            hora = 0
        if minuto == 60:
            minuto = 0
        return int(0.5 * (hora * 60 + minuto))

    def obter_posicao_ponteiro_minuto(self, minuto):
        if minuto == 60:
            minuto = 0
        return int(minuto * 6)

    def retorna_angulo_relogio(self, horario):
        posicao_ponteiro_hora = self.obter_posicao_ponteiro_hora(horario.hour, horario.minute)
        posicao_ponteiro_minuto = self.obter_posicao_ponteiro_minuto(horario.minute)

        angulo = abs(posicao_ponteiro_hora - posicao_ponteiro_minuto)
        angulo = min(360 - angulo, angulo)
        return angulo

# Horários a serem analisados
horarios = [datetime.strptime("00:00", "%H:%M"), 
            datetime.strptime("00:15", "%H:%M"), 
            datetime.strptime("00:30", "%H:%M")]

# Calcular e exibir os ângulos para cada horário
relogio = Relogio()
for horario in horarios:
    angulo = relogio.retorna_angulo_relogio(horario)
    print(f"Para {horario.hour:02d}:{horario.minute:02d}h:")
    print(f"O ângulo entre os ponteiros é de {angulo}°.")
    print()
    