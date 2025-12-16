"""
CONSTANTE = : "Variaveis " que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade =61 # Velocidade atual do carro
local_carro = 100 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade maxima do radar 1
LOCAL_1 = 100 # Local do radar 1 esta
RADAR_RANGE = 1 # Alcance do radar 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and vel_carro_pass_radar_1
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do limite do radar 1')

if carro_passou_radar_1:
    print('Carro passou pelo radar 1')

if carro_multado_radar_1:
    print('Carro multado pelo radar 1')