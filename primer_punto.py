def consultar_horario(materia):
    horarios=[
        ["Calculo integral", "Martes y Jueves", "07:00 a 09:00", "406 D.B", "Jairo Lalinde"],
        ["Fisica mecanica", "Martes y Jueves", "09:00 a 11:00", "404 D.B", "Roberto Bohorquez"],
        ["Programacion aplicada a sistemas mecatronicos", "Martes y Jueves", "13:00 a 15:00", "305 G:O", "Nicolas Torres"],
        ["Circuitos D.C", "Miercoles y VIernes", "11:00 a 13:00", "306 D:B", "Roberto Bohorquez"],
        ["Cultura ecologica", "Viernes", "09:00 a 11:00", "306 P.S", "Yuberney Sanchez"],
        ["Taller de fisica mecanica", "Viernes", "15:00 a 17:00", "206 P.S", "Paula Dorado"]
    ]
    
    for curso in horarios:
        if curso[0] == materia:
            print("Día:", curso[1])
            print("Hora:", curso[2])
            print("Salón:", curso[3])
            print("Profesor:", curso[4])
            return
    print("La materia no se encontró en el horario.")
