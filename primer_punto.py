def consultar_horario(materia):
    horarios = {
        "Calculo integral": {"Día": "Martes y Jueves", "Hora": "07:00 a 09:00", "Salón": "406 D.B", "Profesor": "Jairo Lalinde"},
        "Fisica mecanica": {"Día": "Martes y Jueves", "Hora": "09:00 a 11:00", "Salón": "404 D.B", "Profesor": "Roberto Bohorquez"},
        "Programacion aplicada a sistemas mecatronicos": {"Día": "Martes y Jueves", "Hora": "13:00 a 15:00", "Salón": "305 G:O", "Profesor": "Nicolas Torres"},
        "Circuitos D.C": {"Día": "Miercoles y VIernes", "Hora": "11:00 a 13:00", "Salón": "306 D:B", "Profesor": "Roberto Bohorquez"},
        "Cultura ecologica": {"Día": "Viernes", "Hora": "09:00 a 11:00", "Salón": "306 P.S", "Profesor": "Yuberney Sanchez"},
        "Taller de fisica mecanica": {"Día": "Viernes", "Hora": "15:00 a 17:00", "Salón": "206 P.S", "Profesor": "Paula Dorado"}
    }


    if materia in horarios:
     
        print("Día:", horarios[materia]["Día"])
        print("Hora:", horarios[materia]["Hora"])
        print("Salón:", horarios[materia]["Salón"])
        print("Profesor:", horarios[materia]["Profesor"])
    else:
        print("La materia no se encontró en el horario.")
