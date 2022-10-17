# Si leemos  una temperatura, determinar si es normal o no. 
temperatura = float(input("dame tu temperatura: "))
if temperatura >= 36.8 and temperatura <= 37.2:
    print ("Temperatura Normal")
else:
    print ("Debes ir al medico")
