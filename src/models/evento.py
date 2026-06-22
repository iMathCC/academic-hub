from dataclasses import dataclass
from datetime import date

@dataclass
class Evento:
    titulo:str
    tipo:str
    prazo:date
    disciplina:Disciplina
    concluido:bool
