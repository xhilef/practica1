def clasificar_temperatura(temperatura):
    if not isinstance(temperatura, (int, float)):
        raise TypeError("El valor debe ser numérico")
    
    # los límites físicos y de requerimiento
    if temperatura < -273 or temperatura > 10000:
        raise ValueError("Temperatura fuera del rango válido -273°C a 10,000°C")

    if temperatura <= 15:
        return "Frío"
    elif 16 <= temperatura <= 25:
        return "Templado"
    else:
        return "Caliente"