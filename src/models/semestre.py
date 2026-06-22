from dataclasses import dataclass

@dataclass
class Semestre:
    nome:str
    disciplinas:list[Disciplina]
    percentual_conclusao:float
