name = input('Hola esta es una calculadora, por favor dime tu nombre: ')
print("Vamos a realizar la suma de dos valore")
val_sum_1 = int(input(f"{name} por favor ingresa el sumando 1: "))
val_sum_2 = int(input(f"{name} por favor ingresa el sumando 2: "))
res_sum = val_sum_1 + val_sum_2
print(f"{name} el resultado de la suma es {res_sum}")

# vamos a realizar la resta

print("Vamos a realizar la resta de dos valore")
val_res_1 = int(input(f"{name} por favor ingresa el valor 1: "))
val_res_2 = int(input(f"{name} por favor ingresa el valor 2: "))
res_res = val_res_1 - val_res_2
print(f"{name} el resultado de la resta es {res_res}")