def clasificar_calificacion(calificacion):
    if not isinstance(calificacion, (int, float)):
        raise TypeError("La calificación debe ser numérica")

    if calificacion < 0 or calificacion > 10:
        raise ValueError("La calificación debe estar entre 0 y 10")

    if calificacion < 6:
        return "Reprobado"
    elif 6 <= calificacion <= 8:
        return "Aprobado"
    else:  # 9 a 10
        return "Sobresaliente"