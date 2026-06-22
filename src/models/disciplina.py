from dataclasses import dataclass

@dataclass
class Disciplina:
    codigo:str
    nome:str
    sala:str
    horarios_sigaa:list[str]
    horarios_formatados:list[str]
    professor:Professor
    dificuldade:int
