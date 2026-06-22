from dataclasses import dataclass
from models.professor import Professor

@dataclass
class Disciplina:
    codigo:str
    nome:str
    sala:str
    horarios_sigaa:list[str]
    horarios_formatados:list[str]
    professor:Professor
    dificuldade:int
