DIAS = {
        "2":"Segunda",
        "3":"Terça",
        "4":"Quarta",
        "5":"Quinta",
        "6":"Sexta",
}

HORARIOS = {
        "M23":("08:00", "10:00"),
        "M45":("10:00", "12:00"),
        "T23":("14:00", "16:00"),
        "T45":("16:00", "18:00"),
}

def traduzir_horario(codigo:str) -> dict:
    if codigo[0] not in DIAS:
        raise ValueError("Dia inválido!")
    if codigo[1:] not in HORARIOS:
        raise ValueError("Horário inválido!")

    dia = DIAS[codigo[0]]
    periodo = codigo[1:]
    inicio, fim = HORARIOS[periodo]

    return {
        "dia":dia,
        "inicio":inicio,
        "fim":fim,
    }
