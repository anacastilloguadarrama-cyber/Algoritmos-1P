#Este programa calcula la ley de Ohm
print("Ley de ohm")
print("Selecciona la opcion")
opcion=int(input("1=voltaje, 2=corriente, 3=resistencia: "))
try:
    if opcion==1=:
        resistencia=float(input("Ingresa la resistencia(ohm): "))
        corriente=float(input("Ingresa la corriente(Amperios): "))

"""
Programa para calcular la Ley de Ohm
Opciones:
1. Calcular Voltaje (V = I * R)
2. Calcular Corriente (I = V / R)
3. Calcular Resistencia (R = V / I)
"""
print("Ley de Ohm")
print("Selecciona la opción:")
print("1 = Voltaje (V)")
print("2 = Corriente (I)")
print("3 = Resistencia (R)")

try:
    opcion = int(input("Elige una opción (1, 2 o 3): "))
    if opcion == 1:
        resistencia = float(input("Ingresa la resistencia (Ohm): "))
        corriente = float(input("Ingresa la corriente (Amperios): "))
        voltaje = resistencia * corriente
        print(f"El voltaje es: {voltaje:.2f} V")
    elif opcion == 2:
        voltaje = float(input("Ingresa el voltaje (Voltios): "))
        resistencia = float(input("Ingresa la resistencia (Ohm): "))
        if resistencia == 0:
            print("Error: La resistencia no puede ser cero.")
        else:
            corriente = voltaje / resistencia
            print(f"La corriente es: {corriente:.2f} A")
    elif opcion == 3:
        voltaje = float(input("Ingresa el voltaje (Voltios): "))
        corriente = float(input("Ingresa la corriente (Amperios): "))
        if corriente == 0:
            print("Error: La corriente no puede ser cero.")
        else:
            resistencia = voltaje / corriente
            print(f"La resistencia es: {resistencia:.2f} Ohm")
    else:
        print("Opción no válida. Elige 1, 2 o 3.")
except ValueError:
    print("Error: Ingresa valores numéricos válidos.")
