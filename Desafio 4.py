#Desafio 4 - Desafio dos três interruptores

# Variáveis para lâmpadas
lampada1 = "quente e apagada"
lampada2 = "acesa"
lampada3 = "apagada e fria"

# Variáveis para o estado dos interruptores
interruptor1 = "desligado"
interruptor2 = "desligado"
interruptor3 = "desligado"

#Passo 1, Acende o primeiro interruptor

interruptor1 = "ligado"

# Passo 2, esperar alguns minutos...

# Passo 3, acender o segundo interruptor
interruptor2 = "ligado"

#Passo 4, verificar o estado dos interruptores
if lampada1 == "quente e apagada":
    interruptor_correspondente_1 = 1
elif lampada2 == "acesa":
    interruptor_correspondente_2 = 1
else:
    interruptor_correspondente_3 = 1

if lampada2 == "acesa":
    interruptor_correspondente_2 = 2
elif lampada1 == "quente e apagada":
    interruptor_correspondente_1 = 2
else:
    interruptor_correspondente_3 = 2

if lampada3 == "apagada e fria":
    interruptor_correspondente_3 = 3
elif lampada1 == "quente e apagada":
    interruptor_correspondente_1 = 3
else:
    interruptor_correspondente_2 = 3

# Passo 5, Observar os resultados
print("O interruptor 1 controla a lâmpada:", interruptor_correspondente_1)
print("O interruptor 2 controla a lâmpada:", interruptor_correspondente_2)
print("O interruptor 3 controla a lâmpada:", interruptor_correspondente_3)
