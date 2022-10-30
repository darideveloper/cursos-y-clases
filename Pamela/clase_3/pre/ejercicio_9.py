empleados = {
    'Juan' : 45, 
    'Maria': 25,
    'Alex': 29,
    'Sofia': 48
}

pago_hora = 12

for nombre, horas in empleados.items():
        
    if horas <= 40:
        # Calcular salario sin horas extra
        salario = horas * pago_hora
    else:
        # Calcular salario base
        salario_base = 40 * pago_hora
        
        # Calcular pago de horas extra
        horas_extra = horas - 40 
        horas_extra_pago = horas_extra * pago_hora * 1.5
        
        # Calcular salario
        salario = salario_base + horas_extra_pago
        
    # Convertir salario a entero
    salario = float(salario)
        
    print (f"{nombre} trabajó {horas} horas y su salario es de: {salario}")